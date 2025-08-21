#!/usr/bin/env python3
r"""Batch test script for the GIT image-to-text models.

This script evaluates a GIT checkpoint on a directory of images using
multiple presets tailored for complex chart/scientific captioning. It
saves one JSON per image with all preset runs, including per-preset
inference time, tokens, prompts, and generation params.

References:
- GIT docs: https://huggingface.co/docs/transformers/en/model_doc/git

Usage example:
    python3 experiments/git_vlm/git_batch_test.py \
        --model_name microsoft/git-base-coco \
        --image_dir data/pdf_ocr_samples \
        --output_dir output/GIT-base-coco \
        --device auto \
        --mode auto
"""

import json
import time
import argparse
from pathlib import Path
from typing import Any, Dict, List

import torch
from PIL import Image
from transformers import AutoProcessor, AutoModelForCausalLM


# ----------------------------- Presets ---------------------------------

def get_presets() -> Dict[str, Dict[str, Any]]:
    r"""Return preset configurations for complex chart/scientific images.

    The presets vary decoding strategies to balance detail and precision.
    """
    return {
        "chart_analysis": {
            "prompt": (
                "Analyze this chart or scientific diagram in detail. "
                "Describe axes, labels, units, legends, trends, and "
                "embedded text. Be comprehensive and accurate."
            ),
            "gen": {
                "max_new_tokens": 180,
                "do_sample": True,
                "temperature": 0.6,
                "top_p": 0.9,
                "repetition_penalty": 1.15,
                "no_repeat_ngram_size": 3,
            },
        },
        "technical_description": {
            "prompt": (
                "Provide a technical description. Identify text, numbers, "
                "symbols, axes ranges, and structural elements. Be "
                "precise and systematic."
            ),
            "gen": {
                "max_new_tokens": 140,
                "do_sample": False,
                "num_beams": 4,
                "length_penalty": 1.1,
                "repetition_penalty": 1.2,
                "early_stopping": True,
            },
        },
        "comprehensive_caption": {
            "prompt": (
                "Create a comprehensive caption suitable for academic "
                "documentation. Include visible text, chart elements, "
                "data patterns, and context."
            ),
            "gen": {
                "max_new_tokens": 220,
                "do_sample": True,
                "temperature": 0.7,
                "top_p": 0.95,
                "repetition_penalty": 1.25,
                "no_repeat_ngram_size": 4,
            },
        },
        "structured_analysis": {
            "prompt": (
                "Structured analysis: (1) main elements, (2) text/labels, "
                "(3) data patterns/trends, (4) overall purpose."
            ),
            "gen": {
                "max_new_tokens": 160,
                "do_sample": True,
                "temperature": 0.65,
                "top_p": 0.9,
                "repetition_penalty": 1.1,
                "no_repeat_ngram_size": 3,
            },
        },
        "precision_focused": {
            "prompt": (
                "Describe with high precision. Focus on exact text, "
                "numbers, symbols, and spatial relations. Avoid "
                "speculation; only observable facts."
            ),
            "gen": {
                "max_new_tokens": 120,
                "do_sample": False,
                "num_beams": 5,
                "length_penalty": 1.2,
                "repetition_penalty": 1.25,
                "early_stopping": True,
            },
        },
    }


# ----------------------------- Inference --------------------------------

def build_inputs(
    processor: AutoProcessor,
    image: Image.Image,
    prompt: str,
    mode: str,
) -> Dict[str, torch.Tensor]:
    r"""Prepare GIT inputs.

    - caption: pass only pixel_values (COCO caption usage)
    - vqa: pass pixel_values + input_ids (question/prompt)
    """
    pixel_values = processor(images=image, return_tensors="pt").pixel_values

    if mode == "caption":
        return {"pixel_values": pixel_values}

    # vqa mode
    enc = processor(text=prompt, add_special_tokens=False)
    input_ids: List[int] = enc.input_ids if hasattr(enc, "input_ids") else enc["input_ids"]
    cls_id = getattr(processor.tokenizer, "cls_token_id", None)
    if cls_id is not None:
        input_ids = [cls_id] + input_ids
    input_ids_tensor = torch.tensor(input_ids, dtype=torch.long).unsqueeze(0)
    return {"pixel_values": pixel_values, "input_ids": input_ids_tensor}


def run_once(
    model: AutoModelForCausalLM,
    processor: AutoProcessor,
    device: torch.device,
    image_path: str,
    preset_name: str,
    preset_cfg: Dict[str, Any],
    mode: str,
) -> Dict[str, Any]:
    r"""Run a single inference for one image and one preset.

    Decoding excludes prompt for vqa (by slicing off prompt tokens).
    """
    image = Image.open(image_path).convert("RGB")
    prompt = str(preset_cfg.get("prompt", ""))

    inputs = build_inputs(processor, image, prompt, mode)

    for key, value in inputs.items():
        if isinstance(value, torch.Tensor):
            inputs[key] = value.to(device)

    gen_kwargs = dict(preset_cfg.get("gen", {}))

    start_time = time.time()
    with torch.inference_mode():
        out = model.generate(**inputs, **gen_kwargs)
        sequences = out.sequences if hasattr(out, "sequences") else out

        if mode == "vqa" and "input_ids" in inputs:
            prompt_len = inputs["input_ids"].shape[1]
            gen_tokens = sequences[:, prompt_len:]
            output_text = processor.batch_decode(
                gen_tokens, skip_special_tokens=True
            )[0]
            total_tokens = int(gen_tokens.shape[1]) if gen_tokens.dim() == 2 else 0
        else:
            # caption mode: decode full sequences
            output_text = processor.batch_decode(
                sequences, skip_special_tokens=True
            )[0]
            total_tokens = int(sequences.shape[1]) if sequences.dim() == 2 else 0

    end_time = time.time()

    return {
        "preset": preset_name,
        "prompt": prompt,
        "generation_kwargs": gen_kwargs,
        "output_text": output_text,
        "inference_time": end_time - start_time,
        "total_tokens": total_tokens,
    }


# ------------------------------ Main ------------------------------------

def main() -> None:
    r"""Entry point for batch testing GIT models."""
    parser = argparse.ArgumentParser(description="GIT batch testing")
    parser.add_argument(
        "--model_name",
        default="microsoft/git-base-coco",
        help=(
            "Model id, e.g. microsoft/git-base-coco, microsoft/git-base, "
            "microsoft/git-large-coco, microsoft/git-base-textvqa"
        ),
    )
    parser.add_argument(
        "--image_dir",
        default="data/pdf_ocr_samples",
        help="Directory with test images (*.jpg)",
    )
    parser.add_argument(
        "--output_dir",
        default="output/GIT-base-coco",
        help="Directory to write JSON outputs",
    )
    parser.add_argument(
        "--device",
        default="auto",
        choices=["auto", "cuda", "cpu"],
        help="Device selection",
    )
    parser.add_argument(
        "--mode",
        default="auto",
        choices=["auto", "caption", "vqa"],
        help=(
            "Input mode: caption (pixel_values only), vqa (pixel_values + "
            "input_ids). auto: coco->caption, textvqa->vqa, else vqa."
        ),
    )

    args = parser.parse_args()

    # Device
    if args.device == "auto":
        device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    else:
        device = torch.device(args.device)

    # Mode auto-detection
    mode = args.mode
    mn = args.model_name.lower()
    if mode == "auto":
        if "coco" in mn:
            mode = "caption"
        elif "textvqa" in mn:
            mode = "vqa"
        else:
            mode = "vqa"

    print(f"Using device: {device}")
    print(f"Loading model: {args.model_name}")
    print(f"Mode: {mode}")

    # Load model & processor
    model = AutoModelForCausalLM.from_pretrained(
        args.model_name,
        torch_dtype=(torch.float16 if device.type == "cuda" else torch.float32),
        device_map=("auto" if device.type == "cuda" else None),
        low_cpu_mem_usage=True,
    )
    if device.type == "cuda" and not hasattr(model, "hf_device_map"):
        model = model.to(device)

    processor = AutoProcessor.from_pretrained(args.model_name)

    # Data & IO
    presets = get_presets()
    output_dir = Path(args.output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    image_dir = Path(args.image_dir)
    image_files = sorted([p for p in image_dir.glob("*.jpg") if p.is_file()])
    if not image_files:
        print(f"No JPG images found in {image_dir}")
        return

    print(f"Found {len(image_files)} images to process")

    # Process images
    for idx, image_path in enumerate(image_files, 1):
        print(f"\nProcessing image {idx}/{len(image_files)}: {image_path.name}")
        results: List[Dict[str, Any]] = []
        total_time = 0.0

        for preset_name, preset_cfg in presets.items():
            print(f"  Testing preset: {preset_name}")
            try:
                result = run_once(
                    model, processor, device, str(image_path), preset_name, preset_cfg, mode
                )
                results.append(result)
                total_time += result["inference_time"]
                print(
                    f"    {preset_name}: {result['inference_time']:.2f}s, "
                    f"{result['total_tokens']} tokens"
                )
            except Exception as e:
                print(f"    Error with preset {preset_name}: {e}")
                results.append(
                    {
                        "preset": preset_name,
                        "prompt": preset_cfg.get("prompt", ""),
                        "generation_kwargs": preset_cfg.get("gen", {}),
                        "output_text": f"ERROR: {e}",
                        "inference_time": 0.0,
                        "total_tokens": 0,
                        "error": str(e),
                    }
                )

        data = {
            "image": str(image_path),
            "image_name": image_path.name,
            "total_processing_time": total_time,
            "presets_tested": len(presets),
            "mode": mode,
            "results": results,
        }
        out_file = output_dir / f"{image_path.stem}.json"
        with open(out_file, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)

        print(f"  Saved results to: {out_file}")
        print(f"  Total processing time: {total_time:.2f}s")

    print(f"\nBatch testing completed. Results saved to: {output_dir}")


if __name__ == "__main__":
    main()
