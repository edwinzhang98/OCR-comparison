#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Batch test Qwen/Qwen2-VL-7B-Instruct on OCR samples with multiple presets.

- Reads images from an input directory
- Runs several captioning presets per image
- Aggregates all preset outputs into a single JSON per image
- Saves results to an output directory (no timing fields)

Folder layout (as requested):
- Script: experiments/qwen2_vl/qwen2_vl_batch_test.py
- Outputs: Output/Qwen2-VL-7B-Instruct/<image_stem>.json
"""
from __future__ import annotations
import os
import json
import argparse
from typing import Dict, Any, List, Optional

import torch
from PIL import Image
from transformers import AutoProcessor, Qwen2VLForConditionalGeneration


def list_images(folder: str) -> List[str]:
    r"""List all supported image files in a directory tree.

    Args:
        folder (str): Root directory to search for images.

    Returns:
        List[str]: Sorted list of image file paths.
    """
    exts = {".png", ".jpg", ".jpeg", ".webp", ".bmp", ".tif", ".tiff"}
    files: List[str] = []
    for root, _, names in os.walk(folder):
        for n in sorted(names):
            if os.path.splitext(n.lower())[1] in exts:
                files.append(os.path.join(root, n))
    return files


def ensure_dir(p: str) -> None:
    r"""Create a directory if it does not exist.

    Args:
        p (str): Directory path to create.
    """
    os.makedirs(p, exist_ok=True)


# Preset definitions: prompt + generation kwargs
PRESETS: Dict[str, Dict[str, Any]] = {
    "concise_default": {
        "prompt": (
            "You are an expert science figure and chart captioner. "
            "Write a concise, accurate caption describing what the "
            "figure shows, axes, units, and the main trend."
        ),
        "gen": {
            "max_new_tokens": 384,
            "do_sample": False,
            "num_beams": 3,
            "repetition_penalty": 1.05,
            "no_repeat_ngram_size": 3,
        },
    },
    "long_detailed": {
        "prompt": (
            "Analyze the figure carefully and write a detailed caption. "
            "Include key entities, labels/values, and trends. Avoid "
            "hallucination; describe only what is visible."
        ),
        "gen": {
            "max_new_tokens": 768,
            "do_sample": False,
            "num_beams": 3,
            "repetition_penalty": 1.07,
            "no_repeat_ngram_size": 3,
        },
    },
    "strict_beam": {
        "prompt": (
            "Provide a precise caption focusing on axes, units, and "
            "relationships. Be factual and terse."
        ),
        "gen": {
            "max_new_tokens": 512,
            "do_sample": False,
            "num_beams": 5,
            "repetition_penalty": 1.1,
            "no_repeat_ngram_size": 4,
        },
    },
    "creative_sample": {
        "prompt": (
            "Describe the chart with clarity. Mention axes, units, "
            "labels, and any visible trends."
        ),
        "gen": {
            "max_new_tokens": 512,
            "do_sample": True,
            "temperature": 0.6,
            "top_p": 0.9,
            "num_beams": 1,
            "repetition_penalty": 1.02,
            "no_repeat_ngram_size": 3,
        },
    },
}


def run_once(
    model: Qwen2VLForConditionalGeneration,
    processor: AutoProcessor,
    device: torch.device,
    image_path: str,
    preset_name: str,
    preset_cfg: Dict[str, Any],
) -> Dict[str, Any]:
    r"""Run caption generation once for a single image and preset.

    Args:
        model (Qwen2VLForConditionalGeneration): Loaded Qwen2-VL model.
        processor (AutoProcessor): Paired processor/tokenizer.
        device (torch.device): Target device for tensors.
        image_path (str): Path to the input image.
        preset_name (str): Name of preset to run.
        preset_cfg (Dict[str, Any]): Preset configuration.

    Returns:
        Dict[str, Any]: Minimal record with preset, prompt, gen kwargs,
            and output_text for aggregation.
    """
    img = Image.open(image_path).convert("RGB")

    prompt = str(preset_cfg.get("prompt", ""))
    messages = [
        {"role": "system", "content": prompt},
        {
            "role": "user",
            "content": [
                {"type": "text", "text": "Describe the figure precisely."},
                {"type": "image", "image": img},
            ],
        },
    ]

    text = processor.apply_chat_template(
        messages, tokenize=False, add_generation_prompt=True
    )
    inputs = processor(text=[text], images=[img], return_tensors="pt").to(device)

    gen_kwargs = dict(preset_cfg.get("gen", {}))

    with torch.inference_mode():
        out = model.generate(**inputs, **gen_kwargs)
        seq = out.sequences if hasattr(out, "sequences") else out
        # Decode only newly generated tokens (exclude prompt/input ids)
        inp_len = int(inputs["input_ids"].shape[-1])
        gen_ids = seq[:, inp_len:]
        output_text = processor.batch_decode(gen_ids, skip_special_tokens=True)[0]

    return {
        "preset": preset_name,
        "prompt": prompt,
        "generation_kwargs": gen_kwargs,
        "output_text": output_text,
    }


def main():
    r"""Entry point for batch testing on OCR samples with presets.

    Command-line args:
        --model_id: HF model id (default Qwen/Qwen2-VL-7B-Instruct)
        --input_dir: Source images directory
        --output_dir: Destination directory (Output/Qwen2-VL-7B-Instruct)
        --limit: Optional limit on number of images
        --presets: Optional list of preset names to run
    """
    parser = argparse.ArgumentParser(
        description="Batch caption test with Qwen2-VL presets"
    )
    parser.add_argument(
        "--model_id",
        default="Qwen/Qwen2-VL-7B-Instruct",
        help="HF model id or local path",
    )
    parser.add_argument(
        "--input_dir",
        default="data/pdf_ocr_samples",
        help="Directory of input images",
    )
    parser.add_argument(
        "--output_dir",
        default="output/Qwen2-VL-7B-Instruct",
        help="Directory to save aggregated JSON outputs",
    )
    parser.add_argument(
        "--limit", type=int, default=None, help="Process at most N images"
    )
    parser.add_argument(
        "--presets", nargs="*", default=list(PRESETS.keys()),
        help="Preset names to run (default: all)",
    )
    args = parser.parse_args()

    ensure_dir(args.output_dir)

    # Device and dtype selection
    if torch.cuda.is_available():
        device = torch.device("cuda")
        dtype = torch.bfloat16 if torch.cuda.is_bf16_supported() else torch.float16
    else:
        device = torch.device("cpu")
        dtype = torch.float32

    print(f"Loading {args.model_id} on {device} (dtype={dtype}) ...")
    processor = AutoProcessor.from_pretrained(
        args.model_id, trust_remote_code=True
    )
    model = Qwen2VLForConditionalGeneration.from_pretrained(
        args.model_id,
        torch_dtype=dtype,
        device_map="auto",
        trust_remote_code=True,
    )
    model.eval()

    # Resolve presets to run
    chosen: List[Dict[str, Any]] = []
    for name in args.presets:
        if name not in PRESETS:
            print(f"[warn] Unknown preset: {name}, skipped")
            continue
        chosen.append((name, PRESETS[name]))
    if not chosen:
        print("No valid presets selected.")
        return

    # List images
    images = list_images(args.input_dir)
    if args.limit is not None:
        images = images[: args.limit]
    if not images:
        print(f"No images found in {args.input_dir}")
        return

    # Process images and aggregate results per image
    for idx, img_path in enumerate(images, 1):
        stem = os.path.splitext(os.path.basename(img_path))[0]
        out_file = os.path.join(args.output_dir, f"{stem}.json")

        # Initialize aggregation record
        aggregate: Dict[str, Any] = {
            "image": img_path,
            "model_id": args.model_id,
            "results": [],
            "presets_run": [],
        }

        print(f"[{idx}/{len(images)}] => {os.path.relpath(img_path, args.input_dir)}"
              f" | {len(chosen)} presets")

        for p_idx, (pname, pcfg) in enumerate(chosen, 1):
            print(f"  - preset: {pname} [{p_idx}/{len(chosen)}]")
            try:
                rec = run_once(model, processor, device, img_path, pname, pcfg)
                aggregate["results"].append(rec)
                aggregate["presets_run"].append(pname)
            except Exception as e:
                aggregate["results"].append({
                    "preset": pname,
                    "prompt": pcfg.get("prompt", ""),
                    "generation_kwargs": pcfg.get("gen", {}),
                    "output_text": None,
                    "error": f"{type(e).__name__}: {e}",
                })
                aggregate["presets_run"].append(pname)

        # Save aggregated JSON
        with open(out_file, "w", encoding="utf-8") as f:
            json.dump(aggregate, f, ensure_ascii=False, indent=2)
        print(f"    saved: {out_file}")


if __name__ == "__main__":
    main()
