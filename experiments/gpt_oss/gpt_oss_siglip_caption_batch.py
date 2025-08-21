#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Batch captioning for complex charts/diagrams using gpt-oss-20b.

- Visual priors from SigLIP/CLIP via zero-shot concept matching
- Optional OCR (paddleocr) for text-dense figures
- Harmony chat messages for gpt-oss-20b generation
- Aggregated JSON per image, aligned with existing outputs

Notes
-----
This script avoids any vision-language model (e.g., Qwen2-VL). It relies on
vision encoders for concept tags and passes structured cues to the LLM.
"""
from __future__ import annotations

import os
import json
import argparse
from typing import List, Dict, Any, Tuple

import torch
from PIL import Image

from transformers import (
    AutoProcessor,
    AutoModel,
    CLIPModel,
    CLIPProcessor,
    AutoTokenizer,
    AutoModelForCausalLM,
    pipeline,
)


# ----------------------------
# Utility helpers
# ----------------------------

def list_images(folder: str) -> List[str]:
    r"""List supported image files recursively.

    Args:
        folder (str): Root directory to search for images.

    Returns:
        List[str]: Sorted file paths.
    """
    exts = {".png", ".jpg", ".jpeg", ".webp", ".bmp", ".tif", ".tiff"}
    files: List[str] = []
    for root, _, names in os.walk(folder):
        for n in sorted(names):
            if os.path.splitext(n.lower())[1] in exts:
                files.append(os.path.join(root, n))
    return files


def ensure_dir(p: str) -> None:
    r"""Create directory if not exists.

    Args:
        p (str): Directory path.
    """
    os.makedirs(p, exist_ok=True)


# ----------------------------
# Concept labels for zero-shot
# ----------------------------

DEFAULT_LABELS: List[str] = [
    # Diagram types
    "flowchart", "process diagram", "block diagram", "network graph",
    "org chart", "mind map", "timeline", "swimlane diagram",
    "gantt chart", "tree diagram", "state machine", "er diagram",
    "uml class diagram", "uml sequence diagram", "dependency graph",
    "pipeline diagram", "architecture diagram", "logic gate diagram",
    "circuit diagram", "wiring diagram", "sankey diagram",
    "venn diagram", "concept map", "infographic",
    # Structural cues
    "nodes and edges", "arrows and direction", "hierarchy",
    "decision diamond", "start end terminator", "loop",
    "conditional branch", "legend", "color mapping", "module",
    "service", "database", "api", "queue", "cache",
    # Chart-ish but non-standard
    "iconography", "illustration with text", "mixed media",
]


def _l2_normalize(x: torch.Tensor, dim: int = -1, eps: float = 1e-12) -> torch.Tensor:
    r"""L2 normalize tensor along a dimension.

    Args:
        x (torch.Tensor): Input tensor.
        dim (int): Dimension to normalize.
        eps (float): Numerical stability epsilon.

    Returns:
        torch.Tensor: Normalized tensor.
    """
    return x / (x.norm(dim=dim, keepdim=True) + eps)


def load_vision_encoder(
    model_id: str,
    device: torch.device,
) -> Tuple[Any, Any, bool]:
    r"""Load a vision encoder (SigLIP preferred, fallback to CLIP).

    Args:
        model_id (str): HF model id for vision encoder.
        device (torch.device): Device for inference.

    Returns:
        Tuple[Any, Any, bool]: (processor, model, is_clip)
            is_clip indicates CLIPModel/CLIPProcessor path.
    """
    try:
        processor = AutoProcessor.from_pretrained(model_id)
        model = AutoModel.from_pretrained(model_id).to(device)
        return processor, model, False
    except Exception:
        # Fallback to CLIP if SigLIP is unavailable
        clip_id = "openai/clip-vit-large-patch14"
        proc = CLIPProcessor.from_pretrained(clip_id)
        mod = CLIPModel.from_pretrained(clip_id).to(device)
        return proc, mod, True


def rank_concepts_for_image(
    image: Image.Image,
    processor: Any,
    model: Any,
    device: torch.device,
    labels: List[str],
    top_k: int = 10,
) -> List[Tuple[str, float]]:
    r"""Rank concept labels for an image using vision-text similarity.

    Args:
        image (Image.Image): Input image in RGB.
        processor (Any): Vision processor (SigLIP/CLIP).
        model (Any): Vision model (SigLIP/CLIP).
        device (torch.device): Model device.
        labels (List[str]): Candidate concept labels.
        top_k (int): Number of labels to return.

    Returns:
        List[Tuple[str, float]]: Top-k (label, score) pairs.
    """
    model.eval()
    with torch.inference_mode():
        v = processor(images=image, return_tensors="pt")
        v = {k: t.to(device) for k, t in v.items()}

        # Try SigLIP/CLIP pathways
        try:
            img_feat = model.get_image_features(**v)
        except Exception:
            out = model(**v)
            img_feat = getattr(out, "image_embeds", None)
            if img_feat is None:
                # Fallback: pool last hidden state
                last = getattr(out, "last_hidden_state", None)
                if last is None:
                    raise RuntimeError("Vision model lacks image features")
                img_feat = last.mean(dim=1)

        t = processor(text=labels, return_tensors="pt", padding=True)
        t = {k: tt.to(device) for k, tt in t.items()}
        try:
            txt_feat = model.get_text_features(**t)
        except Exception:
            out_t = model(**t)
            txt_feat = getattr(out_t, "text_embeds", None)
            if txt_feat is None:
                last_t = getattr(out_t, "last_hidden_state", None)
                if last_t is None:
                    raise RuntimeError("Vision model lacks text features")
                txt_feat = last_t.mean(dim=1)

        img_feat = _l2_normalize(img_feat.float())
        txt_feat = _l2_normalize(txt_feat.float())

        sim = img_feat @ txt_feat.t()  # [1, L]
        scores = sim.squeeze(0).cpu()

    idx = torch.topk(scores, k=min(top_k, scores.numel())).indices.tolist()
    return [(labels[i], float(scores[i])) for i in idx]


def extract_ocr_text(image_path: str, enable_ocr: bool) -> str:
    r"""Extract OCR text via paddleocr if available and enabled.

    Args:
        image_path (str): Path to input image.
        enable_ocr (bool): Whether to attempt OCR.

    Returns:
        str: Concatenated OCR text or empty string.
    """
    if not enable_ocr:
        return ""
    try:
        from paddleocr import PaddleOCR  # type: ignore
    except Exception:
        return ""

    ocr = PaddleOCR(use_angle_cls=True, lang="en")
    result = ocr.ocr(image_path, cls=True)
    lines: List[str] = []
    for page in result:
        for line in page:
            txt = line[1][0] if line and line[1] else ""
            if txt:
                lines.append(txt)
    return "\n".join(lines)


# ----------------------------
# GPT-OSS prompting presets
# ----------------------------

PRESETS: Dict[str, Dict[str, Any]] = {
    "structure_focus": {
        "prompt": (
            "You analyze complex diagrams. Describe nodes, edges, hierarchy, "
            "and directional flow. Avoid hallucination; only state visible "
            "relations."
        ),
        "gen": {
            "max_new_tokens": 512,
            "do_sample": False,
            "num_beams": 3,
        },
    },
    "flowchart_focus": {
        "prompt": (
            "If the figure is a flowchart, identify start/end, decisions, "
            "branches, and step sequence. Otherwise, still report structure."
        ),
        "gen": {
            "max_new_tokens": 640,
            "do_sample": False,
            "num_beams": 3,
        },
    },
    "infographic_focus": {
        "prompt": (
            "If the figure is an infographic, summarize key sections, icons, "
            "and textual highlights. Preserve factual grounding."
        ),
        "gen": {
            "max_new_tokens": 512,
            "do_sample": True,
            "temperature": 0.6,
            "top_p": 0.9,
        },
    },
    "generic": {
        "prompt": (
            "Provide a precise caption for a complex diagram. Mention the "
            "diagram type, main components, relationships, and purpose."
        ),
        "gen": {
            "max_new_tokens": 448,
            "do_sample": False,
            "num_beams": 2,
        },
    },
}


def build_user_block(
    concept_scores: List[Tuple[str, float]],
    ocr_text: str,
    max_labels: int,
    max_ocr_chars: int,
) -> str:
    r"""Compose a structured user content block from cues.

    Args:
        concept_scores (List[Tuple[str, float]]): Ranked labels.
        ocr_text (str): OCR extracted text.
        max_labels (int): Cap on number of labels.
        max_ocr_chars (int): Cap on OCR text length.

    Returns:
        str: Structured content for the user message.
    """
    labels = concept_scores[:max_labels]
    label_lines = [f"- {lab} (score={score:.3f})" for lab, score in labels]
    ocr_snip = (ocr_text or "").strip()
    if len(ocr_snip) > max_ocr_chars:
        ocr_snip = ocr_snip[: max_ocr_chars] + "..."

    parts: List[str] = []
    parts.append("Visual concept cues (top-k):")
    parts.extend(label_lines if label_lines else ["- (none)"])
    parts.append("")
    parts.append("OCR text (optional):")
    parts.append(ocr_snip if ocr_snip else "(none)")
    parts.append("")
    parts.append(
        "Task: Based on the cues above, write a factual, structured "
        "caption describing the figure: diagram type, main components, "
        "relations (nodes/edges/directions), key text, and overall purpose."
    )
    return "\n".join(parts)


def run_once(
    image_path: str,
    pipe,
    vision_processor: Any,
    vision_model: Any,
    device: torch.device,
    preset_name: str,
    preset_cfg: Dict[str, Any],
    labels: List[str],
    top_k: int,
    enable_ocr: bool,
    max_labels: int,
    max_ocr_chars: int,
) -> Dict[str, Any]:
    r"""Run one caption generation with a specific preset.

    Args:
        image_path (str): Path to the image.
        pipe: Transformers text-generation pipeline for gpt-oss.
        vision_processor (Any): Vision processor.
        vision_model (Any): Vision encoder model.
        device (torch.device): Torch device.
        preset_name (str): Name of the preset.
        preset_cfg (Dict[str, Any]): Preset config.
        labels (List[str]): Concept label bank.
        top_k (int): Top-k labels for ranking.
        enable_ocr (bool): Whether to use OCR.
        max_labels (int): Max labels to include in prompt.
        max_ocr_chars (int): Max OCR chars to include.

    Returns:
        Dict[str, Any]: Result record.
    """
    img = Image.open(image_path).convert("RGB")

    ranked = rank_concepts_for_image(
        img, vision_processor, vision_model, device, labels, top_k
    )
    ocr_text = extract_ocr_text(image_path, enable_ocr)

    sys_prompt = str(preset_cfg.get("prompt", ""))
    user_block = build_user_block(ranked, ocr_text, max_labels, max_ocr_chars)

    messages = [
        {"role": "system", "content": f"{sys_prompt}\nReasoning: high"},
        {"role": "user", "content": user_block},
    ]

    gen_kwargs = dict(preset_cfg.get("gen", {}))
    outputs = pipe(messages, **gen_kwargs)

    # The pipeline returns a list with chat messages; take the last message.
    last = outputs[0].get("generated_text", [])
    if isinstance(last, list) and last:
        final_msg = last[-1]
        if isinstance(final_msg, dict):
            out_text = str(final_msg.get("content", final_msg))
        else:
            out_text = str(final_msg)
    else:
        out_text = json.dumps(outputs[0])

    return {
        "preset": preset_name,
        "prompt": sys_prompt,
        "generation_kwargs": gen_kwargs,
        "output_text": out_text,
        "concept_labels": [lab for lab, _ in ranked[:max_labels]],
    }


def main() -> None:
    r"""CLI entry point for GPT-OSS diagram captioning batch test.

    Command-line arguments include model ids, I/O paths, and knobs for the
    concept ranking and OCR usage.
    """
    parser = argparse.ArgumentParser(
        description="Batch caption test with gpt-oss-20b using SigLIP/CLIP"
    )
    parser.add_argument(
        "--model_id",
        default="openai/gpt-oss-20b",
        help="LLM model id for caption generation",
    )
    parser.add_argument(
        "--vision_model_id",
        default="google/siglip-so400m-patch14-384",
        help="Vision encoder model id (fallback to CLIP if fails)",
    )
    parser.add_argument(
        "--input_dir",
        default="data/pdf_ocr_samples",
        help="Directory of input images",
    )
    parser.add_argument(
        "--output_dir",
        default="output/gpt-oss-20b",
        help="Directory for aggregated JSON outputs",
    )
    parser.add_argument(
        "--limit", type=int, default=None, help="Process at most N images"
    )
    parser.add_argument(
        "--labels_file",
        default=None,
        help="Optional path to a txt file with one label per line",
    )
    parser.add_argument(
        "--top_k", type=int, default=12, help="Top-k concepts to rank"
    )
    parser.add_argument(
        "--use_ocr", action="store_true", help="Enable PaddleOCR if avail"
    )
    parser.add_argument(
        "--max_labels", type=int, default=10, help="Max labels in prompt"
    )
    parser.add_argument(
        "--max_ocr_chars", type=int, default=800, help="Max OCR chars"
    )
    args = parser.parse_args()

    ensure_dir(args.output_dir)

    # Device and dtype
    if torch.cuda.is_available():
        device = torch.device("cuda")
    else:
        device = torch.device("cpu")

    # Load LLM via pipeline (uses harmony chat template under the hood)
    pipe = pipeline(
        "text-generation",
        model=args.model_id,
        torch_dtype="auto",
        device_map="auto",
    )

    # Load vision encoder (SigLIP preferred)
    vision_processor, vision_model, _ = load_vision_encoder(
        args.vision_model_id, device
    )

    # Load labels
    if args.labels_file and os.path.isfile(args.labels_file):
        with open(args.labels_file, "r", encoding="utf-8") as f:
            labels = [ln.strip() for ln in f if ln.strip()]
        if not labels:
            labels = list(DEFAULT_LABELS)
    else:
        labels = list(DEFAULT_LABELS)

    # Images
    images = list_images(args.input_dir)
    if args.limit is not None:
        images = images[: args.limit]
    if not images:
        print(f"No images found in {args.input_dir}")
        return

    # Process images
    for idx, img_path in enumerate(images, 1):
        stem = os.path.splitext(os.path.basename(img_path))[0]
        out_file = os.path.join(args.output_dir, f"{stem}.json")

        aggregate: Dict[str, Any] = {
            "image": img_path,
            "model_id": args.model_id,
            "results": [],
            "presets_run": [],
        }

        print(
            f"[{idx}/{len(images)}] => "
            f"{os.path.relpath(img_path, args.input_dir)} | "
            f"{len(PRESETS)} presets"
        )

        for p_idx, (pname, pcfg) in enumerate(PRESETS.items(), 1):
            print(f"  - preset: {pname} [{p_idx}/{len(PRESETS)}]")
            try:
                rec = run_once(
                    img_path,
                    pipe,
                    vision_processor,
                    vision_model,
                    device,
                    pname,
                    pcfg,
                    labels,
                    args.top_k,
                    args.use_ocr,
                    args.max_labels,
                    args.max_ocr_chars,
                )
                aggregate["results"].append(rec)
                aggregate["presets_run"].append(pname)
            except Exception as e:
                aggregate["results"].append(
                    {
                        "preset": pname,
                        "prompt": pcfg.get("prompt", ""),
                        "generation_kwargs": pcfg.get("gen", {}),
                        "output_text": None,
                        "error": f"{type(e).__name__}: {e}",
                    }
                )
                aggregate["presets_run"].append(pname)

        with open(out_file, "w", encoding="utf-8") as f:
            json.dump(aggregate, f, ensure_ascii=False, indent=2)
        print(f"    saved: {out_file}")


if __name__ == "__main__":
    main()


