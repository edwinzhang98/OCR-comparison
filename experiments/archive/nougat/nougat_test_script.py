#!/usr/bin/env python3
"""
Nougat OCR 测试脚本
用于处理本地图片，特别是包含数学公式的科学文档
"""

import os
import sys
from pathlib import Path
from PIL import Image
import torch
from typing import List, Union
import time

# ==================== 方法1: 使用 nougat-ocr 包 ====================
def test_with_nougat_package():
    """
    使用官方 nougat-ocr 包进行测试
    首先需要安装: pip install nougat-ocr
    """
    print("=" * 60)
    print("方法1: 使用 nougat-ocr 包")
    print("=" * 60)
    
    try:
        from nougat import NougatModel
        from nougat.utils.dataset import ImageDataset
        from nougat.utils.checkpoint import get_checkpoint
        from nougat.postprocessing import markdown_compatible
        
        # 下载并加载模型
        print("正在加载模型...")
        checkpoint = get_checkpoint('nougat')
        model = NougatModel.from_pretrained(checkpoint)
        
        if torch.cuda.is_available():
            model = model.to('cuda')
            print("使用 GPU 加速")
        else:
            print("使用 CPU (速度较慢)")
        
        model.eval()
        
        # 处理图片
        def process_image(image_path: str):
            print(f"\n处理图片: {image_path}")
            
            # 准备数据
            dataset = ImageDataset(
                [image_path],
                partial_page=True
            )
            
            dataloader = torch.utils.data.DataLoader(
                dataset,
                batch_size=1,
                shuffle=False
            )
            
            # 推理
            predictions = []
            with torch.no_grad():
                for idx, sample in enumerate(dataloader):
                    if torch.cuda.is_available():
                        sample = sample.to('cuda')
                    
                    output = model.inference(
                        image_tensors=sample,
                        early_stopping=True
                    )
                    predictions.append(output)
            
            # 后处理
            result = predictions[0] if predictions else ""
            result = markdown_compatible(result)
            
            return result
            
    except ImportError:
        print("请先安装 nougat-ocr: pip install nougat-ocr")
        return None

# ==================== 方法2: 使用 HuggingFace Transformers ====================
def test_with_huggingface():
    """
    使用 HuggingFace Transformers 进行测试
    需要安装: pip install transformers torch pillow
    """
    print("=" * 60)
    print("方法2: 使用 HuggingFace Transformers")
    print("=" * 60)
    
    try:
        from transformers import NougatProcessor, VisionEncoderDecoderModel
        
        # 加载处理器和模型
        print("正在加载模型 (首次运行会下载模型，约1.5GB)...")
        
        # 可以选择不同的模型版本：
        # - facebook/nougat-small (更快但精度略低)
        # - facebook/nougat-base (平衡)
        model_name = "facebook/nougat-small"  # 使用小模型以加快速度
        
        processor = NougatProcessor.from_pretrained(model_name)
        model = VisionEncoderDecoderModel.from_pretrained(model_name)
        
        # 设置设备
        device = "cuda" if torch.cuda.is_available() else "cpu"
        model.to(device)
        print(f"使用设备: {device}")
        
        # 处理单个图片的函数
        def process_image(image_path: str, max_length: int = 1024):
            print(f"\n处理图片: {image_path}")
            start_time = time.time()
            
            # 加载图片
            image = Image.open(image_path)
            if image.mode != 'RGB':
                image = image.convert('RGB')
            
            # 预处理
            pixel_values = processor(image, return_tensors="pt").pixel_values
            pixel_values = pixel_values.to(device)
            
            # 生成输出
            print("正在识别...")
            outputs = model.generate(
                pixel_values,
                min_length=1,
                max_length=max_length,
                bad_words_ids=[[processor.tokenizer.unk_token_id]],
                return_dict_in_generate=True,
                output_scores=True,
                early_stopping=True,
                no_repeat_ngram_size=3,
                num_beams=5,  # 使用beam search提高质量
            )
            
            # 解码输出
            generated_text = processor.batch_decode(outputs.sequences, skip_special_tokens=True)[0]
            
            # 后处理：修复常见的markdown格式问题
            generated_text = processor.post_process_generation(generated_text, fix_markdown=True)
            
            elapsed_time = time.time() - start_time
            print(f"处理时间: {elapsed_time:.2f} 秒")
            
            return generated_text
        
        return process_image
        
    except ImportError as e:
        print(f"请安装必要的包: pip install transformers torch pillow")
        print(f"错误详情: {e}")
        return None

# ==================== 主测试函数 ====================
def main():
    """主测试函数"""
    
    # 配置测试图片路径
    # 请修改为您的本地图片路径
    test_images = [
        # 添加您的图片路径，例如：
        # "/path/to/your/image1.png",
        # "/path/to/your/image2.jpg",
        # "test_images/math_formula.png",
        # "test_images/scientific_paper.pdf",  # Nougat也支持PDF
    ]
    
    # 如果没有指定图片，尝试从命令行参数获取
    if not test_images and len(sys.argv) > 1:
        test_images = sys.argv[1:]
    
    # 如果还是没有图片，扫描当前目录
    if not test_images:
        print("未指定测试图片，扫描当前目录的图片文件...")
        current_dir = Path(".")
        test_images = []
        for ext in ['*.png', '*.jpg', '*.jpeg', '*.pdf']:
            test_images.extend(current_dir.glob(ext))
        test_images = [str(p) for p in test_images[:3]]  # 限制最多3个
    
    if not test_images:
        print("\n⚠️ 未找到测试图片！")
        print("请使用以下方式之一提供图片：")
        print("1. 修改脚本中的 test_images 列表")
        print("2. 命令行参数: python nougat_test.py image1.png image2.jpg")
        print("3. 将图片放在当前目录")
        return
    
    print(f"\n找到 {len(test_images)} 个测试图片")
    
    # 选择测试方法
    print("\n选择测试方法：")
    print("1. HuggingFace Transformers (推荐，更简单)")
    print("2. 官方 nougat-ocr 包")
    
    choice = input("请选择 (1 或 2，默认为 1): ").strip() or "1"
    
    if choice == "2":
        process_func = test_with_nougat_package()
    else:
        process_func = test_with_huggingface()
    
    if process_func is None:
        return
    
    # 创建输出目录
    output_dir = Path("/workspace/output/nougat")
    output_dir.mkdir(exist_ok=True)
    print(f"\n输出将保存到: {output_dir}")
    
    # 处理每个图片
    for image_path in test_images:
        if not Path(image_path).exists():
            print(f"\n⚠️ 文件不存在: {image_path}")
            continue
        
        try:
            # 处理图片
            result = process_func(image_path)
            
            if result:
                # 保存结果
                output_file = output_dir / f"{Path(image_path).stem}_output.md"
                with open(output_file, 'w', encoding='utf-8') as f:
                    f.write(f"# OCR Result for {Path(image_path).name}\n\n")
                    f.write(result)
                
                print(f"✅ 结果已保存到: {output_file}")
                
                # 打印前500个字符作为预览
                print("\n--- 识别结果预览 (前500字符) ---")
                print(result[:500])
                if len(result) > 500:
                    print("\n... (更多内容请查看输出文件)")
                print("-" * 40)
            
        except Exception as e:
            print(f"\n❌ 处理失败: {e}")
            import traceback
            traceback.print_exc()

# ==================== 安装说明 ====================
def print_installation_guide():
    """打印安装说明"""
    print("""
╔══════════════════════════════════════════════════════════════╗
║                    Nougat OCR 安装指南                        ║
╠══════════════════════════════════════════════════════════════╣
║                                                              ║
║  方法1: 使用 HuggingFace (推荐)                              ║
║  ────────────────────────────────────────                   ║
║  pip install transformers torch pillow                       ║
║                                                              ║
║  方法2: 使用官方包                                           ║
║  ────────────────────────────────────────                   ║
║  pip install nougat-ocr                                      ║
║                                                              ║
║  GPU 加速 (可选，但强烈推荐):                                ║
║  ────────────────────────────────────────                   ║
║  # CUDA 11.8                                                ║
║  pip install torch --index-url https://download.pytorch.org/whl/cu118  ║
║                                                              ║
║  # CUDA 12.1                                                ║
║  pip install torch --index-url https://download.pytorch.org/whl/cu121  ║
║                                                              ║
╚══════════════════════════════════════════════════════════════╝
    """)

if __name__ == "__main__":
    print("🍩 Nougat OCR 测试脚本")
    print("=" * 60)
    print("专门用于识别科学文档、数学公式和复杂排版")
    print()
    
    # 检查是否需要显示安装指南
    if "--help" in sys.argv or "-h" in sys.argv:
        print_installation_guide()
        sys.exit(0)
    
    # 运行主程序
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n用户中断")
    except Exception as e:
        print(f"\n程序错误: {e}")
        import traceback
        traceback.print_exc()
    
    print("\n✨ 测试完成！")
