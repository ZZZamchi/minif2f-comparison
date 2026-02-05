#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
从 Hugging Face 下载 Tonic/MiniF2F 数据集
"""

import json
import sys
from pathlib import Path

try:
    from datasets import load_dataset
    DATASETS_AVAILABLE = True
except ImportError:
    DATASETS_AVAILABLE = False
    print("[ERROR] datasets 库未安装，请运行: pip install datasets")

# 设置输出编码（Windows 兼容）
if sys.platform == 'win32':
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')


def download_tonic_minif2f():
    """从 Hugging Face 下载 Tonic/MiniF2F 数据集"""
    if not DATASETS_AVAILABLE:
        print("[ERROR] 无法下载：datasets 库未安装")
        return False
    
    output_dir = Path("minif2f_v1")
    output_dir.mkdir(exist_ok=True)
    
    print("=" * 60)
    print("下载 Tonic/MiniF2F 数据集")
    print("=" * 60)
    print()
    
    try:
        print("正在从 Hugging Face 加载数据集...")
        dataset = load_dataset("Tonic/MiniF2F")
        
        print(f"[OK] 数据集加载成功")
        print(f"  分割: {list(dataset.keys())}")
        
        # 处理数据
        all_data = []
        
        for split_name, split_data in dataset.items():
            print(f"\n处理分割: {split_name} ({len(split_data)} 条记录)")
            
            for item in split_data:
                # 转换字段名以匹配我们的格式
                converted_item = {
                    "name": item.get("name", ""),
                    "split": item.get("split", split_name),
                    "informal_statement": item.get("informal_prefix", ""),
                    "formal_statement": item.get("formal_statement", ""),
                    "header": item.get("header", ""),
                    "informal_proof": "",
                    "formal_proof": "",
                    "goal": item.get("goal", "")  # 保留 goal 字段
                }
                all_data.append(converted_item)
        
        # 保存为 JSON
        output_path = output_dir / "miniF2F_v1.json"
        with open(output_path, 'w', encoding='utf-8') as f:
            json.dump(all_data, f, ensure_ascii=False, indent=2)
        
        print(f"\n[OK] 数据集已保存到: {output_path}")
        print(f"[OK] 总计: {len(all_data)} 条记录")
        
        # 按 split 统计
        splits = {}
        for item in all_data:
            split = item.get("split", "unknown")
            splits[split] = splits.get(split, 0) + 1
        
        print(f"\n按分割统计:")
        for split, count in splits.items():
            print(f"  {split}: {count} 条")
        
        return True
        
    except Exception as e:
        print(f"[ERROR] 下载失败: {e}")
        import traceback
        traceback.print_exc()
        return False


if __name__ == "__main__":
    if download_tonic_minif2f():
        print()
        print("=" * 60)
        print("下载完成！")
        print("=" * 60)
    else:
        print()
        print("=" * 60)
        print("下载失败")
        print("=" * 60)
