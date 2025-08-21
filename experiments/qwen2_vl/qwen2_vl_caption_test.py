#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Test Qwen2-VL-7B-Instruct on GPU (4090) for complex figure/chart captioning.

- Loads model with bf16 on CUDA if available (fallback to fp16/cpu)
- Iterates images in input_dir
- Generates a descriptive caption per image
- Saves per-image JSON to output_dir
"""
from __future__ import annotations
import os
import json
import time
import argparse
from pathlib import Path
from typing import Dict, Any, List

import torch
from PIL import Image
from transformers import AutoProcessor, Qwen2VLForConditionalGeneration


def list_images(folder: str) -> List[str]:
    exts = {".png", ".jpg", ".jpeg", ".webp", ".bmp", ".tif", ".tiff"}
    files: List[str] = []
    for root, _, names in os.walk(folder):
        for n in sorted(names):
            if os.path.splitext(n.lower())[1] in exts:
                files.append(os.path.join(root, n))
    return files


def ensure_dir(p: str) -> None:
    os.makedirs(p, exist_ok=True)


def main():
    parser = argparse.ArgumentParser(
        description="Qwen2-VL caption test on charts/figures"
    )
    parser.add_argument(
        "--model_id",
        default="Qwen/Qwen2-VL-7B-Instruct",
        help="Hugging Face model id",
    )
    parser.add_argument(
        "--input_dir",
        default="data/pdf_ocr_samples",
        help="Directory of input images",
    )
    parser.add_argument(
        "--output_dir",
        default="output/qwen2_vl",
        help="Directory to save JSON outputs",
    )
    parser.add_argument(
        "--limit", type=int, default=4, help="Process at most N images"
    )
    parser.add_argument(
        "--max_new_tokens", type=int, default=512, help="Generation length"
    )
    args = parser.parse_args()

    ensure_dir(args.output_dir)

    # Device and dtype
    if torch.cuda.is_available():
        device = torch.device("cuda")
        # Prefer bf16 if available on 4090; otherwise fp16
        bf16_ok = torch.cuda.is_bf16_supported()
        dtype = torch.bfloat16 if bf16_ok else torch.float16
    else:
        device = torch.device("cpu")
        dtype = torch.float32

    print(f"Loading {args.model_id} on {device} (dtype={dtype}) ...")
    processor = AutoProcessor.from_pretrained(args.model_id, trust_remote_code=True)
    model = Qwen2VLForConditionalGeneration.from_pretrained(
        args.model_id,
        torch_dtype=dtype,
        device_map="auto",
        trust_remote_code=True,
    )
    model.eval()

    images = list_images(args.input_dir)
    if args.limit is not None:
        images = images[: args.limit]
    if not images:
        print(f"No images found in {args.input_dir}")
        return

    prompt = (
        "You are an expert science figure and chart captioner. "
        "Carefully read the image and write a detailed, accurate caption "
        "that describes: (1) what the chart/figure shows, (2) key entities, "
        "(3) notable labels/values, (4) trends/relationships. Avoid hallucination."
    )

    for idx, img_path in enumerate(images, 1):
        t0 = time.time()
        img = Image.open(img_path).convert("RGB")

        messages = [
            {
                "role": "system",
                "content": prompt,
            },
            {
                "role": "user",
                "content": [
                    {"type": "text", "text": "Describe the figure precisely."},
                    {"type": "image", "image": img},
                ],
            },
        ]
        
        # Qwen2-VL chat template
        text = processor.apply_chat_template(messages, tokenize=False, add_generation_prompt=True)
        inputs = processor(text=[text], images=[img], return_tensors="pt").to(device)

        gen_kwargs = {
            "max_new_tokens": args.max_new_tokens,
            "do_sample": False,
            "num_beams": 3,
            "repetition_penalty": 1.05,
            "no_repeat_ngram_size": 3,
        }

        with torch.inference_mode():
            out = model.generate(**inputs, **gen_kwargs)
            if hasattr(out, "sequences"):
                seq = out.sequences
            else:
                seq = out
            text_out = processor.batch_decode(seq, skip_special_tokens=True)[0]

        dt = time.time() - t0

        rec = {
            "image": img_path,
            "model_id": args.model_id,
            "prompt": prompt,
            "generation_kwargs": gen_kwargs,
            "output_text": text_out,
            "runtime_sec": dt,
        }

        stem = os.path.splitext(os.path.basename(img_path))[0]
        out_file = os.path.join(args.output_dir, f"{stem}.json")
        with open(out_file, "w", encoding="utf-8") as f:
            json.dump(rec, f, ensure_ascii=False, indent=2)

        print(f"[{idx}/{len(images)}] Saved: {out_file} ({dt:.2f}s)")


if __name__ == "__main__":
    main()
