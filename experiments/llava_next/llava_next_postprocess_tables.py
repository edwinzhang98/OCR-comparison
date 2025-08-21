#!/usr/bin/env python3
"""
LLaVA-NeXT-7B post-processing script to generate comparison tables.

This script reads the JSON output files from the batch testing and creates
comparison tables in both Markdown and CSV formats for easy analysis.
"""

import os
import json
import pandas as pd
from pathlib import Path
import argparse


def process_results_to_tables(results_dir: str):
    """Process JSON results and generate comparison tables.
    
    Args:
        results_dir: Directory containing the JSON result files
    """
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
        
        print(f"Processing: {json_file.name}")
        
        try:
            with open(json_file, "r", encoding="utf-8") as f:
                data = json.load(f)
        except Exception as e:
            print(f"  Error reading {json_file}: {e}")
            continue
        
        image_name = Path(data.get("image", "unknown_image")).name
        total_time = data.get("total_processing_time", 0)
        
        records = []
        for result in data.get("results", []):
            record = {
                "preset": result.get("preset", "N/A"),
                "output_text": result.get("output_text", "N/A"),
                "prompt": result.get("prompt", "N/A"),
                "inference_time": result.get("inference_time", 0),
                "total_tokens": result.get("total_tokens", 0),
            }
            
            # Add generation_kwargs as separate columns
            for k, v in result.get("generation_kwargs", {}).items():
                record[f"gen_{k}"] = v
            
            # Add error information if present
            if "error" in result:
                record["error"] = result["error"]
            
            records.append(record)
        
        if records:
            df = pd.DataFrame(records)
            
            # Define column order - put key columns first
            key_cols = ["preset", "output_text", "prompt", "inference_time", "total_tokens"]
            gen_cols = sorted([c for c in df.columns if c.startswith("gen_")])
            other_cols = [c for c in df.columns if c not in key_cols + gen_cols]
            
            cols = key_cols + gen_cols + other_cols
            df = df[cols]
            
            # Save to Markdown with better formatting
            md_output_path = results_path / f"{Path(json_file.stem)}_comparison.md"
            with open(md_output_path, "w", encoding="utf-8") as f:
                f.write(f"# LLaVA-NeXT-7B Comparison for {image_name}\n\n")
                f.write(f"**Total Processing Time:** {total_time:.2f}s\n\n")
                f.write("## Results Comparison\n\n")
                
                # Process each result individually for better formatting
                for i, record in enumerate(records):
                    f.write(f"### {record['preset']}\n\n")
                    f.write(f"**Prompt:** {record['prompt']}\n\n")
                    f.write(f"**Output:** {record['output_text']}\n\n")
                    f.write(f"**Inference Time:** {record['inference_time']:.2f}s\n")
                    f.write(f"**Total Tokens:** {record['total_tokens']}\n")
                    
                    # Add generation parameters
                    gen_params = {k: v for k, v in record.items() if k.startswith('gen_')}
                    if gen_params:
                        f.write("\n**Generation Parameters:**\n")
                        for param, value in gen_params.items():
                            f.write(f"- {param[4:]}: {value}\n")
                    
                    f.write("\n---\n\n")
            
            # Save to CSV
            csv_output_path = results_path / f"{Path(json_file.stem)}_comparison.csv"
            df.to_csv(csv_output_path, index=False, encoding="utf-8")
            
            print(f"  Generated: {md_output_path.name}, {csv_output_path.name}")
        else:
            print(f"  No valid results found in {json_file.name}")
    
    print(f"\nPost-processing completed. Tables saved to: {results_dir}")


def main():
    """Main function."""
    parser = argparse.ArgumentParser(description="LLaVA-NeXT-7B post-processing")
    parser.add_argument(
        "--results_dir",
        default="output/LLaVA-NeXT-7B-fixed",
        help="Directory containing JSON result files"
    )
    
    args = parser.parse_args()
    process_results_to_tables(args.results_dir)


if __name__ == "__main__":
    main()
