# Nougat OCR 实验

本目录包含 Nougat 模型的 OCR 实验代码。

## nougat_advanced_demo.py

`nougat_advanced_demo.py` 是主要的实验脚本，支持多种预设模式和批量处理功能。

## 特点

- **多种预设模式**：提供针对不同文档类型优化的预设
- **对比功能**：可以对同一图像使用不同预设进行对比
- **批量处理**：支持处理整个文件夹的图像
- **进度显示**：显示处理进度和预计剩余时间
- **结果可视化**：生成对比 Markdown 报告

## 安装依赖

```bash
# 创建虚拟环境
uv venv nougat
source nougat/bin/activate

# 安装依赖
uv pip install torch torchvision pillow transformers accelerate nltk python-Levenshtein
```

## 快速开始

### 处理单个图像

```bash
# 使用默认预设（balanced）
python experiments/nougat/nougat_advanced_demo.py data/samples/ocr_test/1.jpg

# 使用特定预设
python experiments/nougat/nougat_advanced_demo.py --preset math data/samples/ocr_test/5.jpg
```

### 对比不同预设

```bash
# 对同一图像使用所有预设进行对比
python experiments/nougat/nougat_advanced_demo.py data/samples/ocr_test/1.jpg --compare
```

### 批量处理

```bash
# 批量处理并对比所有预设
python experiments/nougat/nougat_advanced_demo.py --batch data/samples/ocr_test --compare
```

## 预设模式

- `fast` - 快速模式，牺牲质量换取速度
- `balanced` - 平衡模式，速度和质量的平衡（默认）
- `quality` - 高质量模式，最佳识别质量
- `math` - 数学文档模式，优化数学公式识别
- `table` - 表格文档模式，优化表格识别

## 输出结果

处理结果将保存在 `output/nougat/` 目录下：

- 单个图像处理：生成 `<图像名>_<预设>.md` 文件
- 对比模式：生成 `<图像名>_comparison.md` 文件，包含所有预设的结果和性能对比
- 批量处理：生成 `processing_summary.json` 文件，包含所有图像的处理摘要

## 高级选项

```bash
# 显示所有可用选项
python experiments/nougat/nougat_advanced_demo.py --help
```

主要选项包括：

- `--preset`: 选择预设模式
- `--compare`: 启用对比模式
- `--batch`: 批量处理模式
- `--max-length`: 设置最大输出长度
- `--num-beams`: 设置 Beam 搜索数量
- `--temperature`: 设置温度参数
