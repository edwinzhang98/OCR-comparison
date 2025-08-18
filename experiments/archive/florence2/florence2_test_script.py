#!/usr/bin/env python3
"""
Florence-2 多功能视觉模型测试脚本
支持OCR、目标检测、图像描述、视觉问答等多种任务
"""

import torch
from PIL import Image, ImageDraw, ImageFont
from transformers import AutoProcessor, AutoModelForCausalLM
import numpy as np
from pathlib import Path
import json
import time
from typing import Dict, List, Tuple, Optional
import re

class Florence2Tester:
    """Florence-2 模型测试器"""
    
    # 支持的任务类型和对应的提示词
    TASK_PROMPTS = {
        # OCR相关任务
        'ocr': '<OCR>',
        'ocr_with_region': '<OCR_WITH_REGION>',
        
        # 图像描述任务
        'caption': '<CAPTION>',
        'detailed_caption': '<DETAILED_CAPTION>',
        'more_detailed_caption': '<MORE_DETAILED_CAPTION>',
        
        # 目标检测任务
        'object_detection': '<OD>',
        'dense_region_caption': '<DENSE_REGION_CAPTION>',
        'region_proposal': '<REGION_PROPOSAL>',
        
        # 分割任务
        'referring_expression_segmentation': '<REFERRING_EXPRESSION_SEGMENTATION>',
        'region_to_segmentation': '<REGION_TO_SEGMENTATION>',
        'open_vocabulary_detection': '<OPEN_VOCABULARY_DETECTION>',
        'region_to_category': '<REGION_TO_CATEGORY>',
        'region_to_description': '<REGION_TO_DESCRIPTION>',
        
        # 视觉问答
        'vqa': '',  # VQA需要用户提供问题
        
        # 更多任务
        'caption_to_phrase_grounding': '<CAPTION_TO_PHRASE_GROUNDING>',
    }
    
    def __init__(self, model_id="microsoft/Florence-2-large", device=None):
        """
        初始化Florence-2模型
        
        Args:
            model_id: 模型ID，可选：
                - microsoft/Florence-2-base (0.23B参数)
                - microsoft/Florence-2-large (0.77B参数)
            device: 运行设备
        """
        print(f"🚀 正在加载 Florence-2 模型: {model_id}")
        print("首次加载需要下载模型，请耐心等待...")
        
        # 加载模型和处理器
        self.model = AutoModelForCausalLM.from_pretrained(
            model_id, 
            torch_dtype=torch.float16 if torch.cuda.is_available() else torch.float32,
            trust_remote_code=True
        )
        self.processor = AutoProcessor.from_pretrained(model_id, trust_remote_code=True)
        
        # 设置设备
        if device is None:
            self.device = "cuda" if torch.cuda.is_available() else "cpu"
        else:
            self.device = device
            
        self.model.to(self.device)
        self.model.eval()
        
        print(f"✅ 模型加载完成，使用设备: {self.device}")
        
        # 统计信息
        self.stats = {
            'total_tasks': 0,
            'successful_tasks': 0,
            'failed_tasks': 0,
            'total_time': 0
        }
    
    def run_task(self, image: Image.Image, task: str, text_input: str = "") -> Dict:
        """
        执行单个任务
        
        Args:
            image: PIL图像对象
            task: 任务类型
            text_input: 额外的文本输入（用于VQA等任务）
        
        Returns:
            包含结果的字典
        """
        try:
            start_time = time.time()
            
            # 获取任务提示词
            if task not in self.TASK_PROMPTS:
                raise ValueError(f"不支持的任务: {task}")
            
            prompt = self.TASK_PROMPTS[task]
            
            # 对于VQA任务，需要添加问题
            if task == 'vqa':
                if not text_input:
                    text_input = "What is in this image?"  # 默认问题
                prompt = f"<VQA> {text_input}"
            
            # 对于需要额外输入的任务
            if task in ['open_vocabulary_detection', 'caption_to_phrase_grounding']:
                if text_input:
                    prompt = f"{prompt}{text_input}"
            
            # 预处理输入
            inputs = self.processor(
                text=prompt, 
                images=image, 
                return_tensors="pt"
            ).to(self.device)
            
            # 生成输出
            with torch.no_grad():
                generated_ids = self.model.generate(
                    input_ids=inputs["input_ids"],
                    pixel_values=inputs["pixel_values"],
                    max_new_tokens=1024,
                    do_sample=False,
                    num_beams=3,
                )
            
            # 解码输出
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
            
            elapsed_time = time.time() - start_time
            
            # 更新统计
            self.stats['total_tasks'] += 1
            self.stats['successful_tasks'] += 1
            self.stats['total_time'] += elapsed_time
            
            return {
                'task': task,
                'prompt': prompt,
                'raw_output': generated_text,
                'parsed_output': parsed_answer,
                'success': True,
                'time': elapsed_time
            }
            
        except Exception as e:
            self.stats['total_tasks'] += 1
            self.stats['failed_tasks'] += 1
            
            return {
                'task': task,
                'success': False,
                'error': str(e)
            }
    
    def visualize_detection(self, image: Image.Image, detection_result: Dict) -> Image.Image:
        """
        可视化检测结果
        
        Args:
            image: 原始图像
            detection_result: 检测结果
        
        Returns:
            标注后的图像
        """
        draw = ImageDraw.Draw(image)
        
        # 尝试加载字体
        try:
            font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 16)
        except:
            font = ImageFont.load_default()
        
        # 解析检测结果
        if 'bboxes' in detection_result and 'labels' in detection_result:
            bboxes = detection_result['bboxes']
            labels = detection_result['labels']
            
            # 为每个类别分配颜色
            colors = [
                'red', 'green', 'blue', 'yellow', 'purple', 
                'cyan', 'magenta', 'orange', 'pink', 'lime'
            ]
            
            for i, (bbox, label) in enumerate(zip(bboxes, labels)):
                color = colors[i % len(colors)]
                
                # 画边界框
                draw.rectangle(bbox, outline=color, width=2)
                
                # 画标签背景
                text_bbox = draw.textbbox((0, 0), label, font=font)
                text_width = text_bbox[2] - text_bbox[0]
                text_height = text_bbox[3] - text_bbox[1]
                
                label_bg = [bbox[0], bbox[1] - text_height - 4, 
                           bbox[0] + text_width + 4, bbox[1]]
                draw.rectangle(label_bg, fill=color)
                
                # 画标签文本
                draw.text((bbox[0] + 2, bbox[1] - text_height - 2), 
                         label, fill='white', font=font)
        
        return image
    
    def test_all_tasks(self, image_path: str, output_dir: str = None):
        """
        测试所有支持的任务
        
        Args:
            image_path: 图像文件路径
            output_dir: 输出目录路径
        """
        print(f"\n📸 测试图像: {image_path}")
        print("=" * 60)
        
        # 加载图像
        image = Image.open(image_path).convert('RGB')
        print(f"图像尺寸: {image.size}")
        
        # 创建输出目录
        if output_dir is None:
            output_dir = Path("/workspace/output/florence2")
        else:
            output_dir = Path(output_dir)
        output_dir.mkdir(exist_ok=True, parents=True)
        
        # 测试结果
        results = {
            'image': str(image_path),
            'image_size': image.size,
            'tasks': {}
        }
        
        # 定义要测试的任务
        test_tasks = [
            ('caption', '📝 图像描述'),
            ('detailed_caption', '📄 详细描述'),
            ('ocr', '📖 文字识别(OCR)'),
            ('ocr_with_region', '📍 带区域的OCR'),
            ('object_detection', '🎯 目标检测'),
            ('dense_region_caption', '🗺️ 密集区域描述'),
        ]
        
        # 执行每个任务
        for task_name, task_desc in test_tasks:
            print(f"\n{task_desc} ({task_name})...")
            print("-" * 40)
            
            result = self.run_task(image, task_name)
            results['tasks'][task_name] = result
            
            if result['success']:
                print(f"✅ 成功 (用时: {result['time']:.2f}秒)")
                
                # 打印结果预览
                if 'parsed_output' in result:
                    output = result['parsed_output']
                    
                    # 根据任务类型显示结果
                    if task_name in ['caption', 'detailed_caption', 'more_detailed_caption']:
                        # 文本描述类任务
                        if isinstance(output, dict) and task_name in output:
                            text = output[task_name]
                        else:
                            text = str(output)
                        print(f"结果: {text[:200]}..." if len(text) > 200 else f"结果: {text}")
                        
                    elif task_name == 'ocr':
                        # OCR任务
                        if isinstance(output, dict) and 'OCR' in output:
                            text = output['OCR']
                        else:
                            text = str(output)
                        lines = text.split('\n')[:5]  # 显示前5行
                        for line in lines:
                            print(f"  {line[:80]}..." if len(line) > 80 else f"  {line}")
                        if len(text.split('\n')) > 5:
                            print(f"  ... (共 {len(text.split('\n'))} 行)")
                            
                    elif task_name == 'object_detection':
                        # 目标检测任务
                        if isinstance(output, dict) and 'bboxes' in output:
                            n_objects = len(output['bboxes'])
                            print(f"检测到 {n_objects} 个对象")
                            if 'labels' in output:
                                # 统计每个类别的数量
                                from collections import Counter
                                label_counts = Counter(output['labels'])
                                for label, count in label_counts.most_common(5):
                                    print(f"  - {label}: {count} 个")
                                    
                            # 保存可视化结果
                            vis_image = self.visualize_detection(image.copy(), output)
                            vis_path = output_dir / f"{Path(image_path).stem}_detection.png"
                            vis_image.save(vis_path)
                            print(f"  可视化结果已保存: {vis_path}")
                            
                    elif task_name == 'dense_region_caption':
                        # 密集区域描述
                        if isinstance(output, dict):
                            if 'bboxes' in output and 'labels' in output:
                                n_regions = len(output['bboxes'])
                                print(f"生成了 {n_regions} 个区域描述")
                                # 显示前3个描述
                                for i, label in enumerate(output['labels'][:3]):
                                    print(f"  区域{i+1}: {label[:60]}...")
                                    
            else:
                print(f"❌ 失败: {result.get('error', 'Unknown error')}")
        
        # 保存完整结果
        results_file = output_dir / f"{Path(image_path).stem}_results.json"
        with open(results_file, 'w', encoding='utf-8') as f:
            json.dump(results, f, indent=2, ensure_ascii=False)
        print(f"\n💾 完整结果已保存到: {results_file}")
        
        # 打印统计信息
        self.print_stats()
        
        return results
    
    def interactive_vqa(self, image_path: str):
        """
        交互式视觉问答
        
        Args:
            image_path: 图像文件路径
        """
        print(f"\n🤖 视觉问答模式")
        print(f"图像: {image_path}")
        print("输入 'quit' 退出\n")
        
        # 加载图像
        image = Image.open(image_path).convert('RGB')
        
        while True:
            question = input("❓ 请提问: ").strip()
            
            if question.lower() in ['quit', 'exit', 'q']:
                break
            
            if not question:
                continue
            
            # 执行VQA
            result = self.run_task(image, 'vqa', question)
            
            if result['success']:
                answer = result['parsed_output']
                if isinstance(answer, dict):
                    answer = answer.get('VQA', str(answer))
                print(f"💡 回答: {answer}\n")
            else:
                print(f"❌ 错误: {result.get('error', 'Unknown error')}\n")
    
    def print_stats(self):
        """打印统计信息"""
        print("\n" + "=" * 60)
        print("📊 统计信息:")
        print(f"  总任务数: {self.stats['total_tasks']}")
        print(f"  成功: {self.stats['successful_tasks']}")
        print(f"  失败: {self.stats['failed_tasks']}")
        if self.stats['successful_tasks'] > 0:
            avg_time = self.stats['total_time'] / self.stats['successful_tasks']
            print(f"  平均处理时间: {avg_time:.2f} 秒/任务")
        print("=" * 60)

def main():
    """主函数"""
    import argparse
    
    parser = argparse.ArgumentParser(description='Florence-2 多功能视觉模型测试')
    parser.add_argument('image', help='输入图像路径')
    parser.add_argument('--task', choices=list(Florence2Tester.TASK_PROMPTS.keys()),
                       help='指定任务类型，不指定则测试所有任务')
    parser.add_argument('--model', default='microsoft/Florence-2-large',
                       choices=['microsoft/Florence-2-base', 'microsoft/Florence-2-large'],
                       help='模型版本')
    parser.add_argument('--output', help='输出目录')
    parser.add_argument('--vqa', action='store_true', help='进入交互式VQA模式')
    parser.add_argument('--text', help='额外的文本输入（用于VQA等）')
    
    args = parser.parse_args()
    
    # 检查图像文件
    if not Path(args.image).exists():
        print(f"❌ 图像文件不存在: {args.image}")
        return
    
    # 创建测试器
    print("🚀 Florence-2 视觉模型测试工具")
    print("=" * 60)
    tester = Florence2Tester(model_id=args.model)
    
    # 执行测试
    if args.vqa:
        # 交互式VQA模式
        tester.interactive_vqa(args.image)
    elif args.task:
        # 测试单个任务
        image = Image.open(args.image).convert('RGB')
        result = tester.run_task(image, args.task, args.text or "")
        
        if result['success']:
            print(f"\n✅ 任务成功: {args.task}")
            print(f"结果: {json.dumps(result['parsed_output'], indent=2, ensure_ascii=False)}")
        else:
            print(f"\n❌ 任务失败: {result.get('error', 'Unknown error')}")
    else:
        # 测试所有任务
        tester.test_all_tasks(args.image, args.output)

if __name__ == "__main__":
    import sys
    
    if len(sys.argv) == 1:
        # 交互式界面
        print("🌟 Florence-2 多功能视觉模型测试工具")
        print("=" * 60)
        print("Florence-2 支持以下任务:")
        print("  • OCR - 文字识别")
        print("  • 图像描述 - 生成自然语言描述")
        print("  • 目标检测 - 检测和定位对象")
        print("  • 视觉问答 - 回答关于图像的问题")
        print("  • 区域描述 - 描述图像中的特定区域")
        print()
        
        image_path = input("请输入图像路径: ").strip()
        if image_path:
            tester = Florence2Tester()
            
            print("\n选择模式:")
            print("1. 测试所有任务")
            print("2. 交互式问答")
            print("3. 只做OCR")
            
            choice = input("请选择 (1/2/3): ").strip()
            
            if choice == '2':
                tester.interactive_vqa(image_path)
            elif choice == '3':
                image = Image.open(image_path).convert('RGB')
                result = tester.run_task(image, 'ocr')
                if result['success']:
                    print("\nOCR结果:")
                    print(result['parsed_output'].get('OCR', result['parsed_output']))
            else:
                tester.test_all_tasks(image_path)
        else:
            print("未输入路径，退出程序")
    else:
        main()
