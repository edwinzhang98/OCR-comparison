#!/usr/bin/env python3
"""
Florence-2 快速测试 - 最简单的使用示例
只需10行代码即可运行OCR！
"""

from transformers import AutoProcessor, AutoModelForCausalLM
from PIL import Image
import sys

# 1. 加载模型（首次运行会自动下载）
model = AutoModelForCausalLM.from_pretrained("microsoft/Florence-2-large", trust_remote_code=True)
processor = AutoProcessor.from_pretrained("microsoft/Florence-2-large", trust_remote_code=True)

# 2. 读取图像
image_path = sys.argv[1] if len(sys.argv) > 1 else "test.jpg"
image = Image.open(image_path)

# 3. 执行OCR
inputs = processor(text="<OCR>", images=image, return_tensors="pt")
outputs = model.generate(**inputs, max_new_tokens=1024)
text = processor.batch_decode(outputs, skip_special_tokens=False)[0]
result = processor.post_process_generation(text, task="<OCR>", image_size=image.size)

# 4. 显示结果
print("OCR结果:")
print(result['OCR'] if 'OCR' in result else result)

# 5. 保存结果
import os
from pathlib import Path
output_dir = Path("/workspace/output/florence2")
output_dir.mkdir(exist_ok=True)
output_file = output_dir / f"{os.path.basename(image_path).split('.')[0]}_ocr.txt"
with open(output_file, 'w', encoding='utf-8') as f:
    f.write(result['OCR'] if 'OCR' in result else str(result))
print(f"\n结果已保存到: {output_file}")

# ===========================================================
# 以下是一些其他常用功能的示例
# ===========================================================

def test_all_features(image_path):
    """测试Florence-2的各种功能"""
    from transformers import AutoProcessor, AutoModelForCausalLM
    from PIL import Image
    import torch
    
    # 加载模型
    device = "cuda" if torch.cuda.is_available() else "cpu"
    model = AutoModelForCausalLM.from_pretrained(
        "microsoft/Florence-2-large",
        torch_dtype=torch.float16 if torch.cuda.is_available() else torch.float32,
        trust_remote_code=True
    ).to(device)
    processor = AutoProcessor.from_pretrained("microsoft/Florence-2-large", trust_remote_code=True)
    
    # 加载图像
    image = Image.open(image_path)
    
    # 定义所有任务
    tasks = {
        "OCR文字识别": "<OCR>",
        "图像描述": "<CAPTION>",
        "详细描述": "<DETAILED_CAPTION>",
        "目标检测": "<OD>",
        "带区域的OCR": "<OCR_WITH_REGION>",
        "密集区域描述": "<DENSE_REGION_CAPTION>",
    }
    
    print(f"测试图像: {image_path}")
    print("=" * 60)
    
    # 测试每个任务
    for task_name, prompt in tasks.items():
        print(f"\n{task_name}:")
        print("-" * 40)
        
        # 处理
        inputs = processor(text=prompt, images=image, return_tensors="pt").to(device)
        generated_ids = model.generate(
            input_ids=inputs["input_ids"],
            pixel_values=inputs["pixel_values"],
            max_new_tokens=1024,
            do_sample=False,
            num_beams=3
        )
        
        # 解码
        generated_text = processor.batch_decode(generated_ids, skip_special_tokens=False)[0]
        parsed_answer = processor.post_process_generation(
            generated_text,
            task=prompt,
            image_size=(image.width, image.height)
        )
        
        # 显示结果
        if isinstance(parsed_answer, dict):
            for key, value in parsed_answer.items():
                if isinstance(value, str):
                    # 文本结果
                    preview = value[:200] + "..." if len(value) > 200 else value
                    print(f"{key}: {preview}")
                elif isinstance(value, dict):
                    # 结构化结果（如检测框）
                    if 'bboxes' in value:
                        print(f"检测到 {len(value['bboxes'])} 个对象")
                    elif 'quad_boxes' in value:
                        print(f"检测到 {len(value['quad_boxes'])} 个文本区域")
                    else:
                        print(f"{key}: {value}")
                elif isinstance(value, list):
                    print(f"{key}: {len(value)} 项")
        else:
            print(str(parsed_answer)[:200])

def visual_qa_demo(image_path):
    """视觉问答演示"""
    from transformers import AutoProcessor, AutoModelForCausalLM
    from PIL import Image
    
    # 加载模型
    model = AutoModelForCausalLM.from_pretrained("microsoft/Florence-2-large", trust_remote_code=True)
    processor = AutoProcessor.from_pretrained("microsoft/Florence-2-large", trust_remote_code=True)
    
    # 加载图像
    image = Image.open(image_path)
    
    print(f"📸 图像: {image_path}")
    print("输入问题 (输入 'quit' 退出):\n")
    
    while True:
        question = input("❓ 问题: ")
        if question.lower() == 'quit':
            break
        
        # VQA处理
        prompt = f"<VQA> {question}"
        inputs = processor(text=prompt, images=image, return_tensors="pt")
        outputs = model.generate(**inputs, max_new_tokens=256)
        text = processor.batch_decode(outputs, skip_special_tokens=False)[0]
        answer = processor.post_process_generation(text, task=prompt, image_size=image.size)
        
        # 显示答案
        if isinstance(answer, dict) and 'VQA' in answer:
            print(f"💡 答案: {answer['VQA']}\n")
        else:
            print(f"💡 答案: {answer}\n")

# ===========================================================
# 批量OCR示例
# ===========================================================

def batch_ocr(folder_path):
    """批量OCR处理"""
    from pathlib import Path
    from transformers import AutoProcessor, AutoModelForCausalLM
    from PIL import Image
    
    # 加载模型
    model = AutoModelForCausalLM.from_pretrained("microsoft/Florence-2-large", trust_remote_code=True)
    processor = AutoProcessor.from_pretrained("microsoft/Florence-2-large", trust_remote_code=True)
    
    # 查找所有图像
    folder = Path(folder_path)
    images = list(folder.glob("*.jpg")) + list(folder.glob("*.png"))
    
    print(f"找到 {len(images)} 个图像")
    
    # 处理每个图像
    for img_path in images:
        print(f"\n处理: {img_path.name}")
        
        # OCR
        image = Image.open(img_path)
        inputs = processor(text="<OCR>", images=image, return_tensors="pt")
        outputs = model.generate(**inputs, max_new_tokens=1024)
        text = processor.batch_decode(outputs, skip_special_tokens=False)[0]
        result = processor.post_process_generation(text, task="<OCR>", image_size=image.size)
        
        # 保存结果
        import os
        ocr_text = result.get('OCR', str(result))
        output_dir = Path("/workspace/output/florence2")
        output_dir.mkdir(exist_ok=True)
        output_file = output_dir / f"{img_path.stem}.txt"
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(ocr_text)
        
        print(f"✅ 保存到: {output_file}")
        print(f"   字符数: {len(ocr_text)}")

if __name__ == "__main__":
    import sys
    
    if len(sys.argv) > 1 and sys.argv[1] == "--demo":
        # 运行完整演示
        if len(sys.argv) > 2:
            test_all_features(sys.argv[2])
        else:
            print("用法: python florence2_quick.py --demo <图像路径>")
    elif len(sys.argv) > 1 and sys.argv[1] == "--vqa":
        # 运行VQA演示
        if len(sys.argv) > 2:
            visual_qa_demo(sys.argv[2])
        else:
            print("用法: python florence2_quick.py --vqa <图像路径>")
    elif len(sys.argv) > 1 and sys.argv[1] == "--batch":
        # 批量处理
        if len(sys.argv) > 2:
            batch_ocr(sys.argv[2])
        else:
            print("用法: python florence2_quick.py --batch <文件夹路径>")
    else:
        # 默认：简单OCR
        print("""
Florence-2 快速测试工具
========================
用法:
  python florence2_quick.py <图像>           # OCR识别
  python florence2_quick.py --demo <图像>    # 测试所有功能
  python florence2_quick.py --vqa <图像>     # 视觉问答
  python florence2_quick.py --batch <文件夹>  # 批量OCR
        """)
