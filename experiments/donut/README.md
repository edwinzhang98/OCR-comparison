# Donut OCR 实验

本目录包含 Donut 模型的 OCR 实验代码。

## donut_batch_test_auto.py

`donut_batch_test_auto.py` 是主要的实验脚本，支持批量处理和自动路由功能。

## 一句话说明

- **自动路由**：每张图片先跑一个极短"探针"(`router_probe`) 产出 JSON 标签（是否表/公式/图/文本/混合、表格大小、置信度），再据此自动选择更合适的预设（如 `table_strict_md`、`eq_compact` 等）。
- **通用 preset**：`universal_doc` 一把梭——能结构化就结构化（表→Markdown、式→LaTeX），否则退化为**简短 caption + 关键正文**，统一以 JSON 输出。

> 不需要你手动切换模式；同一图片的所有结果仍聚合写入同一个 `*.json` 文件（含探针输出与路由后各模式的结果）。

## 安装（使用 uv）

```bash
# 1) 创建并激活虚拟环境
uv venv donut
# macOS/Linux
source donut/bin/activate
# Windows PowerShell
# donut\Scripts\Activate.ps1

# 2) 安装依赖
uv pip install -r requirements_donut.txt
```

## 快速开始

### 自动路由（推荐）

```bash
python experiments/donut/donut_batch_test_auto.py --auto_route \
  --input_dir data/samples/ocr_test \
  --output_dir output/donut \
  --no-fp16
```

脚本流程：`router_probe → (pick presets) → run chosen presets → append results`。

### 固定预设（与旧流程一致）

```bash
python experiments/donut/donut_batch_test_auto.py --presets balanced_beam formula_friendly --no-fp16
```

## 预设清单

- `router_probe`：极短 JSON 探针（输出 `dominant`、`table_size`、`confidence`）。
- `universal_doc`：通用一把梭（严格 JSON；表/式优先结构化）。
- `eq_compact`：短/单行公式 → LaTeX，少废话。
- `table_strict_md`：小/中表格 → Markdown，强调不改动数字/标点。
- `wide_table_md`：宽/长表 → 更长输出、不早停；必要时拆分为多张表。
- `figure_bullets`：图示/示意图 → 最多 5 条要点。
- 其它基础预设：`fast_draft`、`balanced_beam`、`long_page_strict`、`formula_friendly`、`table_markdown`、`page_summary`。

## 路由决策（简化版）

探针输出示例：

```json
{"is_table": true, "is_equation": false, "is_figure": false,
 "is_text": false, "dominant": "table", "table_size": "small",
 "confidence": 0.86}
```

选择规则（脚本内置）：

- 置信度 `>= 0.7`：
  - `equation` → `eq_compact`（或 `formula_friendly`）
  - `table/small` → `table_strict_md`（或 `table_markdown`）
  - `table/large` → `wide_table_md`（或 `long_page_strict`）
  - `figure` 或 `mixed` → `figure_bullets` + `page_summary`
  - `text` → `balanced_beam`
- 其他情况：回退 `universal_doc`。

## 输出结构（示例）

每张图片对应一个 `output/donut/<n>.json`：

```json
{
  "image": "data/samples/ocr_test/page_001.jpg",
  "model_id": "naver-clova-ix/donut-base",
  "created_at": "2025-08-17 20:30:00",
  "presets_run": ["router_probe", "table_strict_md", "page_summary"],
  "results": [
    {
      "preset": "router_probe",
      "output_text": "{...}",
      "parsed_json": {"dominant": "table", "table_size": "small", "confidence": 0.83},
      "runtime_sec": 0.12,
      "error": null
    },
    {
      "preset": "table_strict_md",
      "output_text": "| Model | #Param |...",
      "output_json": {"text": "..."},
      "runtime_sec": 0.98
    }
  ]
}
```

## 小贴士

- **超宽表**若仍被截断：把 `wide_table_md.gen.max_new_tokens` 提到 1600–2000（视显存而定）。
- **重复**：调高 `repetition_penalty` 到 1.1–1.2，并设 `no_repeat_ngram_size`≥3。
- **探针不稳定**：可以连跑两次 `router_probe`（不同措辞）做一致性投票；不一致时回退 `universal_doc`。
- **自我校验**（可选）：如果识别结果长度接近 `max_new_tokens`，自动再补跑一次 `long_page_strict` 并追加到同一 JSON。