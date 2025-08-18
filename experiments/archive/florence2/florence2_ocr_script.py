#!/usr/bin/env python3
"""
Florence-2 OCR与手写识别专用脚本
专门优化用于文档OCR、手写识别、表格提取等任务
"""

import torch
from PIL import Image
from transformers import AutoProcessor, AutoModelForCausalLM
import numpy as np
from pathlib import Path
import json
import re
from typing import Dict, List, Tuple, Optional
import pandas as pd

class Florence2OCR:
    """Florence-2 OCR专用处理器"""
    
    def __init__(self, model_id="microsoft/Florence-2-large"):
        """
        初始化OCR模型
        
        Args:
            model_id: 模型ID
                - microsoft/Florence-2-base: 轻量版
                - microsoft/Florence-2-large: 高精度版
        """
        print(f"📚 正在加载 Florence-2 OCR 模型: {model_id}")
        
        # 加载模型
        self.device = "cuda" if torch.cuda.is_available() else "cpu"
        dtype = torch.float16 if torch.cuda.is_available() else torch.float32
        
        self.model = AutoModelForCausalLM.from_pretrained(
            model_id,
            torch_dtype=dtype,
            trust_remote_code=True
        ).to(self.device)
        
        self.processor = AutoProcessor.from_pretrained(
            model_id, 
            trust_remote_code=True
        )
        
        self.model.eval()
        print(f"✅ 模型加载完成 (设备: {self.device})")
    
    def ocr_image(self, image_path: str, task_type: str = "ocr") -> Dict:
        """
        执行OCR识别
        
        Args:
            image_path: 图像路径
            task_type: 任务类型
                - "ocr": 基础OCR
                - "ocr_with_region": 带区域信息的OCR
        
        Returns:
            OCR结果字典
        """
        # 加载图像
        image = Image.open(image_path).convert('RGB')
        
        # 选择任务提示词
        if task_type == "ocr_with_region":
            prompt = "<OCR_WITH_REGION>"
        else:
            prompt = "<OCR>"
        
        # 处理图像
        inputs = self.processor(
            text=prompt,
            images=image,
            return_tensors="pt"
        ).to(self.device)
        
        # 生成文本
        with torch.no_grad():
            generated_ids = self.model.generate(
                input_ids=inputs["input_ids"],
                pixel_values=inputs["pixel_values"],
                max_new_tokens=2048,  # 增加长度以处理长文档
                do_sample=False,
                num_beams=3,
                early_stopping=False  # 不要过早停止，确保完整识别
            )
        
        # 解码结果
        generated_text = self.processor.batch_decode(
            generated_ids,
            skip_special_tokens=False
        )[0]
        
        # 解析结果
        parsed_answer = self.processor.post_process_generation(
            generated_text,
            task=prompt,
            image_size=(image.width, image.height)
        )
        
        return {
            'text': self._extract_text(parsed_answer, task_type),
            'raw_output': generated_text,
            'parsed_output': parsed_answer,
            'image_size': (image.width, image.height)
        }
    
    def _extract_text(self, parsed_output: Dict, task_type: str) -> str:
        """从解析输出中提取纯文本"""
        if isinstance(parsed_output, dict):
            if task_type == "ocr" and 'OCR' in parsed_output:
                return parsed_output['OCR']
            elif task_type == "ocr_with_region" and 'OCR_WITH_REGION' in parsed_output:
                # 处理带区域的OCR结果
                regions = parsed_output['OCR_WITH_REGION']
                if 'quad_boxes' in regions and 'labels' in regions:
                    # 按位置排序文本
                    texts = regions['labels']
                    boxes = regions['quad_boxes']
                    
                    # 简单的从上到下，从左到右排序
                    sorted_pairs = sorted(
                        zip(boxes, texts),
                        key=lambda x: (min(x[0][1], x[0][3]), min(x[0][0], x[0][2]))
                    )
                    
                    return '\n'.join([text for _, text in sorted_pairs])
                return str(regions)
        return str(parsed_output)
    
    def extract_table(self, image_path: str) -> pd.DataFrame:
        """
        从图像中提取表格
        
        Args:
            image_path: 包含表格的图像路径
        
        Returns:
            提取的表格数据 (DataFrame)
        """
        print(f"📊 提取表格: {image_path}")
        
        # 使用带区域的OCR
        result = self.ocr_image(image_path, "ocr_with_region")
        text = result['text']
        
        # 尝试解析表格结构
        lines = text.split('\n')
        
        # 简单的表格解析逻辑
        # 这里假设表格是用空格或制表符分隔的
        table_data = []
        for line in lines:
            if line.strip():
                # 尝试用多种分隔符分割
                cells = re.split(r'\s{2,}|\t|｜|\|', line.strip())
                cells = [cell.strip() for cell in cells if cell.strip()]
                if cells:
                    table_data.append(cells)
        
        # 创建DataFrame
        if table_data:
            # 假设第一行是表头
            df = pd.DataFrame(table_data[1:], columns=table_data[0])
            return df
        else:
            return pd.DataFrame()
    
    def process_handwritten(self, image_path: str) -> Dict:
        """
        专门处理手写文档
        
        Args:
            image_path: 手写文档图像路径
        
        Returns:
            识别结果
        """
        print(f"✍️ 处理手写文档: {image_path}")
        
        # 加载图像
        image = Image.open(image_path).convert('RGB')
        
        results = {}
        
        # 1. 执行基础OCR
        print("  执行OCR识别...")
        ocr_result = self.ocr_image(image_path, "ocr")
        results['ocr_text'] = ocr_result['text']
        
        # 2. 执行带区域的OCR（获取布局信息）
        print("  分析文档布局...")
        region_result = self.ocr_image(image_path, "ocr_with_region")
        results['structured_text'] = region_result['text']
        
        # 3. 生成文档描述
        print("  生成文档描述...")
        caption_result = self._get_caption(image)
        results['description'] = caption_result
        
        # 4. 后处理：清理和格式化文本
        results['cleaned_text'] = self._clean_handwritten_text(results['ocr_text'])
        
        return results
    
    def _get_caption(self, image: Image.Image) -> str:
        """获取图像描述"""
        prompt = "<DETAILED_CAPTION>"
        
        inputs = self.processor(
            text=prompt,
            images=image,
            return_tensors="pt"
        ).to(self.device)
        
        with torch.no_grad():
            generated_ids = self.model.generate(
                input_ids=inputs["input_ids"],
                pixel_values=inputs["pixel_values"],
                max_new_tokens=256,
                do_sample=False,
                num_beams=3
            )
        
        generated_text = self.processor.batch_decode(
            generated_ids,
            skip_special_tokens=False
        )[0]
        
        parsed = self.processor.post_process_generation(
            generated_text,
            task=prompt,
            image_size=(image.width, image.height)
        )
        
        if isinstance(parsed, dict) and 'DETAILED_CAPTION' in parsed:
            return parsed['DETAILED_CAPTION']
        return str(parsed)
    
    def _clean_handwritten_text(self, text: str) -> str:
        """清理手写识别文本"""
        if not text:
            return ""
        
        # 修复常见的手写识别错误
        cleaned = text
        
        # 修复标点符号间距
        cleaned = re.sub(r'\s+([,.\!?;:])', r'\1', cleaned)
        cleaned = re.sub(r'([,.\!?;:])\s*', r'\1 ', cleaned)
        
        # 修复多余的空格
        cleaned = re.sub(r'\s+', ' ', cleaned)
        
        # 修复段落
        cleaned = re.sub(r'\n\s*\n', '\n\n', cleaned)
        
        return cleaned.strip()
    
    def batch_process(self, folder_path: str, output_dir: str = None):
        """
        批量处理文件夹中的所有图像
        
        Args:
            folder_path: 输入文件夹路径
            output_dir: 输出目录路径
        """
        folder = Path(folder_path)
        if not folder.exists():
            print(f"❌ 文件夹不存在: {folder_path}")
            return
        
        # 创建输出目录
        if output_dir is None:
            output_path = Path("/workspace/output/florence2")
        else:
            output_path = Path(output_dir)
        output_path.mkdir(exist_ok=True, parents=True)
        
        # 查找所有图像文件
        image_extensions = ['.png', '.jpg', '.jpeg', '.bmp', '.tiff', '.webp']
        image_files = []
        for ext in image_extensions:
            image_files.extend(folder.glob(f"*{ext}"))
            image_files.extend(folder.glob(f"*{ext.upper()}"))
        
        if not image_files:
            print(f"❌ 未找到图像文件")
            return
        
        print(f"📂 找到 {len(image_files)} 个图像文件")
        
        # 批量处理
        all_results = []
        
        for i, image_file in enumerate(image_files, 1):
            print(f"\n[{i}/{len(image_files)}] 处理: {image_file.name}")
            
            try:
                # OCR识别
                result = self.ocr_image(str(image_file))
                
                # 保存文本结果
                text_file = output_path / f"{image_file.stem}.txt"
                with open(text_file, 'w', encoding='utf-8') as f:
                    f.write(result['text'])
                
                # 记录结果
                all_results.append({
                    'file': str(image_file),
                    'output': str(text_file),
                    'text_length': len(result['text']),
                    'status': 'success'
                })
                
                print(f"  ✅ 已保存到: {text_file.name}")
                print(f"  识别字符数: {len(result['text'])}")
                
            except Exception as e:
                print(f"  ❌ 处理失败: {e}")
                all_results.append({
                    'file': str(image_file),
                    'status': 'failed',
                    'error': str(e)
                })
        
        # 保存汇总结果
        summary_file = output_path / "summary.json"
        with open(summary_file, 'w', encoding='utf-8') as f:
            json.dump(all_results, f, indent=2, ensure_ascii=False)
        
        print(f"\n📊 处理完成！")
        print(f"  成功: {sum(1 for r in all_results if r['status'] == 'success')}")
        print(f"  失败: {sum(1 for r in all_results if r['status'] == 'failed')}")
        print(f"  结果保存在: {output_path}")

def main():
    """主函数"""
    import argparse
    
    parser = argparse.ArgumentParser(description='Florence-2 OCR工具')
    parser.add_argument('input', help='输入图像或文件夹路径')
    parser.add_argument('--output', '-o', help='输出目录')
    parser.add_argument('--model', default='microsoft/Florence-2-large',
                       choices=['microsoft/Florence-2-base', 'microsoft/Florence-2-large'],
                       help='模型版本')
    parser.add_argument('--region', action='store_true', 
                       help='使用带区域信息的OCR')
    parser.add_argument('--table', action='store_true',
                       help='提取表格')
    parser.add_argument('--handwritten', action='store_true',
                       help='手写文档模式')
    parser.add_argument('--batch', action='store_true',
                       help='批量处理模式')
    
    args = parser.parse_args()
    
    # 创建OCR处理器
    ocr = Florence2OCR(model_id=args.model)
    
    # 判断输入类型
    input_path = Path(args.input)
    
    if input_path.is_dir() or args.batch:
        # 批量处理
        ocr.batch_process(args.input, args.output)
    elif input_path.is_file():
        # 单文件处理
        if args.table:
            # 提取表格
            df = ocr.extract_table(args.input)
            if not df.empty:
                print("\n提取的表格:")
                print(df)
                
                # 保存CSV
                output_dir = Path("/workspace/output/florence2")
                output_dir.mkdir(exist_ok=True, parents=True)
                output_file = output_dir / f"{input_path.stem}_table.csv"
                df.to_csv(output_file, index=False, encoding='utf-8')
                print(f"\n表格已保存到: {output_file}")
            else:
                print("未能提取到表格数据")
                
        elif args.handwritten:
            # 手写文档模式
            results = ocr.process_handwritten(args.input)
            
            print("\n📝 手写识别结果:")
            print("-" * 50)
            print(results['cleaned_text'])
            print("-" * 50)
            print(f"\n文档描述: {results['description']}")
            
            # 保存结果
            output_dir = Path("/workspace/output/florence2")
            output_dir.mkdir(exist_ok=True, parents=True)
            output_file = output_dir / f"{input_path.stem}_handwritten.json"
            with open(output_file, 'w', encoding='utf-8') as f:
                json.dump(results, f, indent=2, ensure_ascii=False)
            print(f"\n完整结果已保存到: {output_file}")
            
        else:
            # 普通OCR
            task_type = "ocr_with_region" if args.region else "ocr"
            result = ocr.ocr_image(args.input, task_type)
            
            print("\n📖 OCR识别结果:")
            print("=" * 60)
            print(result['text'])
            print("=" * 60)
            
            # 保存结果
            output_dir = Path("/workspace/output/florence2")
            output_dir.mkdir(exist_ok=True, parents=True)
            output_file = output_dir / f"{input_path.stem}_ocr.txt"
            with open(output_file, 'w', encoding='utf-8') as f:
                f.write(result['text'])
            print(f"\n结果已保存到: {output_file}")
    else:
        print(f"❌ 输入路径不存在: {args.input}")

if __name__ == "__main__":
    import sys
    
    if len(sys.argv) == 1:
        # 交互式界面
        print("🔤 Florence-2 OCR 工具")
        print("=" * 60)
        print("专门优化用于:")
        print("  • 📖 文档OCR - 识别印刷和手写文字")
        print("  • ✍️ 手写识别 - 专门处理手写文档")
        print("  • 📊 表格提取 - 从图像中提取表格数据")
        print("  • 📑 批量处理 - 处理整个文件夹")
        print()
        
        path = input("请输入图像路径或文件夹路径: ").strip()
        
        if path:
            ocr = Florence2OCR()
            
            if Path(path).is_dir():
                print("\n检测到文件夹，执行批量处理...")
                ocr.batch_process(path)
            else:
                print("\n选择处理模式:")
                print("1. 普通OCR")
                print("2. 手写文档识别")
                print("3. 表格提取")
                print("4. 带区域的OCR")
                
                choice = input("请选择 (1-4): ").strip()
                
                if choice == '2':
                    results = ocr.process_handwritten(path)
                    print("\n识别结果:")
                    print(results['cleaned_text'])
                elif choice == '3':
                    df = ocr.extract_table(path)
                    print("\n提取的表格:")
                    print(df)
                elif choice == '4':
                    result = ocr.ocr_image(path, "ocr_with_region")
                    print("\n识别结果:")
                    print(result['text'])
                else:
                    result = ocr.ocr_image(path)
                    print("\n识别结果:")
                    print(result['text'])
    else:
        main()
