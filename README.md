# Lean Benchmark Collection

形式化数学基准数据集集合和分析。

## 项目结构

```
.
├── benchmarks/          # 所有基准数据集
│   ├── minif2f/        # miniF2F 数据集
│   │   ├── minif2f_v1/ # v1 版本
│   │   └── datasets/   # v2c 和 v2s 版本
│   ├── putnambench/    # PutnamBench
│   ├── proofnet/       # ProofNet
│   └── leancat/        # LeanCat
├── analysis/           # 分析脚本和文档
│   └── minif2f/       # miniF2F 分析
│       ├── compare_datasets.py
│       └── README.md
└── README.md
```

## 基准数据集

### miniF2F

- **v1**: 原始版本，488 个问题
- **v2c**: 竞赛版本，保留所有选项
- **v2s**: 简化版本，直接给出答案

### PutnamBench

Putnam 数学竞赛问题基准（1962-2025）。

- **来源**: https://github.com/trishullab/PutnamBench
- **语言**: Lean 4, Isabelle, Coq
- **问题数**: 1724

### ProofNet

本科数学自动形式化基准。

- **来源**: https://github.com/zhangir-azerbayev/proofnet
- **语言**: Lean 3/4
- **问题数**: 371

### LeanCat

范畴论形式化基准。

- **来源**: https://github.com/sciencraft/LeanCat
- **语言**: Lean 4
- **问题数**: 100

## 使用方法

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
- **LeanCat**: https://github.com/sciencraft/LeanCat

## 许可证

- miniF2F: Apache-2.0
- PutnamBench: Apache-2.0 (Lean 4, Isabelle), MIT (Coq)
- ProofNet: MIT
- LeanCat: MIT
