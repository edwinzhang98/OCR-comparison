#!/usr/bin/env python3
r"""Summarize GIT batch test results.

Prints per-image total time, aggregate timing stats, per-preset averages
(tokens and time), and basic error listing.
"""

import json
import statistics
from pathlib import Path
import argparse


def generate_summary(results_dir: str) -> None:
    r"""Generate and print a summary from JSON results in a directory."""
    results_path = Path(results_dir)
    if not results_path.exists():
        print(f"Results directory not found: {results_dir}")
        return

    json_files = sorted(results_path.glob("*.json"))
    if not json_files:
        print(f"No JSON files found in {results_dir}")
        return

    print("GIT Testing Summary")
    print("=" * 50)
    print(f"Total images processed: {len(json_files)}\n")

    total_times = []
    preset_time_map = {}
    preset_token_map = {}
    errors = []

    for jf in json_files:
        try:
            with open(jf, "r", encoding="utf-8") as f:
                data = json.load(f)
        except Exception as e:
            print(f"Error reading {jf}: {e}")
            continue

        image_name = Path(data.get("image", "unknown")).name
        total_time = float(data.get("total_processing_time", 0.0))
        total_times.append(total_time)
        print(f"Image: {image_name:<15} Total time: {total_time:>6.2f}s")

        for res in data.get("results", []):
            p = res.get("preset", "unknown")
            t = float(res.get("inference_time", 0.0))
            tok = int(res.get("total_tokens", 0))
            preset_time_map.setdefault(p, []).append(t)
            preset_token_map.setdefault(p, []).append(tok)
            if "error" in res:
                errors.append(f"{image_name} - {p}: {res['error']}")

    print("\nTiming Statistics:")
    print("-" * 30)
    if total_times:
        print(
            f"Average total time per image: {statistics.mean(total_times):.2f}s"
        )
        print(
            f"Median total time per image: {statistics.median(total_times):.2f}s"
        )
        print(f"Min total time: {min(total_times):.2f}s")
        print(f"Max total time: {max(total_times):.2f}s")
        print(f"Total processing time: {sum(total_times):.2f}s")

    print("\nPreset Performance:")
    print("-" * 30)
    for p, times in preset_time_map.items():
        if not times:
            continue
        avg_t = statistics.mean(times)
        toks = preset_token_map.get(p, [])
        avg_tok = statistics.mean(toks) if toks else 0.0
        print(f"{p:<20} Avg time: {avg_t:>6.2f}s, Avg tokens: {avg_tok:>5.1f}")

    if errors:
        print("\nErrors encountered:")
        print("-" * 30)
        for e in errors:
            print(f"  {e}")

    md_cnt = len(list(results_path.glob("*_comparison.md")))
    csv_cnt = len(list(results_path.glob("*_comparison.csv")))
    print("\nOutput files:")
    print("-" * 30)
    print(f"JSON results: {len(json_files)} files")
    print(f"Comparison tables: {md_cnt} Markdown files")
    print(f"Comparison tables: {csv_cnt} CSV files")
    print(f"Results directory: {results_dir}")


def main() -> None:
    r"""CLI entrypoint."""
    parser = argparse.ArgumentParser(description="GIT results summary")
    parser.add_argument(
        "--results_dir",
        default="output/GIT-base-coco",
        help="Directory containing JSON result files",
    )
    args = parser.parse_args()
    generate_summary(args.results_dir)


if __name__ == "__main__":
    main()
