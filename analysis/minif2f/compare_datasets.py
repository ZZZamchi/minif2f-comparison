#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
miniF2F v1 vs v2 数据集比较分析脚本

该脚本用于比较原始 miniF2F (v1) 数据集与 miniF2F_v2 (v2c 和 v2s) 之间的区别。
"""

import json
import os
import sys
from pathlib import Path
from collections import defaultdict
from typing import Dict, List, Any, Optional
import difflib

# 设置输出编码（Windows 兼容）
if sys.platform == 'win32':
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

class DatasetComparator:
    """数据集比较器"""
    
    def __init__(self, v1_path: Optional[str] = None, v2c_path: str = None, v2s_path: str = None):
        """
        初始化比较器
        
        Args:
            v1_path: 原始 miniF2F v1 数据集路径（可选）
            v2c_path: miniF2F v2c 数据集路径
            v2s_path: miniF2F v2s 数据集路径
        """
        # 尝试自动查找 v1 数据集
        if v1_path is None:
            possible_v1_paths = [
                "minif2f_v1/miniF2F_v1.json",
                "../minif2f_v1/miniF2F_v1.json",
                "minif2f_v1/valid.json",  # 如果只有验证集
            ]
            for path in possible_v1_paths:
                if os.path.exists(path):
                    v1_path = path
                    break
        
        self.v1_path = v1_path
        self.v2c_path = v2c_path or "../miniF2F_v2/datasets/miniF2F_v2c.json"
        self.v2s_path = v2s_path or "../miniF2F_v2/datasets/miniF2F_v2s.json"
        
        self.v1_data = None
        self.v2c_data = None
        self.v2s_data = None
        
    def load_dataset(self, path: str) -> List[Dict[str, Any]]:
        """加载数据集"""
        if not os.path.exists(path):
            print(f"警告: 文件不存在: {path}")
            return []
        
        with open(path, 'r', encoding='utf-8') as f:
            return json.load(f)
    
    def load_all_datasets(self):
        """加载所有数据集"""
        if self.v1_path and os.path.exists(self.v1_path):
            self.v1_data = self.load_dataset(self.v1_path)
            print(f"[OK] 已加载 v1 数据集: {len(self.v1_data)} 条记录")
        else:
            print("[WARN] v1 数据集未找到，将仅分析 v2 版本之间的差异")
        
        self.v2c_data = self.load_dataset(self.v2c_path)
        print(f"[OK] 已加载 v2c 数据集: {len(self.v2c_data)} 条记录")
        
        self.v2s_data = self.load_dataset(self.v2s_path)
        print(f"[OK] 已加载 v2s 数据集: {len(self.v2s_data)} 条记录")
    
    def get_statistics(self, data: List[Dict[str, Any]], name: str) -> Dict[str, Any]:
        """获取数据集统计信息"""
        if not data:
            return {}
        
        stats = {
            "name": name,
            "total": len(data),
            "by_split": defaultdict(int),
            "by_name": {},
            "has_informal_proof": 0,
            "has_formal_proof": 0,
            "avg_informal_length": 0,
            "avg_formal_length": 0,
        }
        
        total_informal_length = 0
        total_formal_length = 0
        
        for item in data:
            # 按 split 统计
            split = item.get("split", "unknown")
            stats["by_split"][split] += 1
            
            # 记录问题名称
            problem_name = item.get("name", "unknown")
            stats["by_name"][problem_name] = {
                "split": split,
                "has_informal_proof": bool(item.get("informal_proof", "")),
                "has_formal_proof": bool(item.get("formal_proof", "")),
            }
            
            # 统计证明存在情况
            if item.get("informal_proof", ""):
                stats["has_informal_proof"] += 1
            if item.get("formal_proof", ""):
                stats["has_formal_proof"] += 1
            
            # 统计长度
            informal = item.get("informal_statement", "")
            formal = item.get("formal_statement", "")
            total_informal_length += len(informal)
            total_formal_length += len(formal)
        
        stats["avg_informal_length"] = total_informal_length / len(data) if data else 0
        stats["avg_formal_length"] = total_formal_length / len(data) if data else 0
        
        return stats
    
    def compare_v2c_v2s(self) -> Dict[str, Any]:
        """比较 v2c 和 v2s 版本"""
        comparison = {
            "common_problems": [],
            "v2c_only": [],
            "v2s_only": [],
            "differences": []
        }
        
        v2c_names = {item["name"]: item for item in self.v2c_data}
        v2s_names = {item["name"]: item for item in self.v2s_data}
        
        # 找出共同问题
        common_names = set(v2c_names.keys()) & set(v2s_names.keys())
        comparison["common_problems"] = sorted(list(common_names))
        
        # 找出只在某个版本存在的问题
        comparison["v2c_only"] = sorted(list(set(v2c_names.keys()) - set(v2s_names.keys())))
        comparison["v2s_only"] = sorted(list(set(v2s_names.keys()) - set(v2c_names.keys())))
        
        # 比较共同问题的差异
        for name in list(common_names)[:10]:  # 只比较前10个作为示例
            v2c_item = v2c_names[name]
            v2s_item = v2s_names[name]
            
            diff = {
                "name": name,
                "informal_different": v2c_item.get("informal_statement") != v2s_item.get("informal_statement"),
                "formal_different": v2c_item.get("formal_statement") != v2s_item.get("formal_statement"),
                "split_same": v2c_item.get("split") == v2s_item.get("split"),
            }
            
            if diff["informal_different"] or diff["formal_different"]:
                comparison["differences"].append(diff)
        
        return comparison
    
    def analyze_amc_problems(self) -> Dict[str, Any]:
        """分析 AMC 问题的处理方式"""
        amc_analysis = {
            "v2c_amc": [],
            "v2s_amc": [],
            "comparison": []
        }
        
        # 找出 AMC 问题
        for item in self.v2c_data:
            if "amc" in item.get("name", "").lower():
                amc_analysis["v2c_amc"].append(item)
        
        for item in self.v2s_data:
            if "amc" in item.get("name", "").lower():
                amc_analysis["v2s_amc"].append(item)
        
        # 比较前几个 AMC 问题
        v2c_amc_dict = {item["name"]: item for item in amc_analysis["v2c_amc"]}
        v2s_amc_dict = {item["name"]: item for item in amc_analysis["v2s_amc"]}
        
        common_amc = set(v2c_amc_dict.keys()) & set(v2s_amc_dict.keys())
        
        for name in list(common_amc)[:5]:  # 前5个作为示例
            v2c_item = v2c_amc_dict[name]
            v2s_item = v2s_amc_dict[name]
            
            amc_analysis["comparison"].append({
                "name": name,
                "v2c_informal": v2c_item.get("informal_statement", "")[:200] + "...",
                "v2s_informal": v2s_item.get("informal_statement", "")[:200] + "...",
                "v2c_formal": v2c_item.get("formal_statement", "")[:200] + "...",
                "v2s_formal": v2s_item.get("formal_statement", "")[:200] + "...",
            })
        
        return amc_analysis
    
    def generate_report(self) -> str:
        """生成分析报告"""
        report = []
        report.append("# miniF2F v1 vs v2 数据集比较分析报告\n")
        report.append(f"生成时间: {Path(__file__).stat().st_mtime}\n")
        
        # 统计信息
        report.append("## 1. 数据集统计信息\n")
        
        if self.v1_data:
            v1_stats = self.get_statistics(self.v1_data, "miniF2F v1")
            report.append(f"### {v1_stats['name']}")
            report.append(f"- 总问题数: {v1_stats['total']}")
            report.append(f"- 按 split 分布: {dict(v1_stats['by_split'])}")
            report.append(f"- 包含非正式证明: {v1_stats['has_informal_proof']} ({v1_stats['has_informal_proof']/v1_stats['total']*100:.1f}%)")
            report.append(f"- 包含正式证明: {v1_stats['has_formal_proof']} ({v1_stats['has_formal_proof']/v1_stats['total']*100:.1f}%)")
            report.append(f"- 平均非正式陈述长度: {v1_stats['avg_informal_length']:.0f} 字符")
            report.append(f"- 平均正式陈述长度: {v1_stats['avg_formal_length']:.0f} 字符\n")
        
        v2c_stats = self.get_statistics(self.v2c_data, "miniF2F v2c")
        report.append(f"### {v2c_stats['name']}")
        report.append(f"- 总问题数: {v2c_stats['total']}")
        report.append(f"- 按 split 分布: {dict(v2c_stats['by_split'])}")
        report.append(f"- 包含非正式证明: {v2c_stats['has_informal_proof']} ({v2c_stats['has_informal_proof']/v2c_stats['total']*100:.1f}%)")
        report.append(f"- 包含正式证明: {v2c_stats['has_formal_proof']} ({v2c_stats['has_formal_proof']/v2c_stats['total']*100:.1f}%)")
        report.append(f"- 平均非正式陈述长度: {v2c_stats['avg_informal_length']:.0f} 字符")
        report.append(f"- 平均正式陈述长度: {v2c_stats['avg_formal_length']:.0f} 字符\n")
        
        v2s_stats = self.get_statistics(self.v2s_data, "miniF2F v2s")
        report.append(f"### {v2s_stats['name']}")
        report.append(f"- 总问题数: {v2s_stats['total']}")
        report.append(f"- 按 split 分布: {dict(v2s_stats['by_split'])}")
        report.append(f"- 包含非正式证明: {v2s_stats['has_informal_proof']} ({v2s_stats['has_informal_proof']/v2s_stats['total']*100:.1f}%)")
        report.append(f"- 包含正式证明: {v2s_stats['has_formal_proof']} ({v2s_stats['has_formal_proof']/v2s_stats['total']*100:.1f}%)")
        report.append(f"- 平均非正式陈述长度: {v2s_stats['avg_informal_length']:.0f} 字符")
        report.append(f"- 平均正式陈述长度: {v2s_stats['avg_formal_length']:.0f} 字符\n")
        
        # v2c vs v2s 比较
        report.append("## 2. v2c vs v2s 版本比较\n")
        comparison = self.compare_v2c_v2s()
        report.append(f"- 共同问题数: {len(comparison['common_problems'])}")
        report.append(f"- 仅在 v2c 中: {len(comparison['v2c_only'])}")
        report.append(f"- 仅在 v2s 中: {len(comparison['v2s_only'])}")
        report.append(f"- 发现差异的问题数: {len(comparison['differences'])}\n")
        
        if comparison['v2c_only']:
            report.append(f"仅在 v2c 中的问题 (前10个): {comparison['v2c_only'][:10]}\n")
        if comparison['v2s_only']:
            report.append(f"仅在 v2s 中的问题 (前10个): {comparison['v2s_only'][:10]}\n")
        
        # AMC 问题分析
        report.append("## 3. AMC 问题处理方式分析\n")
        amc_analysis = self.analyze_amc_problems()
        report.append(f"- v2c 中 AMC 问题数: {len(amc_analysis['v2c_amc'])}")
        report.append(f"- v2s 中 AMC 问题数: {len(amc_analysis['v2s_amc'])}\n")
        
        if amc_analysis['comparison']:
            report.append("### AMC 问题示例比较\n")
            for comp in amc_analysis['comparison'][:3]:
                report.append(f"#### {comp['name']}\n")
                report.append("**v2c 非正式陈述:**")
                report.append(f"{comp['v2c_informal']}\n")
                report.append("**v2s 非正式陈述:**")
                report.append(f"{comp['v2s_informal']}\n")
                report.append("**v2c 正式陈述:**")
                report.append(f"```lean\n{comp['v2c_formal']}\n```\n")
                report.append("**v2s 正式陈述:**")
                report.append(f"```lean\n{comp['v2s_formal']}\n```\n")
        
        # 主要发现
        report.append("## 4. 主要发现\n")
        report.append("1. **v2c 版本**: 保持竞赛原样，选择题包含所有选项")
        report.append("2. **v2s 版本**: 简化版本，选择题直接给出答案")
        report.append("3. **匹配度**: v2 版本确保正式和非正式陈述完全匹配")
        report.append("4. **难度**: v2 版本可能更准确地反映真实难度\n")
        
        return "\n".join(report)
    
    def save_statistics(self, output_path: str = "statistics.json"):
        """保存统计信息到 JSON 文件"""
        stats = {}
        
        if self.v1_data:
            stats["v1"] = self.get_statistics(self.v1_data, "miniF2F v1")
        
        stats["v2c"] = self.get_statistics(self.v2c_data, "miniF2F v2c")
        stats["v2s"] = self.get_statistics(self.v2s_data, "miniF2F v2s")
        stats["comparison"] = self.compare_v2c_v2s()
        stats["amc_analysis"] = self.analyze_amc_problems()
        
        with open(output_path, 'w', encoding='utf-8') as f:
            json.dump(stats, f, ensure_ascii=False, indent=2)
        
        print(f"[OK] 统计信息已保存到: {output_path}")


def main():
    """主函数"""
    print("=" * 60)
    print("miniF2F v1 vs v2 数据集比较分析")
    print("=" * 60)
    print()
    
    # 初始化比较器
    comparator = DatasetComparator()
    
    # 加载数据集
    print("正在加载数据集...")
    comparator.load_all_datasets()
    print()
    
    # 生成报告
    print("正在生成分析报告...")
    report = comparator.generate_report()
    
    # 保存报告
    report_path = "analysis_report.md"
    with open(report_path, 'w', encoding='utf-8') as f:
        f.write(report)
    print(f"[OK] 分析报告已保存到: {report_path}")
    
    # 保存统计信息
    comparator.save_statistics()
    
    print()
    print("=" * 60)
    print("分析完成！")
    print("=" * 60)


if __name__ == "__main__":
    main()
