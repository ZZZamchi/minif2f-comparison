#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""下载 PutnamBench 和 ProofNet 数据集"""

import subprocess
import os
import sys
import json
import shutil
import io

# 设置输出编码（Windows 兼容）
if sys.platform == 'win32':
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

def run_command(cmd, cwd=None):
    """运行命令并返回结果"""
    try:
        result = subprocess.run(cmd, shell=True, cwd=cwd, capture_output=True, text=True, encoding='utf-8')
        return result.returncode == 0, result.stdout, result.stderr
    except Exception as e:
        return False, "", str(e)

def download_putnambench():
    """下载 PutnamBench 数据"""
    print("Downloading PutnamBench...")
    putnambench_dir = "benchmarks/putnambench"
    
    # 克隆仓库
    if not os.path.exists(putnambench_dir):
        success, _, _ = run_command(f"git clone --depth 1 https://github.com/trishullab/PutnamBench.git {putnambench_dir}")
        if success:
            print("[OK] PutnamBench downloaded")
            # 删除 .git 目录以节省空间
            git_dir = os.path.join(putnambench_dir, ".git")
            if os.path.exists(git_dir):
                shutil.rmtree(git_dir)
        else:
            print("[FAIL] PutnamBench download failed")
    else:
        print("[OK] PutnamBench already exists")

def download_proofnet():
    """下载 ProofNet 数据"""
    print("Downloading ProofNet...")
    proofnet_dir = "benchmarks/proofnet"
    
    # 克隆仓库
    if not os.path.exists(proofnet_dir):
        success, _, _ = run_command(f"git clone --depth 1 https://github.com/zhangir-azerbayev/proofnet.git {proofnet_dir}")
        if success:
            print("[OK] ProofNet downloaded")
            # 删除 .git 目录以节省空间
            git_dir = os.path.join(proofnet_dir, ".git")
            if os.path.exists(git_dir):
                shutil.rmtree(git_dir)
        else:
            print("[FAIL] ProofNet download failed")
    else:
        print("[OK] ProofNet already exists")

if __name__ == "__main__":
    os.makedirs("benchmarks", exist_ok=True)
    download_putnambench()
    download_proofnet()
    print("\nAll benchmarks downloaded!")
