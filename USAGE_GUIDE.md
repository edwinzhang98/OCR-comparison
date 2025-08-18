# 使用指南

本文档提供了详细的使用说明，帮助您充分利用这个OCR比较项目。

## 目录

1. [环境设置](#环境设置)
2. [Nougat模型使用](#nougat模型使用)
3. [Donut模型使用](#donut模型使用)
4. [结果分析](#结果分析)
5. [常见问题](#常见问题)

## 环境设置

### 使用设置脚本

最简单的方式是使用提供的设置脚本：

```bash
./setup_env.sh
```

这将创建一个名为`donut`的虚拟环境并安装所有必要的依赖。

### 手动设置

如果您想手动设置环境，可以按照以下步骤操作：

```bash
# 创建虚拟环境
uv venv donut

# 激活环境
source donut/bin/activate  # Linux/macOS
# 或
# donut\Scripts\activate  # Windows

# 安装依赖
uv pip install -r requirements_donut.txt
```

## Nougat模型使用

Nougat是一个专为学术文档设计的OCR模型，特别擅长处理包含数学公式、表格和复杂排版的内容。

### 基本用法

```bash
# 处理单个图像
python experiments/nougat/nougat_advanced_demo.py data/samples/ocr_test/1.jpg

# 使用特定预设模式
python experiments/nougat/nougat_advanced_demo.py --preset math data/samples/ocr_test/5.jpg
```

### 预设模式

Nougat提供了多种预设模式，针对不同类型的文档优化：

- `fast`: 快速模式，牺牲质量换取速度
- `balanced`: 平衡模式，速度和质量的平衡（默认）
- `quality`: 高质量模式，最佳识别质量
- `math`: 数学文档模式，优化数学公式识别
- `table`: 表格文档模式，优化表格识别

### 批量处理

```bash
# 批量处理并对比所有预设
python experiments/nougat/nougat_advanced_demo.py --batch data/samples/ocr_test --compare
```

这将处理指定目录中的所有图像，并为每个图像生成一个包含所有预设模式结果的对比报告。

### 高级参数

Nougat脚本支持多种高级参数：

```bash
python experiments/nougat/nougat_advanced_demo.py --help
```

## Donut模型使用

Donut是一个OCR-free的文档理解模型，可以直接从图像中提取结构化信息。

### 基本用法

```bash
# 处理单个图像
python experiments/donut/donut_batch_test_auto.py --no-fp16 data/samples/ocr_test/1.jpg
```

注意：由于兼容性问题，需要添加`--no-fp16`参数以避免精度错误。

### 批量处理

```bash
# 批量处理
python experiments/donut/donut_batch_test_auto.py --no-fp16 --batch data/samples/ocr_test
```

### 自动路由模式

Donut提供了一个智能的自动路由模式，可以根据图像内容自动选择最合适的预设：

```bash
python experiments/donut/donut_batch_test_auto.py --no-fp16 --auto_route data/samples/ocr_test/1.jpg
```

### 预设模式

Donut提供了多种预设模式：

- `fast_draft`: 快速草稿模式
- `balanced_beam`: 平衡的束搜索模式
- `long_page_strict`: 长页面严格模式
- `formula_friendly`: 公式友好模式
- `table_markdown`: 表格Markdown模式
- `page_summary`: 页面摘要模式
- `universal_doc`: 通用文档模式（最全能）
- `router_probe`: 路由探针模式（效率最高）
- `eq_compact`: 紧凑公式模式
- `table_strict_md`: 严格表格Markdown模式
- `wide_table_md`: 宽表格Markdown模式
- `figure_bullets`: 图形要点模式

## 结果分析

### 分析Donut结果

```bash
python analyze_donut_results.py
```

这将分析`output/donut/`目录中的所有结果文件，并生成一个摘要报告，显示每个图像的最佳预设模式。

### 查看对比报告

Nougat的对比报告保存在`output/nougat/`目录中，格式为`*_comparison.md`。这些报告包含了不同预设模式的处理结果、处理时间和性能统计。

## 常见问题

### 1. 模型下载失败

如果模型下载失败，可以尝试手动下载并放置在正确的位置：

- Nougat模型：`~/.cache/huggingface/hub/models--facebook--nougat-base/`
- Donut模型：`~/.cache/huggingface/hub/models--naver-clova-ix--donut-base/`

### 2. 内存不足错误

如果遇到内存不足错误，可以尝试以下方法：

- 使用`--limit`参数限制处理的图像数量
- 使用较小的模型（例如base版本而不是large版本）
- 减小批处理大小

### 3. 处理速度慢

处理速度受多种因素影响，包括：

- 硬件配置（GPU加速可显著提高速度）
- 图像大小和复杂度
- 选择的预设模式

使用`fast`或`fast_draft`预设可以提高处理速度，但可能会降低识别质量。
