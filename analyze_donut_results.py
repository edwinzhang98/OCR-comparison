#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
分析 Donut OCR 结果，找出每个图片最适合的预设模式
"""

import os
import json
import pandas as pd
from pathlib import Path

RESULTS_DIR = "output/donut_results"

def analyze_results():
    """分析所有结果文件，生成摘要报告"""
    results = []
    
    # 遍历所有 JSON 结果文件
    for json_file in sorted(Path(RESULTS_DIR).glob("*.json")):
        if json_file.name == "capabilities.json":
            continue
            
        with open(json_file, "r") as f:
            data = json.load(f)
        
        image_path = data.get("image", "")
        image_name = Path(image_path).name
        
        # 获取所有成功的预设结果
        successful_results = []
        for result in data.get("results", []):
            if not result.get("error") and result.get("output_text"):
                preset = result.get("preset", "")
                output_len = len(result.get("output_text", ""))
                runtime = result.get("runtime_sec", 0)
                
                successful_results.append({
                    "preset": preset,
                    "output_length": output_len,
                    "runtime": runtime,
                    "efficiency": output_len / runtime if runtime > 0 else 0
                })
        
        # 按输出长度排序找出最佳预设
        if successful_results:
            # 按输出长度排序
            by_length = sorted(successful_results, key=lambda x: x["output_length"], reverse=True)
            best_by_length = by_length[0]
            
            # 按效率排序 (输出长度/运行时间)
            by_efficiency = sorted(successful_results, key=lambda x: x["efficiency"], reverse=True)
            best_by_efficiency = by_efficiency[0]
            
            results.append({
                "image": image_name,
                "best_preset_by_length": best_by_length["preset"],
                "max_output_length": best_by_length["output_length"],
                "best_preset_by_efficiency": best_by_efficiency["preset"],
                "best_efficiency": best_by_efficiency["efficiency"],
                "successful_presets": len(successful_results)
            })
    
    # 转换为 DataFrame 并分析
    df = pd.DataFrame(results)
    
    # 统计每个预设被选为最佳的次数
    best_by_length_counts = df["best_preset_by_length"].value_counts()
    best_by_efficiency_counts = df["best_preset_by_efficiency"].value_counts()
    
    print("\n=== 按输出长度的最佳预设统计 ===")
    print(best_by_length_counts)
    
    print("\n=== 按效率的最佳预设统计 ===")
    print(best_by_efficiency_counts)
    
    print("\n=== 每个图片的最佳预设 ===")
    for _, row in df.iterrows():
        print(f"{row['image']}: 最长输出: {row['best_preset_by_length']} ({row['max_output_length']}字符), "
              f"最高效率: {row['best_preset_by_efficiency']} ({row['best_efficiency']:.1f}字符/秒)")
    
    # 保存结果
    df.to_csv(os.path.join(RESULTS_DIR, "summary.csv"), index=False)
    print(f"\n结果已保存到 {os.path.join(RESULTS_DIR, 'summary.csv')}")
    
    return df

if __name__ == "__main__":
    analyze_results()
