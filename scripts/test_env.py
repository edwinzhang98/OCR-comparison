"""
验证 Florence 环境配置的简化测试脚本
"""
import os
import torch
import numpy as np
from PIL import Image
import requests
from transformers import AutoConfig

# 打印环境信息
print("=== Florence 环境测试 ===")
print(f"Python 版本: {os.sys.version}")
print(f"PyTorch 版本: {torch.__version__}")
print(f"NumPy 版本: {np.__version__}")
print(f"CUDA 是否可用: {torch.cuda.is_available()}")
if torch.cuda.is_available():
    print(f"CUDA 版本: {torch.version.cuda}")
    print(f"GPU 型号: {torch.cuda.get_device_name(0)}")
    print(f"GPU 显存: {torch.cuda.get_device_properties(0).total_memory / 1e9:.2f} GB")

# 测试 PIL
print("\n=== 测试 PIL ===")
try:
    img = Image.new('RGB', (100, 100), color='red')
    print("PIL 图像创建成功")
except Exception as e:
    print(f"PIL 测试失败: {e}")

# 测试 requests
print("\n=== 测试 requests ===")
try:
    response = requests.get("https://www.google.com", timeout=5)
    print(f"网络请求成功，状态码: {response.status_code}")
except Exception as e:
    print(f"网络请求失败: {e}")

# 测试 transformers
print("\n=== 测试 transformers ===")
try:
    # 只获取配置，不下载模型
    config = AutoConfig.from_pretrained("gpt2", local_files_only=False)
    print("Transformers 配置加载成功")
    print(f"模型类型: {config.model_type}")
except Exception as e:
    print(f"Transformers 测试失败: {e}")

print("\n环境测试完成！")
