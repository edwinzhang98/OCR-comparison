#!/usr/bin/env python3
"""
ScreenAI-5B results summary script.

This script provides an overview of the batch testing results including
timing statistics and preset performance.
"""

import json
import statistics
from pathlib import Path
import argparse


def generate_summary(results_dir: str):
    """Generate a summary of ScreenAI-5B testing results.
    
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
    
    print(f"ScreenAI-5B Testing Summary")
    print("=" * 50)
    print(f"Total images processed: {len(json_files)}")
    print()
    
    # Collect statistics
    total_times = []
    preset_times = {}
    preset_tokens = {}
    errors = []
    
    for json_file in json_files:
        try:
            with open(json_file, "r", encoding="utf-8") as f:
                data = json.load(f)
            
            image_name = Path(data.get("image", "unknown")).name
            total_time = data.get("total_processing_time", 0)
            total_times.append(total_time)
            
            print(f"Image: {image_name:<15} Total time: {total_time:>6.2f}s")
            
            # Collect preset statistics
            for result in data.get("results", []):
                preset = result.get("preset", "unknown")
                preset_time = result.get("inference_time", 0)
                preset_tokens_count = result.get("total_tokens", 0)
                
                if preset not in preset_times:
                    preset_times[preset] = []
                    preset_tokens[preset] = []
                
                preset_times[preset].append(preset_time)
                preset_tokens[preset].append(preset_tokens_count)
                
                if "error" in result:
                    errors.append(f"{image_name} - {preset}: {result['error']}")
            
        except Exception as e:
            print(f"Error reading {json_file}: {e}")
    
    print()
    print("Timing Statistics:")
    print("-" * 30)
    if total_times:
        print(f"Average total time per image: {statistics.mean(total_times):.2f}s")
        print(f"Median total time per image: {statistics.median(total_times):.2f}s")
        print(f"Min total time: {min(total_times):.2f}s")
        print(f"Max total time: {max(total_times):.2f}s")
        print(f"Total processing time: {sum(total_times):.2f}s")
    
    print()
    print("Preset Performance:")
    print("-" * 30)
    for preset, times in preset_times.items():
        if times:
            avg_time = statistics.mean(times)
            avg_tokens = statistics.mean(preset_tokens[preset])
            print(f"{preset:<20} Avg time: {avg_time:>6.2f}s, Avg tokens: {avg_tokens:>5.1f}")
    
    if errors:
        print()
        print("Errors encountered:")
        print("-" * 30)
        for error in errors:
            print(f"  {error}")
    
    print()
    print("Output files:")
    print("-" * 30)
    print(f"JSON results: {len(json_files)} files")
    print(f"Comparison tables: {len(list(results_path.glob('*_comparison.md')))} Markdown files")
    print(f"Comparison tables: {len(list(results_path.glob('*_comparison.csv')))} CSV files")
    print(f"Results directory: {results_dir}")


def main():
    """Main function."""
    parser = argparse.ArgumentParser(description="ScreenAI-5B results summary")
    parser.add_argument(
        "--results_dir",
        default="output/ScreenAI-5B",
        help="Directory containing JSON result files"
    )
    
    args = parser.parse_args()
    generate_summary(args.results_dir)


if __name__ == "__main__":
    main()
