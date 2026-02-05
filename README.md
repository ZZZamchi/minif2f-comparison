# Formal Math Benchmarks Collection

本项目收集和整理形式化数学基准数据集，并提供详细的分析和比较。

## 项目结构

```
.
├── benchmarks/              # 基准数据集
│   ├── putnambench/        # PutnamBench 数据集
│   ├── proofnet/           # ProofNet 数据集
│   └── minif2f/           # miniF2F 数据集（在 analysis 中）
├── analysis/               # 分析内容
│   └── minif2f/           # miniF2F v1 vs v2 比较分析
│       ├── examples.md     # 具体例子分析
│       ├── comparison.md  # 完整对比分析
│       └── ...
└── README.md
```

## 基准数据集

### miniF2F

- **v1**: 原始版本，488 个问题
- **v2c**: 竞赛版本，保留所有选项
- **v2s**: 简化版本，直接给出答案

详细分析见 `analysis/minif2f/`

### PutnamBench

PutnamBench 是一个评估定理证明算法的基准，包含来自 William Lowell Putnam 数学竞赛（1962-2025）的问题。

- **来源**: https://github.com/trishullab/PutnamBench
- **语言**: Lean 4, Isabelle, Coq
- **问题数**: 1724 个形式化问题

### ProofNet

ProofNet 是一个自动形式化和形式证明本科数学的基准。

- **来源**: https://github.com/zhangir-azerbayev/proofnet
- **语言**: Lean 3 (建议使用 Lean 4 移植版本)
- **问题数**: 371 个例子

## 使用方法

### 下载基准数据集

```bash
python download_benchmarks.py
```

### 运行分析

```bash
cd analysis/minif2f
python compare_datasets.py
```

## 数据来源

- **miniF2F v1**: https://huggingface.co/datasets/Tonic/MiniF2F
- **miniF2F v2**: https://github.com/roozbeh-yz/miniF2F_v2
- **PutnamBench**: https://github.com/trishullab/PutnamBench
- **ProofNet**: https://github.com/zhangir-azerbayev/proofnet

## 许可证

- miniF2F: Apache-2.0
- PutnamBench: Apache-2.0 (Lean 4, Isabelle), MIT (Coq)
- ProofNet: MIT

## 贡献

欢迎提交 Issue 和 Pull Request！
