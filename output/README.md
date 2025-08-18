# 输出目录

本目录包含各种OCR模型处理结果的输出文件。

## 目录结构

- `nougat/`: Nougat模型的处理结果
  - `*_comparison.md`: 不同预设模式的对比结果
  - `processing_summary.json`: 处理摘要信息

- `donut/`: Donut模型的处理结果
  - `*.json`: 每个图像的处理结果
  - `capabilities.json`: 模型能力概览
  - `summary.csv`: 处理结果摘要

## 结果格式

### Nougat结果

Nougat模型的结果以Markdown文件形式保存，每个文件包含：
- 原始图像信息
- 不同预设模式的处理结果
- 处理时间和性能统计

### Donut结果

Donut模型的结果以JSON文件形式保存，每个文件包含：
- 图像路径
- 处理时间戳
- 各种预设模式的处理结果
- 处理时间和输出文本

## 使用说明

可以使用以下命令分析处理结果：

```bash
# 分析Donut结果
python analyze_donut_results.py
```
