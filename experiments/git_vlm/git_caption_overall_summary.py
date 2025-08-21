#!/usr/bin/env python3
r"""Aggregate caption-mode results across multiple GIT models.

Reads per-image JSONs from several caption result directories and
produces a combined Markdown/CSV summary comparing presets across models.
"""

import json
import statistics
from pathlib import Path
import argparse
import pandas as pd


def collect_stats(results_dir: Path):
    model_name = results_dir.name
    json_files = sorted(results_dir.glob("*.json"))
    preset_time_map = {}
    preset_token_map = {}
    total_times = []

    for jf in json_files:
        try:
            data = json.loads(jf.read_text(encoding="utf-8"))
        except Exception:
            continue
        total_times.append(float(data.get("total_processing_time", 0.0)))
        for res in data.get("results", []):
            p = res.get("preset", "unknown")
            t = float(res.get("inference_time", 0.0))
            tok = int(res.get("total_tokens", 0))
            preset_time_map.setdefault(p, []).append(t)
            preset_token_map.setdefault(p, []).append(tok)

    summary_rows = []
    for p in sorted(preset_time_map.keys() | preset_token_map.keys()):
        times = preset_time_map.get(p, [])
        toks = preset_token_map.get(p, [])
        summary_rows.append({
            "model": model_name,
            "preset": p,
            "avg_inference_time": statistics.mean(times) if times else 0.0,
            "avg_tokens": statistics.mean(toks) if toks else 0.0,
            "images": len(json_files),
            "total_time": sum(total_times) if total_times else 0.0,
        })
    return summary_rows


def main():
    parser = argparse.ArgumentParser(
        description="Overall caption summary across models"
    )
    parser.add_argument(
        "--result_dirs",
        nargs="+",
        default=[
            "output/GIT-base-coco-caption",
            "output/GIT-large-coco-caption",
            "output/GIT-base-caption",
        ],
        help="List of caption result directories",
    )
    parser.add_argument(
        "--out_dir",
        default="output",
        help="Where to write the combined summary",
    )
    args = parser.parse_args()

    rows = []
    for rd in args.result_dirs:
        rp = Path(rd)
        if not rp.exists():
            print(f"Skip missing: {rd}")
            continue
        rows.extend(collect_stats(rp))

    if not rows:
        print("No data collected")
        return

    df = pd.DataFrame(rows)
    out_dir = Path(args.out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)

    # Per-model table
    md_path = out_dir / "git_caption_overall_summary.md"
    with open(md_path, "w", encoding="utf-8") as f:
        f.write("# GIT Caption Overall Summary\n\n")
        for model, sub in df.groupby("model"):
            f.write(f"## {model}\n\n")
            sub2 = sub.sort_values(["preset"]) \
                     [["preset", "avg_inference_time", "avg_tokens", "images", "total_time"]]
            f.write(sub2.to_markdown(index=False))
            f.write("\n\n")

        # Cross-model pivot by preset
        f.write("## Cross-model comparison by preset\n\n")
        piv_time = df.pivot_table(
            index="preset", columns="model", values="avg_inference_time"
        )
        f.write("### Avg inference time (s)\n\n")
        f.write(piv_time.to_markdown())
        f.write("\n\n")

        piv_tok = df.pivot_table(
            index="preset", columns="model", values="avg_tokens"
        )
        f.write("### Avg tokens\n\n")
        f.write(piv_tok.to_markdown())
        f.write("\n")

    csv_path = out_dir / "git_caption_overall_summary.csv"
    df.to_csv(csv_path, index=False, encoding="utf-8")
    print(f"Wrote: {md_path}")
    print(f"Wrote: {csv_path}")


if __name__ == "__main__":
    main()
