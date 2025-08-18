#!/bin/bash
# 环境设置脚本

echo "===== 开始设置环境 ====="

# 检查 uv 是否已安装
if ! command -v uv &> /dev/null; then
    echo "错误: 未找到 uv 工具。请先安装 uv: https://github.com/astral-sh/uv"
    exit 1
fi

# 创建并设置 Donut 环境
echo "===== 设置 Donut 环境 ====="
uv venv donut
source donut/bin/activate
uv pip install -r requirements_donut.txt
echo "Donut 环境设置完成"

# 创建输出目录
mkdir -p output/donut_results

echo "===== 环境设置完成 ====="
echo "使用以下命令激活 Donut 环境:"
echo "source donut/bin/activate"
echo ""
echo "然后运行:"
echo "python experiments/donut/donut_batch_test_auto.py --no-fp16"
