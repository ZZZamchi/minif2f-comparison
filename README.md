# miniF2F v1 vs v2 数据集比较分析

本项目包含原始 miniF2F (v1) 数据集与其改进版本 miniF2F_v2 (v2c 和 v2s) 的详细比较分析。

## 数据集版本说明

### miniF2F v1 (原始版本)
- **来源**: [Tonic/MiniF2F on Hugging Face](https://huggingface.co/datasets/Tonic/MiniF2F)
- **总问题数**: 488 (valid: 244, test: 244)
- **特点**: 可能存在正式和非正式陈述不匹配的问题

### miniF2F v2c (竞赛版本)
- **来源**: [roozbeh-yz/miniF2F_v2](https://github.com/roozbeh-yz/miniF2F_v2)
- **总问题数**: 488 (valid: 244, test: 244)
- **特点**: 保持竞赛原样，选择题包含所有选项，需要证明结果属于选项集合

### miniF2F v2s (简化版本)
- **来源**: [roozbeh-yz/miniF2F_v2](https://github.com/roozbeh-yz/miniF2F_v2)
- **总问题数**: 488 (valid: 244, test: 244)
- **特点**: 简化版本，选择题直接给出答案，陈述更清晰

## 主要发现

1. **匹配度**: v2 版本确保所有正式和非正式陈述完全匹配
2. **选择题处理**:
   - v1: 直接给出答案
   - v2c: 包含所有选项，需要证明结果属于选项集合
   - v2s: 直接给出答案，但陈述更清晰
3. **陈述长度**: v2s 版本的平均陈述长度最短（148 字符），v1 最长（177 字符）

## 项目结构

```
minif2f_comparison/
├── datasets/              # v2 数据集文件
│   ├── miniF2F_v2c.json
│   ├── miniF2F_v2c.jsonl
│   ├── miniF2F_v2s.json
│   └── miniF2F_v2s.jsonl
├── assets/                # 资源文件
│   └── 1_vs_2s_vs_2c.png
├── minif2f_v1/            # v1 数据集
│   └── miniF2F_v1.json
├── compare_datasets.py    # 数据集比较脚本
├── generate_detailed_report.py  # 详细报告生成脚本
├── download_tonic_minif2f.py    # v1 数据集下载脚本
├── miniF2F_comparison_report.docx  # Word 格式详细报告
├── Google_Docs_完整对比_纯文本.txt  # Google 文档格式对比
├── statistics.json        # 统计信息
└── README.md             # 本文件
```

## 使用方法

### 查看报告

**推荐**: 直接打开 `miniF2F_comparison_report.docx` 查看详细的比较分析，包含：
- 数据集统计信息表格
- 5 个具体问题的详细对比（v1、v2c、v2s 三个版本）
- 每个示例的差异分析

### 重新生成报告

```bash
# 重新生成 Word 报告
python generate_detailed_report.py

# 重新运行基础比较
python compare_datasets.py
```

### 下载 v1 数据集

如果需要重新下载 v1 数据集：

```bash
python download_tonic_minif2f.py
```

## 数据来源

- **v1**: https://huggingface.co/datasets/Tonic/MiniF2F
- **v2**: https://github.com/roozbeh-yz/miniF2F_v2

## 性能对比

根据论文数据，v2 版本在模型上的表现：

| 模型 | v1-test | v2s-test | v2c-test |
|------|---------|----------|----------|
| Deepseek-Prover-V1.5-RL | 50.0% | 41.0% | 38.1% |
| Goedel-Prover-SFT | 58.2% | 48.4% | 46.3% |
| Kimina-Prover-Distill-7B | 65.2% | 59.0% | 57.0% |
| DeepSeek-Prover-V2-7B | 73.4% | 68.1% | 64.4% |
| Goedel-V2 | 82.0% | 74.2% | 72.5% |

**观察**: v2 版本的准确率普遍低于 v1，这可能是因为 v2 更准确地反映了真实难度。

## 引用

如果使用本分析，请引用相关论文：

### v2 论文
```bibtex
@inproceedings{
  ospanov2025minifflean,
  title={miniF2F-Lean Revisited: Reviewing Limitations and Charting a Path Forward},
  author={Azim Ospanov and Farzan Farnia and Roozbeh Yousefzadeh},
  booktitle={The Thirty-ninth Annual Conference on Neural Information Processing Systems},
  year={2025},
  url={https://openreview.net/forum?id=KtaHv0YUyh}
}
```

### v1 论文
```bibtex
@inproceedings{
  jiang2022draft,
  title={Draft, Sketch, and Prove: Guiding Formal Theorem Provers with Informal Proofs},
  author={Albert Q. Jiang and Sean Welleck and Jin Peng Zhou and Wenda Li and Jiacheng Liu and Mateja Jamnik and Timothée Lacroix and Yuhuai Wu and Guillaume Lample},
  booktitle={Submitted to The Eleventh International Conference on Learning Representations},
  year={2022},
  url={https://arxiv.org/abs/2210.12283}
}
```

## 许可证

本项目遵循 Apache-2.0 许可证（与 miniF2F_v2 相同）。

## 贡献

欢迎提交 Issue 和 Pull Request！
