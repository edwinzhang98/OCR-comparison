#!/usr/bin/env python3
"""
Nougat OCR 快速测试脚本
最简化的版本，快速测试单个图片
"""

from transformers import NougatProcessor, VisionEncoderDecoderModel
from PIL import Image
import torch
import sys

def ocr_image(image_path):
    """
    使用 Nougat 识别图片中的文字和公式
    
    Args:
        image_path: 图片文件路径
    
    Returns:
        识别出的 Markdown 格式文本
    """
    print(f"正在处理: {image_path}")
    
    # 1. 加载模型（首次运行会自动下载）
    print("加载模型...")
    processor = NougatProcessor.from_pretrained("facebook/nougat-base")
    model = VisionEncoderDecoderModel.from_pretrained("facebook/nougat-base")
    
    # 使用GPU（如果可用）
    device = "cuda" if torch.cuda.is_available() else "cpu"
    model.to(device)
    print(f"使用设备: {device}")
    
    # 2. 加载并预处理图片
    print("读取图片...")
    image = Image.open(image_path).convert("RGB")
    pixel_values = processor(image, return_tensors="pt").pixel_values.to(device)
    
    # 3. 生成文本
    print("识别中...")
    outputs = model.generate(
        pixel_values,
        max_length=2048,  # 最大输出长度
        early_stopping=True,
        pad_token_id=processor.tokenizer.pad_token_id,
        eos_token_id=processor.tokenizer.eos_token_id,
        use_cache=True,
        num_beams=5,  # beam search 提高质量
        length_penalty=0.6
    )
    
    # 4. 解码输出
    text = processor.batch_decode(outputs, skip_special_tokens=True)[0]
    text = processor.post_process_generation(text, fix_markdown=True)
    
    return text

# 主程序
if __name__ == "__main__":
    # 从命令行获取图片路径，或使用默认值
    if len(sys.argv) > 1:
        image_path = sys.argv[1]
    else:
        # 请修改为您的图片路径
        image_path = "test.png"
        print(f"未指定图片，使用默认: {image_path}")
        print("用法: python nougat_quick.py <图片路径>")
    
    try:
        # 执行OCR
        result = ocr_image(image_path)
        
        # 显示结果
        print("\n" + "="*50)
        print("识别结果:")
        print("="*50)
        print(result)
        
        # 保存到文件
        # 创建输出目录
        import os
        output_dir = "/workspace/output/nougat"
        os.makedirs(output_dir, exist_ok=True)
        
        # 提取图片文件名
        image_filename = os.path.basename(image_path)
        output_filename = os.path.splitext(image_filename)[0] + "_ocr.md"
        output_file = os.path.join(output_dir, output_filename)
        
        # 保存结果
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(result)
        print(f"\n结果已保存到: {output_file}")
        
    except FileNotFoundError:
        print(f"❌ 找不到文件: {image_path}")
    except Exception as e:
        print(f"❌ 出错了: {e}")
