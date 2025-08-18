# 环境设置指南

本文档提供了使用 `uv` 工具复现项目环境的详细步骤。

## 环境要求

- Python 3.11+
- uv 工具 (https://github.com/astral-sh/uv)

## Donut 环境设置

Donut 是一个 OCR-free 的文档理解模型，用于从图像中提取结构化信息。

```bash
# 创建虚拟环境
uv venv donut

# 激活环境
source donut/bin/activate  # Linux/macOS
# 或
# donut\Scripts\activate  # Windows

# 从 requirements 文件安装依赖
uv pip install -r requirements_donut.txt
```

### 关键依赖

Donut 环境包含以下关键依赖：
- transformers==4.55.2
- torch==2.8.0
- torchvision==0.23.0
- sentencepiece==0.2.1
- protobuf==6.32.0
- pandas==2.3.1

## Nougat 环境设置

Nougat 是一个专为学术文档设计的 OCR 模型，特别擅长处理包含数学公式、表格和复杂排版的内容。

```bash
# 创建虚拟环境
uv venv nougat

# 激活环境
source nougat/bin/activate  # Linux/macOS
# 或
# nougat\Scripts\activate  # Windows

# 安装依赖
uv pip install torch torchvision pillow transformers accelerate nltk python-Levenshtein
```

## 验证环境

安装完成后，可以运行以下命令验证环境是否正确设置：

```bash
# Donut 环境验证
source donut/bin/activate
python -c "import torch; import transformers; import pandas; print('Donut 环境验证成功')"

# Nougat 环境验证
source nougat/bin/activate
python -c "import torch; import transformers; import nltk; print('Nougat 环境验证成功')"
```

## 运行项目

设置好环境后，可以运行以下命令：

### Donut

```bash
source donut/bin/activate
python experiments/donut/donut_batch_test_auto.py --no-fp16
```

### Nougat

```bash
source nougat/bin/activate
python experiments/nougat/nougat_advanced_demo.py --batch data/pdf_ocr_samples --compare
```

### 分析结果

```bash
source donut/bin/activate
python analyze_donut_results.py
```

## 故障排除

如果遇到模块导入错误，请确保已激活正确的虚拟环境，并且所有依赖都已正确安装。

对于 Donut 环境，可能需要额外安装以下依赖：
```bash
uv pip install sentencepiece protobuf
```

对于 Nougat 环境，可能需要额外安装以下依赖：
```bash
uv pip install nltk python-Levenshtein
```
