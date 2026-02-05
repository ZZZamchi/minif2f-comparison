# Lean Benchmark Collection

形式化数学基准数据集集合和分析。

## 项目结构

```
.
├── benchmarks/          # 所有基准数据集
│   ├── minif2f/        # miniF2F 数据集
│   ├── putnambench/    # PutnamBench
│   ├── proofnet/       # ProofNet
│   ├── leancat/        # LeanCat
│   └── fate/           # FATE
├── analysis/           # 分析脚本和文档
│   └── minif2f/       # miniF2F 分析
└── README.md
```

## 基准数据集

### miniF2F

高中数学竞赛问题基准，包含 AMC、AIME 等竞赛题目。

- **来源**: https://github.com/roozbeh-yz/miniF2F_v2
- **语言**: Lean 4
- **问题数**: 488 (v1, v2c, v2s)
- **特点**: 包含选择题和证明题，v2 版本改进了陈述匹配度

### PutnamBench

Putnam 数学竞赛问题基准（1962-2025）。

- **来源**: https://github.com/trishullab/PutnamBench
- **语言**: Lean 4, Isabelle, Coq
- **问题数**: 1724
- **特点**: 本科竞赛数学，多语言支持

### ProofNet

本科数学自动形式化基准。

- **来源**: https://github.com/zhangir-azerbayev/proofnet
- **语言**: Lean 3/4
- **问题数**: 371
- **特点**: 涵盖线性代数、实分析、抽象代数等

### LeanCat

范畴论形式化基准。

- **来源**: https://github.com/sciencraft/LeanCat
- **语言**: Lean 4
- **问题数**: 100
- **特点**: 研究级范畴论问题，测试抽象推理能力

### FATE

形式化代数定理评估基准，包含抽象代数和交换代数问题。

- **来源**: https://github.com/frenzymath/FATE
- **语言**: Lean 4
- **问题数**: 350 (FATE-M: 150, FATE-H: 100, FATE-X: 100)
- **特点**: 三个难度级别，从基础练习到博士资格考试级别

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
- **FATE**: https://github.com/frenzymath/FATE

## 许可证

- miniF2F: Apache-2.0
- PutnamBench: Apache-2.0 (Lean 4, Isabelle), MIT (Coq)
- ProofNet: MIT
- LeanCat: MIT
- FATE: MIT