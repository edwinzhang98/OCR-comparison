#!/usr/bin/env python3
"""
Nougat 批量处理脚本
用于批量处理文件夹中的所有图片/PDF文件
"""

from transformers import NougatProcessor, VisionEncoderDecoderModel
from PIL import Image
import torch
from pathlib import Path
from tqdm import tqdm
import json
import time

class NougatBatchProcessor:
    def __init__(self, model_name="facebook/nougat-small", device=None):
        """
        初始化批量处理器
        
        Args:
            model_name: 模型名称，可选:
                - facebook/nougat-small (快速)
                - facebook/nougat-base (平衡)
            device: 运行设备，None则自动选择
        """
        print(f"初始化 Nougat 模型: {model_name}")
        self.processor = NougatProcessor.from_pretrained(model_name)
        self.model = VisionEncoderDecoderModel.from_pretrained(model_name)
        
        # 设置设备
        if device is None:
            self.device = "cuda" if torch.cuda.is_available() else "cpu"
        else:
            self.device = device
        
        self.model.to(self.device)
        print(f"使用设备: {self.device}")
        
        # 统计信息
        self.stats = {
            'processed': 0,
            'failed': 0,
            'total_time': 0
        }
    
    def process_image(self, image_path, max_length=1024):
        """处理单个图片"""
        try:
            # 加载图片
            image = Image.open(image_path).convert("RGB")
            
            # 预处理
            pixel_values = self.processor(image, return_tensors="pt").pixel_values
            pixel_values = pixel_values.to(self.device)
            
            # 生成
            outputs = self.model.generate(
                pixel_values,
                max_length=max_length,
                early_stopping=True,
                pad_token_id=self.processor.tokenizer.pad_token_id,
                eos_token_id=self.processor.tokenizer.eos_token_id,
                use_cache=True,
                num_beams=4,
                length_penalty=0.6
            )
            
            # 解码
            text = self.processor.batch_decode(outputs, skip_special_tokens=True)[0]
            text = self.processor.post_process_generation(text, fix_markdown=True)
            
            return text, None
            
        except Exception as e:
            return None, str(e)
    
    def process_folder(self, input_folder, output_folder=None, 
                       extensions=('.png', '.jpg', '.jpeg', '.bmp', '.tiff'),
                       save_json=True):
        """
        批量处理文件夹中的图片
        
        Args:
            input_folder: 输入文件夹路径
            output_folder: 输出文件夹路径，None则自动创建
            extensions: 要处理的文件扩展名
            save_json: 是否保存JSON格式的汇总结果
        """
        input_path = Path(input_folder)
        if not input_path.exists():
            raise ValueError(f"输入文件夹不存在: {input_folder}")
        
        # 创建输出文件夹
        if output_folder is None:
            output_path = Path("/workspace/output/nougat")
        else:
            output_path = Path(output_folder)
        output_path.mkdir(exist_ok=True, parents=True)
        
        # 收集所有图片文件
        image_files = []
        for ext in extensions:
            image_files.extend(input_path.glob(f"*{ext}"))
            image_files.extend(input_path.glob(f"*{ext.upper()}"))
        
        if not image_files:
            print(f"未找到图片文件 (支持的格式: {extensions})")
            return
        
        print(f"找到 {len(image_files)} 个图片文件")
        
        # 处理结果汇总
        results = []
        
        # 批量处理
        for image_file in tqdm(image_files, desc="处理进度"):
            start_time = time.time()
            
            # 处理图片
            text, error = self.process_image(image_file)
            
            process_time = time.time() - start_time
            self.stats['total_time'] += process_time
            
            if text is not None:
                # 保存结果
                output_file = output_path / f"{image_file.stem}.md"
                with open(output_file, 'w', encoding='utf-8') as f:
                    f.write(f"# OCR Result: {image_file.name}\n\n")
                    f.write(text)
                
                self.stats['processed'] += 1
                
                # 记录结果
                results.append({
                    'file': str(image_file),
                    'output': str(output_file),
                    'status': 'success',
                    'process_time': process_time,
                    'text_length': len(text),
                    'preview': text[:200] + '...' if len(text) > 200 else text
                })
                
                print(f"✅ {image_file.name} -> {output_file.name}")
            else:
                self.stats['failed'] += 1
                
                # 记录错误
                results.append({
                    'file': str(image_file),
                    'status': 'failed',
                    'error': error,
                    'process_time': process_time
                })
                
                print(f"❌ {image_file.name}: {error}")
        
        # 保存汇总结果
        if save_json:
            summary_file = output_path / "processing_summary.json"
            with open(summary_file, 'w', encoding='utf-8') as f:
                json.dump({
                    'stats': self.stats,
                    'results': results,
                    'model': self.model.config.name_or_path,
                    'device': self.device
                }, f, indent=2, ensure_ascii=False)
            print(f"\n汇总结果已保存到: {summary_file}")
        
        # 打印统计信息
        self.print_stats()
    
    def print_stats(self):
        """打印处理统计信息"""
        print("\n" + "="*50)
        print("处理统计:")
        print(f"  成功: {self.stats['processed']} 个文件")
        print(f"  失败: {self.stats['failed']} 个文件")
        print(f"  总用时: {self.stats['total_time']:.2f} 秒")
        if self.stats['processed'] > 0:
            avg_time = self.stats['total_time'] / self.stats['processed']
            print(f"  平均处理时间: {avg_time:.2f} 秒/文件")
        print("="*50)

def main():
    """主函数"""
    import argparse
    
    parser = argparse.ArgumentParser(description='Nougat 批量OCR处理')
    parser.add_argument('input_folder', help='输入文件夹路径')
    parser.add_argument('-o', '--output', help='输出文件夹路径')
    parser.add_argument('-m', '--model', default='facebook/nougat-small',
                       choices=['facebook/nougat-small', 'facebook/nougat-base'],
                       help='使用的模型版本')
    parser.add_argument('--max-length', type=int, default=1024,
                       help='最大输出长度')
    parser.add_argument('--extensions', nargs='+', 
                       default=['.png', '.jpg', '.jpeg', '.bmp'],
                       help='要处理的文件扩展名')
    parser.add_argument('--device', choices=['cuda', 'cpu', 'auto'],
                       default='auto', help='运行设备')
    
    args = parser.parse_args()
    
    # 设置设备
    if args.device == 'auto':
        device = None
    else:
        device = args.device
    
    # 创建处理器
    processor = NougatBatchProcessor(model_name=args.model, device=device)
    
    # 执行批量处理
    try:
        processor.process_folder(
            input_folder=args.input_folder,
            output_folder=args.output,
            extensions=tuple(args.extensions)
        )
    except KeyboardInterrupt:
        print("\n用户中断处理")
        processor.print_stats()
    except Exception as e:
        print(f"错误: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    # 如果没有命令行参数，提供交互式界面
    import sys
    
    if len(sys.argv) == 1:
        print("Nougat 批量OCR处理工具")
        print("="*50)
        folder = input("请输入要处理的文件夹路径: ").strip()
        if folder:
            processor = NougatBatchProcessor()
            processor.process_folder(folder)
        else:
            print("未输入路径，退出程序")
            print("\n命令行用法:")
            print("  python nougat_batch.py <文件夹路径> [选项]")
            print("\n选项:")
            print("  -o OUTPUT     指定输出文件夹")
            print("  -m MODEL      选择模型 (small/base)")
            print("  --device      选择设备 (cuda/cpu/auto)")
    else:
        main()
