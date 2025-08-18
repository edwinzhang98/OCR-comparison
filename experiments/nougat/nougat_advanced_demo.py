#!/usr/bin/env python3
"""
Nougat 高级参数演示脚本
展示所有可配置参数的使用方法
"""

from transformers import NougatProcessor, VisionEncoderDecoderModel
from transformers import GenerationConfig
from PIL import Image
import torch
import time
from pathlib import Path
from typing import Dict, Optional
import json

class NougatAdvancedOCR:
    """Nougat高级OCR处理器"""
    
    # 预定义的配置模板
    PRESET_CONFIGS = {
        "fast": {
            "description": "快速模式 - 牺牲一些质量换取速度",
            "model": "facebook/nougat-small",
            "generation": {
                "max_length": 2048,
                "num_beams": 3,
                "length_penalty": 0.5,
                "early_stopping": True,
                "no_repeat_ngram_size": 2
            }
        },
        "balanced": {
            "description": "平衡模式 - 速度和质量的平衡",
            "model": "facebook/nougat-base",
            "generation": {
                "max_length": 3072,
                "num_beams": 5,
                "length_penalty": 0.6,
                "early_stopping": True,
                "no_repeat_ngram_size": 3
            }
        },
        "quality": {
            "description": "高质量模式 - 最佳识别质量",
            "model": "facebook/nougat-base",
            "generation": {
                "max_length": 4096,
                "num_beams": 8,
                "length_penalty": 0.7,
                "early_stopping": False,
                "no_repeat_ngram_size": 4,
                "num_beam_groups": 2,
                "diversity_penalty": 0.5
            }
        },
        "math": {
            "description": "数学文档模式 - 优化数学公式识别",
            "model": "facebook/nougat-base",
            "generation": {
                "max_length": 5120,
                "num_beams": 10,
                "length_penalty": 0.8,
                "early_stopping": False,
                "no_repeat_ngram_size": 3,
                "temperature": 0.9,
                "top_k": 50
            }
        },
        "table": {
            "description": "表格文档模式 - 优化表格识别",
            "model": "facebook/nougat-base",
            "generation": {
                "max_length": 4096,
                "num_beams": 6,
                "length_penalty": 0.6,
                "no_repeat_ngram_size": 5,
                "repetition_penalty": 1.2
            }
        }
    }
    
    def __init__(self, preset: str = "balanced", custom_config: Dict = None):
        """
        初始化高级OCR处理器
        
        Args:
            preset: 预设配置 ("fast", "balanced", "quality", "math", "table")
            custom_config: 自定义配置字典
        """
        # 选择配置
        if custom_config:
            self.config = custom_config
            print(f"📋 使用自定义配置")
        elif preset in self.PRESET_CONFIGS:
            self.config = self.PRESET_CONFIGS[preset]
            print(f"📋 使用预设: {preset} - {self.config['description']}")
        else:
            self.config = self.PRESET_CONFIGS["balanced"]
            print(f"📋 使用默认配置: balanced")
        
        # 设置设备
        self.device = "cuda" if torch.cuda.is_available() else "cpu"
        self.dtype = torch.float16 if self.device == "cuda" else torch.float32
        
        # 加载模型
        model_name = self.config.get("model", "facebook/nougat-base")
        print(f"🚀 加载模型: {model_name}")
        print(f"   设备: {self.device}")
        print(f"   精度: {'FP16' if self.dtype == torch.float16 else 'FP32'}")
        
        self.model = VisionEncoderDecoderModel.from_pretrained(
            model_name,
            torch_dtype=self.dtype,
            low_cpu_mem_usage=True,
            use_safetensors=True if Path(f"{model_name}/model.safetensors").exists() else False
        ).to(self.device)
        
        self.processor = NougatProcessor.from_pretrained(model_name)
        
        # 设置生成配置
        self.generation_config = GenerationConfig(**self.config.get("generation", {}))
        
        # 编译模型（PyTorch 2.0+）
        if hasattr(torch, 'compile') and self.device == "cuda":
            print("⚡ 编译模型以提高性能...")
            self.model = torch.compile(self.model)
        
        self.model.eval()
        print("✅ 模型准备就绪\n")
    
    def process_with_params(self, 
                           image_path: str,
                           max_length: Optional[int] = None,
                           num_beams: Optional[int] = None,
                           temperature: Optional[float] = None,
                           top_k: Optional[int] = None,
                           top_p: Optional[float] = None,
                           repetition_penalty: Optional[float] = None,
                           length_penalty: Optional[float] = None,
                           no_repeat_ngram_size: Optional[int] = None,
                           do_sample: Optional[bool] = None,
                           early_stopping: Optional[bool] = None,
                           show_stats: bool = True) -> Dict:
        """
        使用自定义参数处理图像
        
        Args:
            image_path: 图像路径
            max_length: 最大输出长度
            num_beams: Beam搜索数量
            temperature: 温度参数（控制随机性）
            top_k: Top-K采样
            top_p: Top-P采样
            repetition_penalty: 重复惩罚
            length_penalty: 长度惩罚
            no_repeat_ngram_size: 禁止重复的n-gram大小
            do_sample: 是否使用采样
            early_stopping: 是否早停
            show_stats: 是否显示统计信息
        
        Returns:
            包含结果和统计信息的字典
        """
        print(f"📄 处理图像: {image_path}")
        
        # 加载图像
        image = Image.open(image_path).convert('RGB')
        print(f"   图像尺寸: {image.size}")
        
        # 创建生成配置
        gen_kwargs = {}
        
        # 更新参数（只添加非None的参数）
        if max_length is not None:
            gen_kwargs['max_length'] = max_length
        if num_beams is not None:
            gen_kwargs['num_beams'] = num_beams
        if temperature is not None:
            gen_kwargs['temperature'] = temperature
        if top_k is not None:
            gen_kwargs['top_k'] = top_k
        if top_p is not None:
            gen_kwargs['top_p'] = top_p
        if repetition_penalty is not None:
            gen_kwargs['repetition_penalty'] = repetition_penalty
        if length_penalty is not None:
            gen_kwargs['length_penalty'] = length_penalty
        if no_repeat_ngram_size is not None:
            gen_kwargs['no_repeat_ngram_size'] = no_repeat_ngram_size
        if do_sample is not None:
            gen_kwargs['do_sample'] = do_sample
        if early_stopping is not None:
            gen_kwargs['early_stopping'] = early_stopping
        
        # 合并默认配置
        final_config = {**self.config.get("generation", {}), **gen_kwargs}
        
        if show_stats:
            print("\n⚙️ 生成参数:")
            for key, value in final_config.items():
                print(f"   {key}: {value}")
        
        # 预处理图像
        start_time = time.time()
        pixel_values = self.processor(image, return_tensors="pt").pixel_values
        pixel_values = pixel_values.to(self.device)
        preprocess_time = time.time() - start_time
        
        # 生成文本
        print("\n🔄 生成中...")
        start_time = time.time()
        
        with torch.no_grad():
            if self.device == "cuda":
                with torch.cuda.amp.autocast():
                    outputs = self.model.generate(
                        pixel_values,
                        **final_config,
                        bad_words_ids=[[self.processor.tokenizer.unk_token_id]],
                        use_cache=True,
                        pad_token_id=self.processor.tokenizer.pad_token_id,
                        eos_token_id=self.processor.tokenizer.eos_token_id
                    )
            else:
                outputs = self.model.generate(
                    pixel_values,
                    **final_config,
                    bad_words_ids=[[self.processor.tokenizer.unk_token_id]],
                    use_cache=True,
                    pad_token_id=self.processor.tokenizer.pad_token_id,
                    eos_token_id=self.processor.tokenizer.eos_token_id
                )
        
        generation_time = time.time() - start_time
        
        # 解码输出
        start_time = time.time()
        generated_text = self.processor.batch_decode(outputs, skip_special_tokens=True)[0]
        
        # 后处理
        processed_text = self.processor.post_process_generation(
            generated_text, 
            fix_markdown=True
        )
        
        decode_time = time.time() - start_time
        
        # 统计信息
        stats = {
            "total_time": preprocess_time + generation_time + decode_time,
            "preprocess_time": preprocess_time,
            "generation_time": generation_time,
            "decode_time": decode_time,
            "output_tokens": outputs.shape[1],
            "text_length": len(processed_text),
            "tokens_per_second": outputs.shape[1] / generation_time if generation_time > 0 else 0
        }
        
        if show_stats:
            print("\n📊 统计信息:")
            print(f"   总用时: {stats['total_time']:.2f}秒")
            print(f"   - 预处理: {stats['preprocess_time']:.2f}秒")
            print(f"   - 生成: {stats['generation_time']:.2f}秒")
            print(f"   - 解码: {stats['decode_time']:.2f}秒")
            print(f"   输出tokens: {stats['output_tokens']}")
            print(f"   文本长度: {stats['text_length']}字符")
            print(f"   生成速度: {stats['tokens_per_second']:.1f} tokens/秒")
        
        return {
            "text": processed_text,
            "raw_text": generated_text,
            "stats": stats,
            "config": final_config
        }
    
    def compare_configs(self, image_path: str, total_images=None, current_index=None):
        """
        比较不同配置的效果
        
        Args:
            image_path: 测试图像路径
            total_images: 总图片数量
            current_index: 当前处理的图片索引
        """
        # 显示进度信息
        if total_images and current_index is not None:
            progress_percent = (current_index / total_images) * 100
            print(f"\n🔄 进度: [{current_index}/{total_images}] - {progress_percent:.1f}%")
            print(f"📄 当前处理: {Path(image_path).name}")
            
        print("🔬 配置对比实验")
        print("=" * 60)
        
        model_name_for_path = self.model.name_or_path.replace("/", "_")
        output_dir = Path("output") / model_name_for_path
        output_dir.mkdir(parents=True, exist_ok=True)
        
        results_for_table = {}
        md_content = f"# Comparison for {Path(image_path).name}\n\n"
        
        # 计算预设配置的总数，用于显示子进度
        total_presets = len(self.PRESET_CONFIGS)
        
        for preset_idx, (preset_name, preset_config) in enumerate(self.PRESET_CONFIGS.items(), 1):
            # 显示子进度
            if total_images and current_index is not None:
                sub_progress = (preset_idx / total_presets) * 100
                print(f"\n测试配置: {preset_name} [{preset_idx}/{total_presets}] - {sub_progress:.1f}%")
            else:
                print(f"\n测试配置: {preset_name}")
                
            print(f"描述: {preset_config['description']}")
            print("-" * 40)
            
            # 临时更新配置
            original_config = self.config
            self.config = preset_config
            self.generation_config = GenerationConfig(**preset_config.get("generation", {}))
            
            # 处理图像
            result = self.process_with_params(
                image_path,
                show_stats=False
            )
            
            # 记录结果用于表格
            results_for_table[preset_name] = {
                "time": result['stats']['total_time'],
                "length": result['stats']['text_length'],
                "speed": result['stats']['tokens_per_second'],
            }
            
            # 构建Markdown内容
            md_content += f"## Preset: {preset_name}\n\n"
            md_content += f"**Description:** {preset_config['description']}\n\n"
            md_content += f"**Time:** {result['stats']['total_time']:.2f}s  \n"
            md_content += f"**Length:** {result['stats']['text_length']} characters  \n"
            md_content += f"**Speed:** {result['stats']['tokens_per_second']:.1f} tokens/s  \n\n"
            md_content += f"### Generated Text\n\n"
            md_content += f"```markdown\n{result['text']}\n```\n\n"
            md_content += "---\n\n"

            print(f"用时: {result['stats']['total_time']:.2f}秒")
            print(f"输出长度: {result['stats']['text_length']}字符")
            
            # 恢复原始配置
            self.config = original_config
        
        # 打印对比表
        print("\n" + "=" * 60)
        print("📊 性能对比汇总:")
        print("-" * 60)
        print(f"{'配置':<10} {'用时(秒)':<10} {'字符数':<10} {'速度(t/s)':<12}")
        print("-" * 60)
        
        for name, stats in results_for_table.items():
            print(f"{name:<10} {stats['time']:<10.2f} {stats['length']:<10} {stats['speed']:<12.1f}")
        
        # 保存对比结果到Markdown文件
        output_file = output_dir / (Path(image_path).stem + "_comparison.md")
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(md_content)
        print(f"\n💾 对比结果已保存到: {output_file}")
    
    def adaptive_process(self, image_path: str) -> str:
        """
        自适应处理 - 根据图像内容自动选择最佳参数
        
        Args:
            image_path: 图像路径
        
        Returns:
            识别的文本
        """
        print("🤖 自适应处理模式")
        
        # 分析图像特征
        image = Image.open(image_path)
        width, height = image.size
        aspect_ratio = width / height
        
        # 根据图像特征选择配置
        if aspect_ratio > 1.5:
            # 宽图像，可能是表格
            print("   检测到: 宽幅图像，使用表格优化配置")
            preset = "table"
        elif height > 2000:
            # 长图像，可能是长文档
            print("   检测到: 长文档，使用高质量配置")
            preset = "quality"
        else:
            # 标准文档
            print("   检测到: 标准文档，使用平衡配置")
            preset = "balanced"
        
        # 应用配置
        self.config = self.PRESET_CONFIGS[preset]
        self.generation_config = GenerationConfig(**self.config.get("generation", {}))
        
        # 处理
        result = self.process_with_params(image_path)
        return result['text']

def demo_all_features():
    """演示所有功能"""
    print("🍩 Nougat 高级功能演示")
    print("=" * 60)
    
    # 1. 基础使用
    print("\n1️⃣ 基础使用示例:")
    print("-" * 40)
    ocr = NougatAdvancedOCR(preset="balanced")
    
    # 2. 自定义参数
    print("\n2️⃣ 自定义参数示例:")
    print("-" * 40)
    custom_config = {
        "model": "facebook/nougat-base",
        "generation": {
            "max_length": 4096,
            "num_beams": 7,
            "temperature": 0.8,
            "top_k": 40,
            "top_p": 0.95,
            "repetition_penalty": 1.1,
            "length_penalty": 0.65,
            "no_repeat_ngram_size": 4,
            "do_sample": False,
            "early_stopping": True
        }
    }
    ocr_custom = NougatAdvancedOCR(custom_config=custom_config)
    
    # 3. 参数组合示例
    print("\n3️⃣ 常用参数组合:")
    print("-" * 40)
    
    # 快速草稿模式
    print("快速草稿模式:")
    print("  - num_beams=1 (贪婪解码)")
    print("  - max_length=1024")
    print("  - early_stopping=True")
    
    # 高精度模式
    print("\n高精度模式:")
    print("  - num_beams=10")
    print("  - temperature=0.7")
    print("  - no_repeat_ngram_size=5")
    print("  - early_stopping=False")
    
    # 创造性模式
    print("\n创造性模式 (不推荐用于OCR):")
    print("  - do_sample=True")
    print("  - temperature=1.2")
    print("  - top_k=50")
    print("  - top_p=0.9")

if __name__ == "__main__":
    import argparse
    import glob
    
    parser = argparse.ArgumentParser(description='Nougat 高级参数演示')
    parser.add_argument('image', nargs='?', help='输入图像路径')
    parser.add_argument('--preset', choices=['fast', 'balanced', 'quality', 'math', 'table'],
                       default='balanced', help='使用预设配置')
    parser.add_argument('--compare', action='store_true', help='比较所有配置')
    parser.add_argument('--adaptive', action='store_true', help='自适应模式')
    parser.add_argument('--demo', action='store_true', help='演示模式')
    parser.add_argument('--batch', help='批量处理目录中的所有图片')
    
    # 生成参数
    parser.add_argument('--max-length', type=int, help='最大输出长度')
    parser.add_argument('--num-beams', type=int, help='Beam搜索数量')
    parser.add_argument('--temperature', type=float, help='温度参数')
    parser.add_argument('--top-k', type=int, help='Top-K采样')
    parser.add_argument('--top-p', type=float, help='Top-P采样')
    parser.add_argument('--repetition-penalty', type=float, help='重复惩罚')
    parser.add_argument('--length-penalty', type=float, help='长度惩罚')
    parser.add_argument('--no-repeat-ngram-size', type=int, help='禁止重复n-gram')
    parser.add_argument('--do-sample', action='store_true', help='使用采样')
    parser.add_argument('--no-early-stopping', action='store_true', help='禁用早停')
    
    args = parser.parse_args()
    
    if args.demo:
        demo_all_features()
    elif args.batch:
        # 批量处理模式
        image_files = sorted(glob.glob(f"{args.batch}/*.jpg") + glob.glob(f"{args.batch}/*.png") + 
                            glob.glob(f"{args.batch}/*.jpeg") + glob.glob(f"{args.batch}/*.JPG"))
        
        if not image_files:
            print(f"错误: 在 {args.batch} 目录中未找到图片文件")
            exit(1)
            
        print(f"🔍 找到 {len(image_files)} 个图片文件")
        print(f"📂 批量处理目录: {args.batch}")
        print("=" * 60)
        
        # 创建处理器
        ocr = NougatAdvancedOCR(preset=args.preset)
        
        # 处理每个图片
        for idx, img_path in enumerate(image_files, 1):
            if args.compare:
                # 比较模式
                ocr.compare_configs(img_path, total_images=len(image_files), current_index=idx)
            elif args.adaptive:
                # 自适应模式
                print(f"\n🔄 进度: [{idx}/{len(image_files)}] - {(idx/len(image_files))*100:.1f}%")
                print(f"📄 当前处理: {Path(img_path).name}")
                text = ocr.adaptive_process(img_path)
                print("\n识别结果:")
                print(text)
            else:
                # 常规处理
                print(f"\n🔄 进度: [{idx}/{len(image_files)}] - {(idx/len(image_files))*100:.1f}%")
                print(f"📄 当前处理: {Path(img_path).name}")
                result = ocr.process_with_params(
                    img_path,
                    max_length=args.max_length,
                    num_beams=args.num_beams,
                    temperature=args.temperature,
                    top_k=args.top_k,
                    top_p=args.top_p,
                    repetition_penalty=args.repetition_penalty,
                    length_penalty=args.length_penalty,
                    no_repeat_ngram_size=args.no_repeat_ngram_size,
                    do_sample=args.do_sample,
                    early_stopping=not args.no_early_stopping if args.no_early_stopping else None
                )
                
                print("\n📝 识别结果:")
                print("=" * 60)
                print(result['text'])
    elif args.image:
        # 创建处理器
        ocr = NougatAdvancedOCR(preset=args.preset)
        
        if args.compare:
            # 比较模式
            ocr.compare_configs(args.image)
        elif args.adaptive:
            # 自适应模式
            text = ocr.adaptive_process(args.image)
            print("\n识别结果:")
            print(text)
        else:
            # 常规处理
            result = ocr.process_with_params(
                args.image,
                max_length=args.max_length,
                num_beams=args.num_beams,
                temperature=args.temperature,
                top_k=args.top_k,
                top_p=args.top_p,
                repetition_penalty=args.repetition_penalty,
                length_penalty=args.length_penalty,
                no_repeat_ngram_size=args.no_repeat_ngram_size,
                do_sample=args.do_sample,
                early_stopping=not args.no_early_stopping if args.no_early_stopping else None
            )
            
            print("\n📝 识别结果:")
            print("=" * 60)
            print(result['text'])
    else:
        print("请提供图像路径或使用 --demo 查看演示")
        parser.print_help()
