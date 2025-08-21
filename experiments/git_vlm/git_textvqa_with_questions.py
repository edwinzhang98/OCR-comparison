#!/usr/bin/env python3
r"""TextVQA batch test with a fixed question set per image.

For each image, asks several templated questions that suit charts/figures.
Outputs one JSON per image with per-question results.
"""

import json
import time
import argparse
from pathlib import Path
from typing import Any, Dict, List

import torch
from PIL import Image
from transformers import AutoProcessor, AutoModelForCausalLM


# Questions redesigned for scientific charts/figures based on prior VLM
# outputs (axes, units, labels, trends, text transcription, equations,
# legend mappings, scale). Keep prompts concise and specific.
QUESTIONS = [
    "Give a brief high-level caption of the figure.",
    "Transcribe all visible text exactly as it appears (title, labels).",
    "What is the main title or heading?",
    "Is there a subtitle or caption text? If yes, transcribe it.",
    "What is the x-axis label and its unit?",
    "What is the y-axis label and its unit?",
    "List axis ranges and tick values for x and y.",
    "Is the scale linear or logarithmic on each axis?",
    "Describe the legend: categories and their color/marker mapping.",
    "List any symbols or abbreviations and their meanings if shown.",
    "Extract key numeric values, peaks, minima, or notable points.",
    "Describe visible trends or relationships (rise, fall, correlation).",
    "If an equation is shown, rewrite it as plain text.",
    "If a table is shown, summarize its rows/columns briefly.",
    "List units or percentages mentioned anywhere in the figure.",
    "Note any footnotes, sources, or figure labels (A/B/C panels).",
]


def build_inputs(processor: AutoProcessor, image: Image.Image, question: str):
    pixel_values = processor(images=image, return_tensors="pt").pixel_values
    enc = processor(text=question, add_special_tokens=False)
    input_ids = enc.input_ids if hasattr(enc, "input_ids") else enc["input_ids"]
    cls_id = getattr(processor.tokenizer, "cls_token_id", None)
    if cls_id is not None:
        input_ids = [cls_id] + input_ids
    input_ids = torch.tensor(input_ids, dtype=torch.long).unsqueeze(0)
    return {"pixel_values": pixel_values, "input_ids": input_ids}


def answer_question(model, processor, device, image_path, question, gen):
    img = Image.open(image_path).convert("RGB")
    inputs = build_inputs(processor, img, question)
    for k, v in inputs.items():
        if isinstance(v, torch.Tensor):
            inputs[k] = v.to(device)

    start = time.time()
    with torch.inference_mode():
        out = model.generate(**inputs, **gen)
        seq = out.sequences if hasattr(out, "sequences") else out
        prompt_len = inputs["input_ids"].shape[1]
        gen_tokens = seq[:, prompt_len:]
        text = processor.batch_decode(gen_tokens, skip_special_tokens=True)[0]
    end = time.time()
    return {
        "question": question,
        "output_text": text,
        "inference_time": end - start,
        "total_tokens": int(gen_tokens.shape[1]) if gen_tokens.dim() == 2 else 0,
        "generation_kwargs": gen,
    }


def main():
    parser = argparse.ArgumentParser(description="TextVQA with questions")
    parser.add_argument(
        "--model_name",
        default="microsoft/git-base-textvqa",
        help="TextVQA-capable model id",
    )
    parser.add_argument(
        "--image_dir",
        default="data/pdf_ocr_samples",
        help="Directory with test images (*.jpg)",
    )
    parser.add_argument(
        "--output_dir",
        default="output/GIT-base-textvqa-questions-v2",
        help="Where to save JSON results",
    )
    parser.add_argument(
        "--device",
        default="auto",
        choices=["auto", "cuda", "cpu"],
        help="Device",
    )

    args = parser.parse_args()

    device = torch.device(
        "cuda" if args.device == "auto" and torch.cuda.is_available() else args.device
    )
    if isinstance(device, str):
        device = torch.device(device)

    print(f"Using device: {device}")
    print(f"Loading model: {args.model_name}")

    model = AutoModelForCausalLM.from_pretrained(
        args.model_name,
        torch_dtype=(torch.float16 if device.type == "cuda" else torch.float32),
        device_map=("auto" if device.type == "cuda" else None),
        low_cpu_mem_usage=True,
    )
    if device.type == "cuda" and not hasattr(model, "hf_device_map"):
        model = model.to(device)

    processor = AutoProcessor.from_pretrained(args.model_name)

    image_dir = Path(args.image_dir)
    output_dir = Path(args.output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    files = sorted([p for p in image_dir.glob("*.jpg") if p.is_file()])
    print(f"Found {len(files)} images to process")

    # Increase budget for longer textual answers; beam for precision.
    gen = {
        "max_new_tokens": 96,
        "do_sample": False,
        "num_beams": 4,
        "length_penalty": 1.0,
        "early_stopping": True,
    }

    for i, p in enumerate(files, 1):
        print(f"\nProcessing {i}/{len(files)}: {p.name}")
        results = []
        total_time = 0.0
        for q in QUESTIONS:
            try:
                r = answer_question(model, processor, device, str(p), q, gen)
                results.append(r)
                total_time += r["inference_time"]
                print(
                    f"  Q: {q} -> {r['inference_time']:.2f}s, {r['total_tokens']} tokens"
                )
            except Exception as e:
                results.append(
                    {
                        "question": q,
                        "output_text": f"ERROR: {e}",
                        "inference_time": 0.0,
                        "total_tokens": 0,
                        "generation_kwargs": gen,
                        "error": str(e),
                    }
                )
                print(f"  Q error: {e}")

        data = {
            "image": str(p),
            "image_name": p.name,
            "total_processing_time": total_time,
            "questions": QUESTIONS,
            "results": results,
        }
        out = output_dir / f"{p.stem}.json"
        out.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
        print(f"  Saved: {out}")


if __name__ == "__main__":
    main()
