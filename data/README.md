# 数据目录

本目录包含项目使用的各种图像和数据文件。

## 目录结构

- `samples/`: 样本图像
  - `ocr_test/`: OCR测试用的文档图像，包含文字、表格、公式等
  - `general_images/`: 通用图像，用于测试模型的通用识别能力

## 数据来源

- `ocr_test/`: 包含18张测试图像，用于评估OCR模型性能
- `general_images/`: 包含通用图像，用于测试和演示

## 使用说明

在运行OCR脚本时，可以使用这些样本图像进行测试：

```bash
# 使用Nougat处理OCR测试图像
python experiments/nougat/nougat_advanced_demo.py data/samples/ocr_test/1.jpg

# 使用Donut处理OCR测试图像
python experiments/donut/donut_batch_test_auto.py --no-fp16 data/samples/ocr_test/1.jpg
```

## 批量处理

可以使用以下命令批量处理所有OCR测试图像：

```bash
# 使用Nougat批量处理
python experiments/nougat/nougat_advanced_demo.py --batch data/samples/ocr_test --compare

# 使用Donut批量处理
python experiments/donut/donut_batch_test_auto.py --no-fp16 --batch data/samples/ocr_test
```

结果将保存在 `output/` 目录中。
