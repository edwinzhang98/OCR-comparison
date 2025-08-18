# 归档实验

本目录包含不再积极维护的实验代码，但可能在未来有用。

## Florence2

`florence2/` 目录包含使用 Microsoft Florence-2 多模态模型进行 OCR 和图像理解的实验脚本。

### 脚本说明

- `florence2_ocr_script.py` - 专门用于 OCR 任务的脚本，支持文档文本提取、表格识别等
- `florence2_quick.py` - 简化的 Florence-2 使用示例，只需几行代码即可运行
- `florence2_test_script.py` - 全面的测试脚本，支持多种视觉任务，包括 OCR、目标检测、图像描述等

### 使用方法

这些脚本需要安装额外的依赖：

```bash
pip install transformers torch pillow pandas
```

基本用法：

```bash
python experiments/archive/florence2/florence2_ocr_script.py <图像路径>
```

更多选项请参考各脚本中的帮助文档。
