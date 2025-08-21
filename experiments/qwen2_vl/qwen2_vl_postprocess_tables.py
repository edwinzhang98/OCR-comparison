#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Build per-image comparison tables for Qwen2-VL outputs.

- Input: a directory like 'Output/Qwen2-VL-7B-Instruct' containing
  aggregated JSON per image (fields: image, model_id, results[]).
- Output: for each JSON, emit a CSV and a Markdown table named
  '<stem>_comparison.csv' and '<stem>_comparison.md' in the same folder.

Table schema per requirements:
- First column: preset name
- Second column: output_text
- Third column: prompt
- Remaining columns: generation parameters (flattened from
  'generation_kwargs')
"""
from __future__ import annotations
import os
import json
import csv
import argparse
from pathlib import Path
from typing import Dict, Any, List, Set


def read_json(path: Path) -> Dict[str, Any]:
    """Read a JSON file into a dict.

    Args:
        path (Path): File path to read.

    Returns:
        Dict[str, Any]: Parsed JSON object.
    """
    with path.open("r", encoding="utf-8") as f:
        return json.load(f)


def sanitize_cell(value: Any) -> str:
    """Convert any value to a single-line string for table cells.

    Args:
        value (Any): Cell value.

    Returns:
        str: String with newlines collapsed to spaces.
    """
    if value is None:
        return ""
    s = str(value)
    return " ".join(s.splitlines()).strip()


def build_union_gen_keys(results: List[Dict[str, Any]]) -> List[str]:
    """Collect the union of generation_kwargs keys across results.

    Args:
        results (List[Dict[str, Any]]): Result items with
            'generation_kwargs'.

    Returns:
        List[str]: Sorted list of unique gen param keys.
    """
    keys: Set[str] = set()
    for r in results:
        gw = r.get("generation_kwargs", {}) or {}
        for k in gw.keys():
            keys.add(str(k))
    return sorted(keys)


def write_csv(
    out_path: Path,
    rows: List[Dict[str, Any]],
    gen_keys: List[str],
) -> None:
    """Write a CSV comparison table.

    Args:
        out_path (Path): Output CSV file path.
        rows (List[Dict[str, Any]]): Result rows.
        gen_keys (List[str]): Column keys for generation params.
    """
    header = ["preset", "output_text", "prompt"] + gen_keys
    with out_path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(header)
        for r in rows:
            gw = r.get("generation_kwargs", {}) or {}
            line = [
                sanitize_cell(r.get("preset")),
                sanitize_cell(r.get("output_text")),
                sanitize_cell(r.get("prompt")),
            ]
            for k in gen_keys:
                line.append(sanitize_cell(gw.get(k)))
            writer.writerow(line)


def write_markdown(
    out_path: Path,
    title: str,
    rows: List[Dict[str, Any]],
    gen_keys: List[str],
) -> None:
    """Write a Markdown comparison table.

    Args:
        out_path (Path): Output Markdown file path.
        title (str): Optional title to show at top.
        rows (List[Dict[str, Any]]): Result rows.
        gen_keys (List[str]): Column keys for generation params.
    """
    header = ["preset", "output_text", "prompt"] + gen_keys
    with out_path.open("w", encoding="utf-8") as f:
        if title:
            f.write(f"### {title}\n\n")
        # Table header
        f.write("| " + " | ".join(header) + " |\n")
        f.write("| " + " | ".join(["---"] * len(header)) + " |\n")
        # Rows
        for r in rows:
            gw = r.get("generation_kwargs", {}) or {}
            cells: List[str] = [
                sanitize_cell(r.get("preset")),
                sanitize_cell(r.get("output_text")),
                sanitize_cell(r.get("prompt")),
            ]
            for k in gen_keys:
                cells.append(sanitize_cell(gw.get(k)))
            f.write("| " + " | ".join(cells) + " |\n")


def process_dir(output_dir: Path) -> None:
    """Process all aggregated JSON files to table formats.

    Args:
        output_dir (Path): Directory containing aggregated JSON files.
    """
    json_files = sorted(output_dir.glob("*.json"))
    for jf in json_files:
        try:
            agg = read_json(jf)
        except Exception as e:
            print(f"[skip] {jf.name}: {e}")
            continue
        results = agg.get("results", []) or []
        if not results:
            print(f"[warn] no results in {jf.name}")
            continue
        gen_keys = build_union_gen_keys(results)
        title = (
            f"Image: {Path(agg.get('image','')).name} | "
            f"Model: {agg.get('model_id','')}"
        )
        stem = jf.stem
        md_path = output_dir / f"{stem}_comparison.md"
        csv_path = output_dir / f"{stem}_comparison.csv"
        write_markdown(md_path, title, results, gen_keys)
        write_csv(csv_path, results, gen_keys)
        print(f"wrote: {md_path.name}, {csv_path.name}")


def main():
    """CLI entry point to build comparison tables for Qwen outputs."""
    parser = argparse.ArgumentParser(
        description=(
            "Build per-image comparison tables for Qwen2-VL outputs"
        )
    )
    parser.add_argument(
        "--output_dir",
        default="output/Qwen2-VL-7B-Instruct",
        help="Folder containing aggregated per-image JSONs",
    )
    args = parser.parse_args()
    process_dir(Path(args.output_dir))


if __name__ == "__main__":
    main()
