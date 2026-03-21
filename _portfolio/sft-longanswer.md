---
title: "LLM 后训练与数据评测 Agent 系统开发｜中文长回答优化方向"
date: 2026-02-01
excerpt: "围绕中文长回答生成质量优化，基于 Qwen2.5-1.5B + LoRA + TRL SFTTrainer 搭建端到端后训练 workflow，完成数据构建、SFT 微调、推理对比、离线评测与版本迭代的闭环系统。"
---

**时间：** 02/2026 – 至今  

**项目地址：** [LLM DataProcessing Agent](https://github.com/zhangbomingnice/LLM_dataprocessing_agent)

---

## 一、版本迭代：参数与算法修改

### 1.1 版本差异总表

| 版本 | 数据 | LoRA 范围 | max_length | learning_rate | epoch | 关键改动 |
|------|------|-----------|------------|---------------|-------|----------|
| **v2** | wiki+zhihu+wikihow 6000 条 | attn+MLP | 512 | 1e-4 | 2 | 扩到 6000 条，仍为 attn+MLP |
| **v2.5** | 沿用 v2 数据 | attn+MLP | **1024** | 5e-5 | 1 | 首次拉长训练窗口 |
| **v2.6** | train_v2/val_v2 6000 条 | **attn-only** | 1024 | **3e-5** | 1 | 切换 attn-only，降 lr，max_grad_norm=0.5 |
| **v2.7** | 同 v2.6 | attn-only | **1280** | **2.5e-5** | 1 | 更长窗口 + warmup 0.03，rep_penalty=1.08 |
| **v2.8** | **不重训，沿用 v2.7 模型** | 同 v2.7 | 同 v2.7 | 同 v2.7 | - | **仅改 generate()：rep_penalty 1.08→1.16，no_repeat_ngram=4** |
| **v2.9** | 同 v2.7 | **同 v2.7（attn-only）** | 1280 | 2.5e-5 | 1 | **CE + UL-lite（λ=0.2, ngram=4）**，LoRA 与 v2.7 一致 |

**重要说明：** v2.8 与 v2.9 的 LoRA 均与 v2.7 相同，未重新训练 adapter。v2.8 仅调整推理侧生成参数；v2.9 在训练侧加入 UL-lite loss，但 LoRA 结构不变。

### 1.2 数据使用

| 类型 | 规模 | 说明 |
|------|------|------|
| 训练数据 | train_v2.jsonl / val_v2.jsonl | 约 6000 条，wiki 2800 / zhihu 2600 / wikihow 600 |
| 评测数据 | eval_public_v2.jsonl | 600 条，全量评测；剔除共同 39 条异常样本后为稳健主体样本 |

---

## 二、Base vs SFT 整体趋势对比

以下对比**不含 v2.9**，因 v2.9 未做 v2.9 vs Base 的评测，仅与 v2.7 做 SFT 头对头。数据来自剔除共同 39 条异常样本后的稳健均值。

### 2.1 柱状图：总分、格式输出、语言结构、重复率

![Base vs SFT 对比]({{ site.baseurl }}/images/sft/base_sft_comparison.png)

### 2.2 各维度达标情况

| 维度 | 满分 | 说明 | v2 | v2.5 | v2.6 | v2.7 | v2.8 |
|------|------|------|-----|------|------|------|------|
| **格式输出 (ResponseMode)** | 20 | 是否像助手、回答结构是否合理 | SFT 达标 | SFT 明显退化 | SFT 达标 | SFT 达标 | SFT 达标 |
| **语言结构 (Structure+Org)** | 45 | 起承转合、段落组织 | SFT 略逊 | SFT 略逊 | SFT 略逊 | SFT 略逊 | SFT 略逊 |
| **非重复性 (NonRepetition)** | 15 | 无重复、表述精炼 | SFT 略逊 | **SFT 严重退化** | SFT 明显退化 | SFT 明显退化 | **SFT 达标** |

**SFT 训练达标结论：**

- **格式输出：** v2.6 起 SFT 在 ResponseMode 上达到或接近满分 20，符合「更像助手」的目标。
- **语言结构：** 各版本 SFT 在 Structure+Organization 上多数略逊于 Base，v2.5 结构有改善但被重复问题掩盖；v2.8 在 Organization 上首次明显转正。
- **重复率：** v2.5 最差（SFT 仅约 4.8），v2.6/v2.7 仍明显未达标；**v2.8 是首个在 NonRepetition 上真正压住重复的版本**（SFT 达 15 满分），依赖 decode 侧 repetition_penalty=1.16 与 no_repeat_ngram_size=4。

---

## 三、v2.7 vs v2.9：UL-lite 带来的变化

v2.9 使用 **v2.7 的 LoRA**，唯一变量为损失函数：**CE vs CE+UL-lite**。评测为 v2.7 SFT 与 v2.9 SFT 头对头对比。

### 3.1 数据对比（剔除异常样本后）

| 维度 | v2.7 | v2.9 | 变化 |
|------|------|------|------|
| 总分 | 77.24 | 78.35 | +1.11 |
| ResponseMode | 19.97 | 20.00 | +0.03 |
| Structure | 20.34 | 19.55 | **-0.79** |
| Organization | 11.63 | 11.79 | +0.16 |
| Fluency | 10.00 | 10.00 | 持平 |
| NonRepetition | 14.62 | 14.89 | **+0.27** |
| TaskFit | 5.00 | 5.00 | 持平 |

### 3.2 变化解读

- **NonRepetition：** v2.9 相对 v2.7 有约 +0.27 的提升，说明 UL-lite 在训练侧有效改善了重复问题，不依赖 decode 约束。
- **Structure：** v2.9 在 Structure 上略逊于 v2.7（约 -0.79），UL 强度可能轻微牺牲了结构完整性。
- **其余维度：** ResponseMode、Organization、Fluency、TaskFit 基本持平或略有提升。

**结论：** UL-lite 在训练侧实现了可验证的反重复收益，但需在 λ、ngram 等超参上进一步平衡，以减轻对 Structure 的负面影响。

---

## 四、Version 3 对照实验（600 条全量 head-to-head）

以下结论基于**完整 600 条**评测样本、按 answer key 正确还原 A/B 后的 head-to-head 评分；不再使用早期 206 条子集解析。

### 4.1 总结结论

| 对比 | 总分均值 (V3 − 基线) | 胜负 (V3 胜 / 平 / 基线胜) | 非平局胜率 | 显著性 |
|------|----------------------|----------------------------|------------|--------|
| **v3_main vs v2.7** | **+0.95** | 62 / 476 / 62 | 50.0% | t / Wilcoxon **不显著** |
| **v3_bestdecode vs v2.8** | **−0.32** | 295 / 9 / 296 | 49.9% | **不显著** |

- **v3_main 相对 v2.7：** 各小项与总分均略正，但**高平局、弱差异**；trimmed mean 为 0，只能概括为「方向偏正、尚未形成统计上可分离的优势」。
- **v3_bestdecode 相对 v2.8：** **几乎完全打平**（仅 9 条平局），六维均值全部为 v3 略低，但差距极小；**v2.8 极轻微占优**，差异可视为噪声级。

**压缩判断：** Version 3 系列已接近 v2.7 / v2.8 两条基线，但**尚未在统计上明确超越**。

### 4.2 各维度均值（全量 600 条）

| 对比 | 基线 | V3 | Mode | Struct | Org | Fluency | Rep | Fit | Total |
|------|------|-----|------|--------|-----|---------|-----|-----|-------|
| v3_main vs v2.7 | v2.7 | v3_main | 19.98→20.00 | 22.16→22.35 | 17.91→18.13 | 14.33→14.45 | 13.03→13.35 | 4.60→4.67 | 92.0→92.9 (**+0.95**) |
| v3_bestdecode vs v2.8 | v2.8 | v3_bestdecode | 19.61→19.55 | 21.89→21.79 | 18.06→17.98 | 14.31→14.30 | 14.72→14.69 | 4.63→4.59 | 93.23→92.91 (**−0.32**) |

### 4.3 稳健统计

| 对比 | 中位差 (V3−基线) | 10% trimmed mean | t 检验 p | Wilcoxon p |
|------|------------------|------------------|----------|------------|
| v3_main vs v2.7 | 0 | 0.000 | 0.317 | 0.294 |
| v3_bestdecode vs v2.8 | 0 | −0.096 | 0.529 | 0.616 |

### 4.4 可视化

**均值对比（六维度 + 总分分列）：**

![Version3 head-to-head]({{ site.baseurl }}/images/sft/version3_head_to_head.png)

**各维度与总分的均值差 Δ (V3 − 基线)：**

![Version3 delta]({{ site.baseurl }}/images/sft/version3_delta.png)

---

## 五、六维度评测体系

| 维度 | 英文 key | 满分 | 说明 |
|------|----------|------|------|
| 回复模式 | ResponseMode | 20 | 是否像助手、回答结构是否合理 |
| 结构完整性 | Structure | 25 | 起承转合、逻辑递进 |
| 组织条理 | Organization | 20 | 段落组织、层次清晰 |
| 流畅度 | Fluency | 15 | 表达自然、无生硬感 |
| 非重复性 | NonRepetition | 15 | 无重复、表述精炼 |
| 任务契合度 | TaskFit | 5 | 精准回应问题 |

**总分范围：** 0–100。评测采用 Pairwise blind comparison，MiniMax 2.7 与 Gemini Pro 3 双裁判，结合 N-gram 重复率、结构统计、风格检测、多轮评审（K=3）与中位数聚合/规则后修正。

