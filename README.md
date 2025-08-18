# Document OCR Comparison

这个项目比较了两种文档 OCR 技术：Nougat 和 Donut，用于处理各种类型的文档图像。通过对比分析，可以了解不同模型在各种文档类型上的表现。

## 项目特点

- 支持多种OCR模型（Nougat、Donut）的对比测试
- 提供多种预设模式，针对不同类型的文档优化
- 自动生成对比报告和性能分析
- 批量处理功能，支持处理整个文件夹的图像
- 详细的进度显示和结果可视化

## 项目结构

```
.
├── README.md                      # 项目概述
├── ENV_SETUP_GUIDE.md             # 环境设置指南
├── PROJECT_STRUCTURE.md           # 项目结构说明
├── requirements_donut.txt         # Donut 环境依赖
├── setup_env.sh                   # 环境设置脚本
├── analyze_donut_results.py       # Donut 结果分析脚本
├── data/                          # 数据目录
│   ├── README.md                  # 数据说明文档
│   └── samples/                   # 样本图像
│       ├── ocr_test/              # OCR测试图像
│       └── general_images/        # 通用图像
├── experiments/                   # 实验代码
│   ├── donut/                     # Donut 相关代码
│   │   └── donut_batch_test_auto.py  # Donut 批量测试脚本
│   └── nougat/                    # Nougat 相关代码
│       └── nougat_advanced_demo.py   # Nougat 高级演示脚本
└── output/                        # 输出结果目录
    ├── README.md                  # 输出说明文档
    ├── donut/                     # Donut 处理结果
    └── nougat/                    # Nougat 处理结果
```

## 模型介绍

### Nougat

Nougat (Neural Optical Understanding for Academic Documents) 是专为学术文档设计的 OCR 模型，特别擅长处理包含数学公式、表格和复杂排版的内容。

#### 预设模式

- `fast` - 快速模式，牺牲质量换取速度
- `balanced` - 平衡模式，速度和质量的平衡
- `quality` - 高质量模式，最佳识别质量
- `math` - 数学文档模式，优化数学公式识别
- `table` - 表格文档模式，优化表格识别

### Donut

Donut (Document Understanding Transformer) 是一个 OCR-free 的文档理解模型，可以直接从图像中提取结构化信息。

#### 预设模式

- `fast_draft` - 快速草稿模式
- `balanced_beam` - 平衡的束搜索模式
- `long_page_strict` - 长页面严格模式
- `formula_friendly` - 公式友好模式
- `table_markdown` - 表格 Markdown 模式
- `page_summary` - 页面摘要模式
- `universal_doc` - 通用文档模式
- `router_probe` - 路由探针模式
- `eq_compact` - 紧凑公式模式
- `table_strict_md` - 严格表格 Markdown 模式
- `wide_table_md` - 宽表格 Markdown 模式
- `figure_bullets` - 图形要点模式

## 快速开始

### 环境设置

```bash
# 运行环境设置脚本
./setup_env.sh

# 或手动创建环境
uv venv donut
source donut/bin/activate
uv pip install -r requirements_donut.txt
```

### 运行 Donut

```bash
# 处理单个图像
python experiments/donut/donut_batch_test_auto.py --no-fp16 data/samples/ocr_test/1.jpg

# 批量处理
python experiments/donut/donut_batch_test_auto.py --no-fp16 --batch data/samples/ocr_test

# 自动路由模式
python experiments/donut/donut_batch_test_auto.py --no-fp16 --auto_route data/samples/ocr_test/1.jpg
```

### 运行 Nougat

```bash
# 处理单个图像
python experiments/nougat/nougat_advanced_demo.py data/samples/ocr_test/1.jpg

# 批量处理并对比所有预设
python experiments/nougat/nougat_advanced_demo.py --batch data/samples/ocr_test --compare

# 使用特定预设
python experiments/nougat/nougat_advanced_demo.py --preset math data/samples/ocr_test/5.jpg
```

### 分析结果

```bash
# 分析Donut结果
python analyze_donut_results.py
```

## 结果分析

根据我们的测试，不同模型在不同类型的文档上表现各异：

- **Nougat** 在处理学术文档和数学公式方面表现优异
- **Donut** 的 `universal_doc` 预设在大多数图片上产生了最长的文本输出
- **Donut** 的 `router_probe` 预设在效率方面表现最佳

## 贡献

欢迎提交问题和改进建议！

## 许可证

本项目采用 MIT 许可证。