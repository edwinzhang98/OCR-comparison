#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Donut 批量测试器（Batch Tester） + 自动路由
----------------------------------------
• 遍历输入文件夹中的所有图片
• 支持两种工作方式：
  1) 直接按你指定的预设（presets）逐一运行；
  2) **自动路由（--auto_route）**：先用“探针”判定页面类型（表/公式/图/混合），再自动选择合适的预设；
• 同一张图片的所有模式结果汇总到 **同一个** JSON 文件中，便于对比
• 保留数据路径与模型/预设占位，便于你按需修改

环境建议：transformers >= 4.38, torch >= 2.0, Pillow

安装示例（使用 uv）：
# 1) 创建并激活虚拟环境
uv venv .venv
# macOS/Linux
source .venv/bin/activate
# Windows PowerShell
# .venv\Scripts\Activate.ps1

# 2) 安装依赖
uv pip install -U torch torchvision pillow transformers accelerate

说明：
- Donut 是 OCR‑free 的文档理解模型。不同 checkpoint 往往需要不同的任务前缀（task prompt）。
  如果你使用的权重在 Hugging Face README 里给了示范 prompt，请把它填到下方 PRESETS 的
  "task_prompt" 字段。
- 对“教材类页面的通用读文本（pseudo‑OCR）”，优先尝试 SynthDoG 系列微调权重。
  示例："naver-clova-ix/donut-base-finetuned-synthdog"（通用文本读取）
- 若是文档问答（DocVQA），使用 *_docvqa 微调权重，并在 prompt 中提供问题。

脚本还会把能力信息（生成参数、tokenizer 新增 token、图像处理配置）
导出到 <output_dir>/capabilities.json，以便排查与复现实验。
"""
from __future__ import annotations
import argparse
import json
import os
import sys
import time
import inspect
import re
from dataclasses import dataclass, asdict
from typing import Dict, Any, List, Optional

from PIL import Image
import torch
from transformers import VisionEncoderDecoderModel
from transformers import DonutProcessor

# ---------------------------
# 默认配置（你可以改这里）
# ---------------------------
DEFAULT_INPUT_DIR = "data/pdf_ocr_samples"   # 使用已有的样本图片目录
DEFAULT_OUTPUT_DIR = "output/donut_results"   # 结果保存目录
DEFAULT_MODEL_ID = "naver-clova-ix/donut-base"  # 通用基础模型
# 其他基础模型可用："naver-clova-ix/donut-base"

# 若 GPU 显存允许，在 CUDA 上用 FP16 可提升推理速度
DEFAULT_USE_FP16 = True

# 是否默认启用自动路由（也可用 --auto_route 开关覆盖）
DEFAULT_AUTO_ROUTE = False

# ---------------------------
# 预设参数模板（Presets）
# ---------------------------
# 每个预设控制三类参数：
#   - task_prompt：解码器的任务前缀/提示（不同 checkpoint 可能不同）
#   - gen：传给 model.generate 的生成参数
#   - iproc：本次运行的图像预处理覆盖项（例如重新设定输入尺寸）
#
# 针对“教材页包含表格/图片/公式”的场景，给出若干可直接使用的预设；
# 你可以自由增删或调整。
PRESETS: Dict[str, Dict[str, Any]] = {
    # 速度快、确定性强的初筛；先看能否顺畅读出正文。
    "fast_draft": {
        "task_prompt": "",  # 若 checkpoint 需要如 "<s_synthdog>" 等起始 token，请写在这里
        "gen": {
            "max_new_tokens": 384,
            "num_beams": 1,
            "do_sample": False,
            "early_stopping": True,
            "repetition_penalty": 1.05,
            "no_repeat_ngram_size": 3,
        },
        "iproc": {
            # 示例：Donut 默认常用短边约 1280；
            # 如需手动设定尺寸，取消注释：
            # "size": {"height": 1280, "width": 960},
        },
        "description": "快速且确定性的粗读，适合先看页面主体内容。"},

    # 平衡的束搜索，提升结构稳定性，减少列表/表格重复。
    "balanced_beam": {
        "task_prompt": "",
        "gen": {
            "max_new_tokens": 768,
            "num_beams": 4,
            "do_sample": False,
            "early_stopping": True,
            "repetition_penalty": 1.1,
            "no_repeat_ngram_size": 4,
            "length_penalty": 0.95,
        },
        "iproc": {
            # 可按需提高输入分辨率：
            # "size": {"height": 1440, "width": 1024},
        },
        "description": "结构更干净，适合含表格与混合内容的页面。"},

    # 面向长页面（多图/多公式/内容密集），以完整性为优先，牺牲一点速度。
    "long_page_strict": {
        "task_prompt": "",
        "gen": {
            "max_new_tokens": 1400,
            "num_beams": 3,
            "do_sample": False,
            "early_stopping": False,
            "repetition_penalty": 1.12,
            "no_repeat_ngram_size": 4,
        },
        "iproc": {
            # 显存允许时可适度增大输入尺寸：
            # "size": {"height": 1600, "width": 1130},
        },
        "description": "面向长页与密集信息，尽量覆盖更多内容。"},

    # 鼓励把清晰的公式按 LaTeX 风格转写；保持确定性。
    "formula_friendly": {
        # 若权重支持自然语言任务提示，可用下述提示引导公式转写风格：
        "task_prompt": "Transcribe math as LaTeX when clear; keep original text for body.",
        "gen": {
            "max_new_tokens": 1024,
            "num_beams": 4,
            "do_sample": False,
            "early_stopping": True,
            "repetition_penalty": 1.15,
            "no_repeat_ngram_size": 3,
            "length_penalty": 1.0,
        },
        "iproc": {},
        "description": "对公式更友好，偏向 LaTeX 式转写，正文保持原文风格。"},

    # 尝试把表格渲染为 Markdown；结构不确定时适当使用采样有时更稳。
    "table_markdown": {
        "task_prompt": "If tables are present, render them as GitHub-flavored Markdown; otherwise read text.",
        "gen": {
            "max_new_tokens": 900,
            "num_beams": 1,
            "do_sample": True,
            "temperature": 0.7,
            "top_p": 0.9,
            "repetition_penalty": 1.05,
            "no_repeat_ngram_size": 3,
        },
        "iproc": {},
        "description": "鼓励生成 Markdown 表格；遇到不稳定版面时更灵活。"},

    # 一句话级别的页面摘要/说明，便于快速浏览。
    "page_summary": {
        "task_prompt": "Provide a concise one-sentence summary of the page content.",
        "gen": {
            "max_new_tokens": 64,
            "num_beams": 1,
            "do_sample": True,
            "temperature": 0.8,
            "top_p": 0.92,
        },
        "iproc": {},
        "description": "生成页面的简短摘要（非通用自然图像 captioning）。"},

    # ===== 通用一把梭：能结构化就结构化，复杂就降级为 caption+要点 =====
    "universal_doc": {
        "task_prompt": (
            "Analyze the page image and output STRICT JSON with keys: "
            "{"
            "\"page_type\": [\"table\"|\"equation\"|\"figure\"|\"text\"|\"mixed\"], "
            "\"tables_md\": [], \"equations_latex\": [], "
            "\"caption\": \"\", \"text\": \"\"" 
            "}. "
            "Rules: "
            "1) If the page is predominantly a TABLE and small enough, transcribe it exactly as GitHub-Flavored Markdown into tables_md. "
            "2) If the page is predominantly EQUATIONS with little body text, transcribe equations into equations_latex (LaTeX). "
            "3) If the layout is MIXED or too large to reproduce, do NOT hallucinate; return a short caption and key body text; keep tables_md/equations_latex empty. "
            "Always return valid JSON and no text outside JSON."
        ),
        "gen": {
            "max_new_tokens": 1000,
            "num_beams": 4,
            "do_sample": False,
            "early_stopping": True,
            "no_repeat_ngram_size": 4,
            "repetition_penalty": 1.10,
            "length_penalty": 1.0
        },
        "iproc": { "size": {"height": 1440, "width": 1024} },
        "description": "通用 preset：统一 JSON 协议；表/式优先结构化，复杂则降级摘要。"},

    # ===== 路由探针：极短 JSON 分类输出（表/式/图/文本/混合 & 表格大小 & 置信度） =====
    "router_probe": {
        "task_prompt": (
            "Classify the page layout. Output STRICT JSON ONLY with keys: "
            "{\"is_table\": bool, \"is_equation\": bool, \"is_figure\": bool, "
            " \"is_text\": bool, \"dominant\": \"table|equation|figure|text|mixed\", "
            " \"table_size\": \"none|small|large\", \"confidence\": number}."
        ),
        "gen": {
            "max_new_tokens": 48,
            "num_beams": 1,
            "do_sample": False,
            "early_stopping": True
        },
        "iproc": { "size": {"height": 1280, "width": 960} },
        "description": "快速判别版式类型+表格大小+置信度。"},

    # —— 公式短图：只转写可见公式，倾向 LaTeX，尽量少废话 ——
    "eq_compact": {
        "task_prompt": "Transcribe visible equations using LaTeX; keep inline math inline; do not invent symbols.",
        "gen": {
            "max_new_tokens": 160,
            "num_beams": 4,
            "do_sample": False,
            "no_repeat_ngram_size": 2,
            "repetition_penalty": 1.20,
            "early_stopping": True
        },
        "iproc": { "size": {"height": 1024, "width": 768} },
        "description": "短/单行公式，高保真、低冗余。"},

    # —— 表格（小到中等）：精确复刻为 Markdown ——
    "table_strict_md": {
        "task_prompt": "Extract all tables as GitHub-Flavored Markdown. Preserve headers, numbers, and punctuation exactly. Do not summarize.",
        "gen": {
            "max_new_tokens": 480,
            "num_beams": 4,
            "do_sample": False,
            "no_repeat_ngram_size": 4,
            "repetition_penalty": 1.10,
            "length_penalty": 1.00
        },
        "iproc": { "size": {"height": 1440, "width": 1024} },
        "description": "小/中表格的严谨复刻。"},

    # —— 宽/长表格：允许更长输出 ——
    "wide_table_md": {
        "task_prompt": "If the table is wide, split into multiple Markdown tables by logical sections. Preserve header rows; avoid wrapping cell content.",
        "gen": {
            "max_new_tokens": 1400,
            "num_beams": 3,
            "do_sample": False,
            "no_repeat_ngram_size": 4,
            "repetition_penalty": 1.12,
            "early_stopping": False
        },
        "iproc": { "size": {"height": 1600, "width": 1130} },
        "description": "宽/长表（结果表）更稳。"},

    # —— 图示+说明：提取结构化要点（最多 5 条） ——
    "figure_bullets": {
        "task_prompt": "Summarize the figure with up to 5 bullet points: (1) key entities, (2) relationships, (3) notable labels/values.",
        "gen": {
            "max_new_tokens": 180,
            "num_beams": 1,
            "do_sample": True,
            "temperature": 0.7,
            "top_p": 0.9
        },
        "iproc": { "size": {"height": 1280, "width": 960} },
        "description": "架构图/示意图的要点摘要。"},
}


# ---------------------------
# 数据结构
# ---------------------------
@dataclass
class RunResult:
    preset: str
    prompt: str
    image_processor_overrides: Dict[str, Any]
    generation_kwargs: Dict[str, Any]
    output_text: Optional[str]
    output_json: Optional[Dict[str, Any]]
    runtime_sec: float
    num_generated_tokens: Optional[int]
    error: Optional[str]


# ---------------------------
# 工具函数
# ---------------------------
IMG_EXTS = {".png", ".jpg", ".jpeg", ".webp", ".bmp", ".tif", ".tiff"}

def list_images(folder: str) -> List[str]:
    """递归列出目录下所有受支持的图片路径（按文件名排序）。"""
    files = []
    for root, _, names in os.walk(folder):
        for n in sorted(names):
            if os.path.splitext(n.lower())[1] in IMG_EXTS:
                files.append(os.path.join(root, n))
    return files


def ensure_dir(p: str):
    """若目录不存在则创建。"""
    os.makedirs(p, exist_ok=True)


def save_json(path: str, obj: Any):
    """以 UTF‑8 和缩进写入 JSON 文件。"""
    with open(path, "w", encoding="utf-8") as f:
        json.dump(obj, f, ensure_ascii=False, indent=2)


def load_json(path: str) -> Any:
    """读取 JSON 文件为 Python 对象。"""
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def image_processor_apply_overrides(processor: DonutProcessor, overrides: Dict[str, Any]):
    """安全地应用常用的图像处理覆盖项（当前仅支持 size: {height, width}）。"""
    ip = processor.image_processor
    if not overrides:
        return
    if "size" in overrides and isinstance(overrides["size"], dict):
        size = overrides["size"]
        if {"height", "width"}.issubset(size.keys()):
            ip.size = {"height": int(size["height"]), "width": int(size["width"]) }


def dump_capabilities(output_dir: str, model: VisionEncoderDecoderModel, processor: DonutProcessor):
    """导出当前模型/处理器的能力概览，便于调参与排错。"""
    # 确保输出目录存在
    ensure_dir(output_dir)
    cap = {}
    # 生成配置
    try:
        cap["generation_config"] = model.generation_config.to_dict()
    except Exception as e:
        cap["generation_config_error"] = str(e)
    # generate 方法签名（查看可用参数）
    try:
        sig = str(inspect.signature(model.generate))
        cap["model_generate_signature"] = sig
    except Exception as e:
        cap["model_generate_signature_error"] = str(e)
    # 分词器新增词（常包含任务 token，如 <s_xxx>）
    try:
        added = list(processor.tokenizer.get_added_vocab().keys())
        cap["tokenizer_added_tokens"] = sorted(added)
    except Exception as e:
        cap["tokenizer_added_tokens_error"] = str(e)
    # 图像处理器配置
    try:
        cap["image_processor_config"] = getattr(processor.image_processor, "config", {})
        # 某些字段不可序列化，降级为常见属性字典
        if not isinstance(cap["image_processor_config"], dict):
            cap["image_processor_config"] = {
                "size": getattr(processor.image_processor, "size", None),
                "do_resize": getattr(processor.image_processor, "do_resize", None),
                "resample": getattr(processor.image_processor, "resample", None),
            }
    except Exception as e:
        cap["image_processor_config_error"] = str(e)

    save_json(os.path.join(output_dir, "capabilities.json"), cap)


def extract_json_from_text(text: str) -> Optional[Dict[str, Any]]:
    """从任意文本中尽量抽取第一个 JSON 对象。失败返回 None。"""
    if not text:
        return None
    try:
        # 直接 parse
        return json.loads(text)
    except Exception:
        pass
    # 寻找最外层花括号
    try:
        start = text.find("{")
        end = text.rfind("}")
        if start != -1 and end != -1 and end > start:
            snippet = text[start:end+1]
            # 去掉可能的多余尾随标点/控制字符
            snippet = re.sub(r"[^ -~\t]", "", snippet)
            return json.loads(snippet)
    except Exception:
        return None
    return None


# ---------------------------
# 核心：对单张图片按某个预设运行一次
# ---------------------------
@torch.inference_mode()
def run_once(
    model: VisionEncoderDecoderModel,
    processor: DonutProcessor,
    device: torch.device,
    image_path: str,
    preset_name: str,
    preset_cfg: Dict[str, Any],
) -> RunResult:
    t0 = time.time()
    error = None
    output_text = None
    output_json = None
    num_gen_tokens: Optional[int] = None

    # 读取图片并转为 RGB
    img = Image.open(image_path).convert("RGB")

    # 临时应用图像处理覆盖参数
    original_size = dict(getattr(processor.image_processor, "size", {}))
    image_processor_apply_overrides(processor, preset_cfg.get("iproc", {}))

    try:
        task_prompt = str(preset_cfg.get("task_prompt", ""))

        inputs = processor(images=img, text=task_prompt, return_tensors="pt")
        inputs = {k: v.to(device) for k, v in inputs.items()}

        gen_kwargs = dict(preset_cfg.get("gen", {}))
        # 确保 pad/eos token 设置妥当（从 processor 注入）
        if model.config.pad_token_id is None and hasattr(processor.tokenizer, "pad_token_id"):
            model.config.pad_token_id = processor.tokenizer.pad_token_id
        if model.config.eos_token_id is None and hasattr(processor.tokenizer, "eos_token_id"):
            model.config.eos_token_id = processor.tokenizer.eos_token_id

        # 生成
        out = model.generate(**inputs, **gen_kwargs)
        # 记录生成 token 数（若可用）
        if hasattr(out, "sequences"):
            seq = out.sequences
        else:
            seq = out
        num_gen_tokens = int(seq.shape[-1]) if hasattr(seq, "shape") else None

        # 解码文本；若可解析为结构化 JSON，则同时给出
        decoded = processor.batch_decode(seq, skip_special_tokens=False)[0]
        output_text = decoded
        try:
            output_json = processor.token2json(decoded)
        except Exception:
            output_json = None

    except Exception as e:
        error = f"{type(e).__name__}: {e}"
    finally:
        # 恢复图像处理器的原始尺寸设置
        if original_size:
            processor.image_processor.size = original_size

    dt = time.time() - t0
    return RunResult(
        preset=preset_name,
        prompt=task_prompt,
        image_processor_overrides=preset_cfg.get("iproc", {}),
        generation_kwargs=preset_cfg.get("gen", {}),
        output_text=output_text,
        output_json=output_json,
        runtime_sec=dt,
        num_generated_tokens=num_gen_tokens,
        error=error,
    )


def pick_presets_by_probe(probe: Optional[Dict[str, Any]]) -> List[str]:
    """根据探针 JSON 选择后续预设。"""
    p = probe or {}
    dom = str(p.get("dominant", "mixed")).lower()
    size = str(p.get("table_size", "none")).lower()
    try:
        conf = float(p.get("confidence", 0.0))
    except Exception:
        conf = 0.0

    # 高置信度，直达专项
    if conf >= 0.7:
        if dom == "equation":
            return ["eq_compact"] if "eq_compact" in PRESETS else ["formula_friendly"]
        if dom == "table" and size == "small":
            return ["table_strict_md"] if "table_strict_md" in PRESETS else ["table_markdown"]
        if dom == "table" and size == "large":
            return ["wide_table_md"] if "wide_table_md" in PRESETS else ["long_page_strict"]
        if dom in ("figure", "mixed"):
            return ["figure_bullets", "page_summary"] if "figure_bullets" in PRESETS else ["page_summary"]
        if dom == "text":
            return ["balanced_beam"]

    # 兜底：通用 preset
    return ["universal_doc"]


# ---------------------------
# 主流程（批量遍历图片并聚合结果）
# ---------------------------

def main():
    parser = argparse.ArgumentParser(description="对一个图片文件夹批量测试 Donut（支持自动路由）")
    parser.add_argument("--input_dir", default=DEFAULT_INPUT_DIR, help="样本图片目录")
    parser.add_argument("--output_dir", default=DEFAULT_OUTPUT_DIR, help="识别结果保存目录（按图片名生成 JSON）")
    parser.add_argument("--model_id", default=DEFAULT_MODEL_ID, help="HF 模型 ID 或本地 checkpoint 路径，如 naver-clova-ix/donut-base-finetuned-synthdog")
    parser.add_argument("--device", default=None, choices=[None, "cuda", "mps", "cpu"], help="强制使用的设备（默认自动选择）")
    parser.add_argument("--fp16", action="store_true", help="在 CUDA 上启用 FP16（若未指定，以脚本默认为准）")
    parser.add_argument("--no-fp16", dest="fp16", action="store_false", help="禁用 FP16")
    parser.set_defaults(fp16=DEFAULT_USE_FP16)
    parser.add_argument("--presets", nargs="*", default=list(PRESETS.keys()), help="要运行的预设名（留空=全部；自动路由时忽略）")
    parser.add_argument("--auto_route", action="store_true", help="启用自动路由：先跑 router_probe，再按结果选择后续预设")
    parser.add_argument("--save_capabilities", action="store_true", help="导出模型/处理器能力概览到 capabilities.json")
    parser.add_argument("--limit", type=int, default=None, help="最多只处理前 N 张图片")

    args = parser.parse_args()

    input_dir = args.input_dir
    output_dir = args.output_dir
    ensure_dir(output_dir)

    # 设备选择逻辑
    if args.device:
        device_str = args.device
    else:
        if torch.cuda.is_available():
            device_str = "cuda"
        elif torch.backends.mps.is_available():
            device_str = "mps"
        else:
            device_str = "cpu"
    device = torch.device(device_str)

    # 加载模型与处理器
    torch.set_grad_enabled(False)
    dtype = torch.float16 if (device_str == "cuda" and args.fp16) else torch.float32
    print(f"正在加载模型 {args.model_id} 到 {device_str} (dtype={dtype}) ...")
    processor = DonutProcessor.from_pretrained(args.model_id)
    model = VisionEncoderDecoderModel.from_pretrained(args.model_id, torch_dtype=dtype)
    model.to(device)
    model.eval()

    # 可选：导出能力概览
    if args.save_capabilities:
        dump_capabilities(output_dir, model, processor)
        print(f"已保存能力概览: {os.path.join(output_dir, 'capabilities.json')}")

    # 列出图片
    images = list_images(input_dir)
    if args.limit is not None:
        images = images[: args.limit]
    if not images:
        print(f"未在该目录找到图片: {input_dir}")
        sys.exit(1)

    # 如果不走自动路由，准备固定的预设集合
    chosen_presets = []
    if not args.auto_route:
        for name in args.presets:
            if name not in PRESETS:
                print(f"[警告] 未找到预设 '{name}'，已跳过。")
                continue
            chosen_presets.append((name, PRESETS[name]))
        if not chosen_presets:
            print("未选择到有效的预设。")
            sys.exit(1)

    # 逐图处理并聚合写入 JSON
    for idx, img_path in enumerate(images, 1):
        rel = os.path.relpath(img_path, input_dir)
        stem = os.path.splitext(os.path.basename(img_path))[0]
        out_file = os.path.join(output_dir, f"{stem}.json")
        
        # 显示进度信息
        progress_percent = (idx / len(images)) * 100
        print(f"\n🔄 进度: [{idx}/{len(images)}] - {progress_percent:.1f}%")
        print(f"==> {rel} : {('自动路由' if args.auto_route else '运行 ' + str(len(chosen_presets)) + ' 个预设')}")

        # 若该图片已有聚合结果则读取（以便追加）
        if os.path.exists(out_file):
            try:
                aggregate = load_json(out_file)
            except Exception:
                aggregate = {}
        else:
            aggregate = {}

        # 初始化/规范化聚合结构
        if not isinstance(aggregate, dict):
            aggregate = {}
        aggregate.setdefault("image", img_path)
        aggregate.setdefault("model_id", args.model_id)
        aggregate.setdefault("created_at", time.strftime("%Y-%m-%d %H:%M:%S"))
        aggregate.setdefault("results", [])

        if args.auto_route:
            # 1) 跑探针
            probe_res = run_once(model, processor, device, img_path, "router_probe", PRESETS["router_probe"]) 
            probe_parsed = extract_json_from_text(probe_res.output_text or "") or probe_res.output_json

            # 记录探针结果
            rec_probe = asdict(probe_res)
            rec_probe["parsed_json"] = probe_parsed
            rec_probe["timestamp"] = time.strftime("%Y-%m-%d %H:%M:%S")
            aggregate["results"].append(rec_probe)

            # 2) 由探针选择后续预设
            to_run = pick_presets_by_probe(probe_parsed)
            # 3) 跑后续预设
            for preset_idx, name in enumerate(to_run, 1):
                if name not in PRESETS:
                    print(f"[警告] 预设 '{name}' 未定义，跳过。")
                    continue
                
                # 显示子进度
                sub_progress = (preset_idx / len(to_run)) * 100
                print(f"  - 预设: {name} [{preset_idx}/{len(to_run)}] - {sub_progress:.1f}%")
                
                res = run_once(model, processor, device, img_path, name, PRESETS[name])
                record = asdict(res)
                record["timestamp"] = time.strftime("%Y-%m-%d %H:%M:%S")
                aggregate["results"].append(record)
                
                # 显示结果摘要
                if res.error:
                    print(f"    ❌ 错误: {res.error}")
                else:
                    text_preview = res.output_text[:50] + "..." if res.output_text and len(res.output_text) > 50 else res.output_text
                    print(f"    ✅ 用时: {res.runtime_sec:.2f}秒, 输出长度: {len(res.output_text or '') if res.output_text else 0}字符")

        else:
            # 固定预设流程
            for preset_idx, (preset_name, preset_cfg) in enumerate(chosen_presets, 1):
                # 显示子进度
                sub_progress = (preset_idx / len(chosen_presets)) * 100
                print(f"  - 预设: {preset_name} [{preset_idx}/{len(chosen_presets)}] - {sub_progress:.1f}%")
                
                res = run_once(model, processor, device, img_path, preset_name, preset_cfg)
                record = asdict(res)
                record["timestamp"] = time.strftime("%Y-%m-%d %H:%M:%S")
                aggregate["results"].append(record)
                
                # 显示结果摘要
                if res.error:
                    print(f"    ❌ 错误: {res.error}")
                else:
                    text_preview = res.output_text[:50] + "..." if res.output_text and len(res.output_text) > 50 else res.output_text
                    print(f"    ✅ 用时: {res.runtime_sec:.2f}秒, 输出长度: {len(res.output_text or '') if res.output_text else 0}字符")

        # 记录已运行的预设名（追加式）
        already = set(aggregate.get("presets_run", []))
        if args.auto_route:
            already.update(["router_probe"])  # 探针
            # 把本次真正跑的预设名也写进去
            # 从最新追加的记录中抓 preset 字段
            for r in aggregate["results"][-3:]:  # 简化：最近几条通常就是本次
                if isinstance(r, dict) and r.get("preset"):
                    already.add(r["preset"]) 
        else:
            already.update(name for name, _ in (chosen_presets or []))
        aggregate["presets_run"] = sorted(list(already))

        save_json(out_file, aggregate)
        print(f"已保存: {out_file}")

    print("\n全部完成。")


if __name__ == "__main__":
    main()
