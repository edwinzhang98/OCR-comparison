#!/usr/bin/env python3
r"""Post-process GIT batch results into Markdown/CSV tables per image.

Reads JSON files produced by git_batch_test.py and writes readable
Markdown blocks and a CSV table for each image.
"""

import json
from pathlib import Path
import argparse
import pandas as pd


def process_results_to_tables(results_dir: str) -> None:
    r"""Generate Markdown and CSV comparison outputs for each JSON."""
    results_path = Path(results_dir)
    if not results_path.exists():
        print(f"Results directory not found: {results_dir}")
        return

    json_files = sorted(results_path.glob("*.json"))
    if not json_files:
        print(f"No JSON files found in {results_dir}")
        return

    print(f"Processing {len(json_files)} result files...")

    for json_file in json_files:
        if json_file.name == "capabilities.json":
            continue

        try:
            with open(json_file, "r", encoding="utf-8") as f:
                data = json.load(f)
        except Exception as e:
            print(f"  Error reading {json_file}: {e}")
            continue

        image_name = Path(data.get("image", "unknown")).name
        total_time = float(data.get("total_processing_time", 0.0))

        records = []
        for res in data.get("results", []):
            rec = {
                "preset": res.get("preset", "N/A"),
                "output_text": res.get("output_text", ""),
                "prompt": res.get("prompt", ""),
                "inference_time": float(res.get("inference_time", 0.0)),
                "total_tokens": int(res.get("total_tokens", 0)),
            }
            for k, v in res.get("generation_kwargs", {}).items():
                rec[f"gen_{k}"] = v
            if "error" in res:
                rec["error"] = res["error"]
            records.append(rec)

        if not records:
            print(f"  No valid results in {json_file.name}")
            continue

        df = pd.DataFrame(records)
        key_cols = [
            "preset",
            "output_text",
            "prompt",
            "inference_time",
            "total_tokens",
        ]
        gen_cols = sorted([c for c in df.columns if c.startswith("gen_")])
        other_cols = [c for c in df.columns if c not in key_cols + gen_cols]
        df = df[key_cols + gen_cols + other_cols]

        # Write Markdown with blocks per preset
        md_path = results_path / f"{json_file.stem}_comparison.md"
        with open(md_path, "w", encoding="utf-8") as f:
            f.write(f"# GIT Comparison for {image_name}\n\n")
            f.write(f"**Total Processing Time:** {total_time:.2f}s\n\n")
            f.write("## Results Comparison\n\n")
            for rec in records:
                f.write(f"### {rec['preset']}\n\n")
                f.write(f"**Prompt:** {rec['prompt']}\n\n")
                f.write(f"**Output:** {rec['output_text']}\n\n")
                f.write(
                    f"**Inference Time:** {rec['inference_time']:.2f}s\n"
                )
                f.write(f"**Total Tokens:** {rec['total_tokens']}\n")
                gen_params = {k: v for k, v in rec.items() if k.startswith("gen_")}
                if gen_params:
                    f.write("\n**Generation Parameters:**\n")
                    for p, v in gen_params.items():
                        f.write(f"- {p[4:]}: {v}\n")
                f.write("\n---\n\n")

        # Write CSV
        csv_path = results_path / f"{json_file.stem}_comparison.csv"
        df.to_csv(csv_path, index=False, encoding="utf-8")
        print(f"  Generated: {md_path.name}, {csv_path.name}")

    print(f"\nPost-processing completed. Tables saved to: {results_dir}")


def main() -> None:
    r"""CLI entrypoint."""
    parser = argparse.ArgumentParser(description="GIT post-processing")
    parser.add_argument(
        "--results_dir",
        default="output/GIT-base-coco",
        help="Directory containing JSON result files",
    )
    args = parser.parse_args()
    process_results_to_tables(args.results_dir)


if __name__ == "__main__":
    main()
