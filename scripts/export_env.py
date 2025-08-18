#!/usr/bin/env python3
"""
导出当前环境配置，方便在新服务器上重建环境。
该脚本会创建必要的配置文件，包括requirements.txt和环境信息。
"""
import os
import sys
import json
import subprocess
import platform
from datetime import datetime


def run_cmd(cmd):
    """
    运行系统命令并返回输出。
    
    Args:
        cmd (str): 要运行的命令
        
    Returns:
        str: 命令的输出
    """
    try:
        result = subprocess.run(
            cmd, 
            shell=True, 
            check=True, 
            stdout=subprocess.PIPE, 
            stderr=subprocess.PIPE,
            text=True
        )
        return result.stdout.strip()
    except subprocess.CalledProcessError as e:
        print(f"命令执行失败: {cmd}")
        print(f"错误: {e.stderr}")
        return ""


def get_system_info():
    """
    获取系统信息。
    
    Returns:
        dict: 系统信息字典
    """
    info = {
        "os": platform.system(),
        "os_release": platform.release(),
        "os_version": platform.version(),
        "architecture": platform.machine(),
        "processor": platform.processor(),
        "python_version": platform.python_version(),
        "python_implementation": platform.python_implementation(),
        "python_compiler": platform.python_compiler(),
        "python_path": sys.executable,
    }
    
    # 获取CUDA信息
    try:
        import torch
        info["cuda_available"] = torch.cuda.is_available()
        if info["cuda_available"]:
            info["cuda_version"] = torch.version.cuda
            info["cudnn_version"] = torch.backends.cudnn.version()
            info["gpu_name"] = torch.cuda.get_device_name(0)
            info["gpu_count"] = torch.cuda.device_count()
            info["gpu_memory"] = f"{torch.cuda.get_device_properties(0).total_memory / 1e9:.2f} GB"
    except ImportError:
        info["cuda_available"] = False
    
    return info


def export_pip_packages(output_dir="docs"):
    """
    导出当前环境中的pip包列表。
    
    Args:
        output_dir (str): 输出目录路径
    """
    os.makedirs(output_dir, exist_ok=True)
    output_file = os.path.join(output_dir, "requirements.txt")
    print(f"导出pip包到 {output_file}...")
    
    # 检查是否安装了uv
    uv_installed = os.system("command -v uv > /dev/null 2>&1") == 0
    
    if uv_installed:
        # 使用uv导出依赖
        cmd = f"uv pip freeze > {output_file}"
        os.system(cmd)
        print(f"已使用 uv 导出 {output_file}")
        
        # 同时更新锁定文件
        print("更新 uv.lock 文件...")
        os.system("uv lock")
        print("已更新 uv.lock 文件")
    else:
        # 使用传统pip导出
        cmd = f"{sys.executable} -m pip freeze > {output_file}"
        os.system(cmd)
        print(f"已使用 pip 导出 {output_file} (未安装 uv)")


def create_setup_script():
    """
    创建环境重建脚本。
    """
    script_content = """#!/bin/bash
# 环境重建脚本
# 由 export_env.py 自动生成

echo "开始重建环境..."

# 检查是否安装了uv
if ! command -v uv &> /dev/null; then
    echo "安装uv包管理器..."
    curl -LsSf https://astral.sh/uv/install.sh | sh
    source ~/.bashrc
fi

# 创建虚拟环境
ENV_NAME="florence"
echo "创建虚拟环境: $ENV_NAME"
uv venv $ENV_NAME

# 激活环境
source $ENV_NAME/bin/activate

# 安装依赖
echo "安装Python依赖..."

# 检查是否存在锁定文件
if [ -f "uv.lock" ]; then
    echo "使用锁定文件安装依赖..."
    uv pip sync
else
    echo "使用requirements.txt安装依赖..."
    uv pip install -r requirements.txt
fi

echo "环境重建完成！"
"""
    
    with open("setup_env.sh", "w") as f:
        f.write(script_content)
    
    os.chmod("setup_env.sh", 0o755)  # 添加执行权限
    print("已创建环境重建脚本: setup_env.sh")


def export_environment_info(output_dir="docs"):
    """
    导出环境信息到JSON文件。
    """
    os.makedirs(output_dir, exist_ok=True)
    output_file = os.path.join(output_dir, "environment_info.json")
    info = {
        "system_info": get_system_info(),
        "export_date": datetime.now().isoformat(),
    }
    
    # 获取已安装的包
    try:
        import pkg_resources
        packages = []
        for pkg in pkg_resources.working_set:
            packages.append({
                "name": pkg.key,
                "version": pkg.version
            })
        info["installed_packages"] = packages
    except Exception as e:
        print(f"无法获取已安装的包信息: {e}")
    
    with open(output_file, "w") as f:
        json.dump(info, f, indent=2)
    
    print(f"已导出环境信息到 {output_file}")


def create_readme():
    """
    创建README文件。
    """
    readme_content = """# Florence 环境

这个目录包含了Florence模型推理环境的配置文件和脚本。

## 文件说明

- `docs/requirements.txt`: Python依赖包列表
- `uv.lock`: uv 锁定文件，确保精确的依赖版本
- `pyproject.toml`: 项目配置文件，包含依赖定义
- `docs/environment_info.json`: 环境详细信息
- `setup_env.sh`: 环境重建脚本
- `src/test.py`: 测试脚本
- `src/test_env.py`: 环境测试脚本

## 如何重建环境

1. 确保你有一个干净的Linux环境
2. 运行以下命令:

```bash
# 添加执行权限
chmod +x setup_env.sh

# 运行重建脚本
./setup_env.sh
```

3. 测试环境:

```bash
# 激活环境
source florence/bin/activate

# 运行测试脚本
python test_env.py
```

## 使用 uv 进行版本管理

本项目使用 [uv](https://github.com/astral-sh/uv) 进行依赖管理，相比传统的 pip，它具有以下优势：

- 更快的包安装速度
- 精确的版本锁定
- 更好的依赖解析
- 与 pyproject.toml 无缝集成

### 常用命令

```bash
# 安装依赖
uv pip install <package>

# 从 pyproject.toml 安装依赖
uv pip install -e .

# 同步环境（使用锁定文件）
uv pip sync

# 更新锁定文件
uv lock

# 导出依赖
uv pip freeze > docs/requirements.txt
```

## 注意事项

- 此环境需要CUDA支持以获得最佳性能
- 如果你遇到任何问题，请查看 `environment_info.json` 了解原始环境的详细信息
- 优先使用 uv.lock 文件进行环境重建，确保版本一致性
"""
    
    with open("README.md", "w") as f:
        f.write(readme_content)
    
    print("已创建README.md")


def main():
    """
    主函数。
    """
    print("开始导出环境配置...")
    
    # 导出pip包
    export_pip_packages(output_dir="docs")
    
    # 创建环境重建脚本
    create_setup_script()
    
    # 导出环境信息
    export_environment_info(output_dir="docs")
    
    # 创建README
    create_readme()
    
    print("环境配置导出完成！")
    print("现在你可以将整个workspace目录复制到新服务器，然后运行 setup_env.sh 重建环境。")


if __name__ == "__main__":
    main()
