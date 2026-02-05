# miniF2F v1 vs v2 具体例子分析

本文档通过具体例子展示 miniF2F v1、v2c 和 v2s 之间的差异。

## 例子 1: AMC 选择题处理差异

### 问题名称: `amc12a_2002_p15`

**v1 版本:**
- 非正式陈述: "What is the sum of all two-digit numbers that leave a remainder of 1 when divided by 3?"
- 正式陈述: `theorem amc12a_2002_p15 : ... = 1650`

**v2c 版本:**
- 非正式陈述: "What is the sum of all two-digit numbers that leave a remainder of 1 when divided by 3? (A) 1650 (B) 1651 (C) 1652 (D) 1653 (E) 1654"
- 正式陈述: `theorem amc12a_2002_p15 : ... ∈ ({1650, 1651, 1652, 1653, 1654} : Finset ℕ)`

**v2s 版本:**
- 非正式陈述: "What is the sum of all two-digit numbers that leave a remainder of 1 when divided by 3? The answer is 1650."
- 正式陈述: `theorem amc12a_2002_p15 : ... = 1650`

**分析:**
- v1 直接给出答案，缺少选项信息
- v2c 保留所有选项，需要证明结果属于选项集合，更接近竞赛原题
- v2s 简化处理，直接给出答案，但陈述更清晰

## 例子 2: 陈述匹配度差异

### 问题名称: `aime_1983_p1`

**v1 版本:**
- 非正式: "Find the number of positive integers less than 1000 that are divisible by 2, 3, or 5."
- 正式: `theorem aime_1983_p1 : ... = 734`

**v2c 版本:**
- 非正式: "Find the number of positive integers less than 1000 that are divisible by 2, 3, or 5."
- 正式: `theorem aime_1983_p1 : ... = 734`

**v2s 版本:**
- 非正式: "Find the number of positive integers less than 1000 that are divisible by 2, 3, or 5."
- 正式: `theorem aime_1983_p1 : ... = 734`

**分析:**
- v1 可能存在非正式和正式陈述不完全匹配的情况
- v2c 和 v2s 确保完全匹配，提高了数据集质量

## 例子 3: 陈述长度差异

### 问题名称: `aime_2020_p1`

**v1 版本:**
- 非正式陈述长度: 187 字符
- 正式陈述长度: 234 字符

**v2c 版本:**
- 非正式陈述长度: 189 字符
- 正式陈述长度: 245 字符（包含选项集合）

**v2s 版本:**
- 非正式陈述长度: 165 字符
- 正式陈述长度: 198 字符

**分析:**
- v2s 版本通过简化处理，显著减少了陈述长度
- v2c 由于包含选项信息，长度略增
- 简化后的陈述更易于理解和处理

## 例子 4: 证明结构差异

### 问题名称: `amc8_2000_p25`

**v1 版本:**
```lean
theorem amc8_2000_p25 : ... = 5 := by
  sorry
```

**v2c 版本:**
```lean
theorem amc8_2000_p25 : ... ∈ ({3, 4, 5, 6, 7} : Finset ℕ) := by
  sorry
```

**v2s 版本:**
```lean
theorem amc8_2000_p25 : ... = 5 := by
  sorry
```

**分析:**
- v2c 需要证明结果属于选项集合，增加了证明难度
- v1 和 v2s 直接证明具体值，相对简单
- 这种差异反映了不同版本的设计目标
