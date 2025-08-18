# 项目结构

```
.
├── README.md                      # 项目概述
├── ENV_SETUP_GUIDE.md             # 环境设置指南
├── PROJECT_STRUCTURE.md           # 本文件，项目结构说明
├── requirements_donut.txt         # Donut 环境依赖
├── setup_env.sh                   # 环境设置脚本
├── analyze_donut_results.py       # Donut 结果分析脚本
├── data/
│   └── pdf_ocr_samples/           # 测试图片样本
├── experiments/
│   ├── donut/                     # Donut 相关代码
│   │   └── donut_batch_test_auto.py  # Donut 批量测试脚本
│   └── nougat/                    # Nougat 相关代码
│       └── nougat_advanced_demo.py   # Nougat 高级演示脚本
└── output/                        # 输出结果目录
    ├── donut_results/             # Donut 处理结果
    └── facebook_nougat-base/      # Nougat 处理结果
```

## 关键文件说明

### 核心脚本

- **donut_batch_test_auto.py**: Donut 模型批量处理图片的脚本，支持多种预设模式和自动路由功能
- **nougat_advanced_demo.py**: Nougat 模型的高级演示脚本，支持多种预设模式
- **analyze_donut_results.py**: 分析 Donut 处理结果，找出每个图片最适合的预设模式

### 环境相关

- **requirements_donut.txt**: Donut 环境的完整依赖列表
- **setup_env.sh**: 快速设置环境的脚本
- **ENV_SETUP_GUIDE.md**: 详细的环境设置指南

### 输出目录

- **output/donut_results/**: Donut 处理结果，每个图片对应一个 JSON 文件
- **output/facebook_nougat-base/**: Nougat 处理结果，每个图片对应一个 Markdown 文件

## 数据流

1. 从 `data/pdf_ocr_samples/` 读取图片
2. 使用 Donut 或 Nougat 模型处理图片
3. 结果保存到 `output/` 目录
4. 使用 `analyze_donut_results.py` 分析结果
