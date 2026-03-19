---
title: "中文长回答 SFT 评测与优化"
date: 2026-02-01
excerpt: "基于 Qwen2.5-1.5B 的 LoRA SFT 中文长回答生成优化，多版本迭代（v2→v2.9），六维度评测体系与参数影响分析。"
---

**时间：** 02/2026 – 至今  

**项目地址：** [LLM DataProcessing Agent](https://github.com/zhangbomingnice/LLM_dataprocessing_agent)

---

## 一、项目概览

本项目围绕 **Qwen2.5-1.5B** 基座模型，通过 LoRA SFT 提升**中文长回答生成质量**，重点解决：

- 长回答的结构完整性、组织条理
- 流畅度与任务契合度
- **非重复性（NonRepetition）** — 贯穿全版本的核心瓶颈

### 技术栈

| 组件 | 选型 |
|------|------|
| 基座模型 | Qwen/Qwen2.5-1.5B |
| 微调方式 | LoRA (PEFT) |
| 训练框架 | TRL SFTTrainer + HuggingFace Transformers |
| 数据格式 | JSONL（Instruction-Response 对） |
| 评测 | Pairwise blind comparison，MiniMax 2.7 / Gemini Pro 3 |

---

## 二、版本迭代与核心发现

### 2.1 版本演化主线

```
v2 (修崩坏) → v2.5 (长窗口失败) → v2.6 (attn-only 转折) → v2.7 (成熟基线)
                                                                    │
                                    ┌───────────────────────────────┼───────────────────────────────┐
                                    │                               │                               │
                                    ▼                               ▼                               ▼
                              v2.8 (decode 工程)              v2.9 (UL-lite)              未来方向
```

### 2.2 关键参数与效果

| 参数 | 正向影响 | 负向影响 | 结论 |
|------|----------|----------|------|
| **max_length** | 1280 给长回答更多训练窗口 | 1024 在旧 recipe 下放大重复 | 需配合 attn-only + 低 lr |
| **Learning Rate** | 2.5e-5 更稳 | 1e-4 易学坏 base | 建议 2.5e–3e-5 |
| **LoRA targets** | attn-only 保护 base | attn+MLP 易退化 | 推荐 attn-only |
| **repetition_penalty** | 1.16 显著提升 | 1.08 相对不足 | decode 侧关键参数 |
| **UL-lite** | 训练侧改善 NonRepetition | 可能轻微牺牲 Structure | v2.9 验证有效 |

### 2.3 最终效果排名

**含 decode 约束：** v2.8 > v2.9 > v2.7 > v2.6 > v2 > v2.5  

**纯训练侧：** v2.9 ≈ v2.7 > v2.6 > v2 > v2.5  

---

## 三、六维度评测体系

| 维度 | 英文 key | 满分 | 说明 |
|------|----------|------|------|
| 回复模式 | ResponseMode | 20 | 是否像助手、回答结构是否合理 |
| 结构完整性 | Structure | 25 | 起承转合、逻辑递进 |
| 组织条理 | Organization | 20 | 段落组织、层次清晰 |
| 流畅度 | Fluency | 15 | 表达自然、无生硬感 |
| 非重复性 | NonRepetition | 15 | 无重复、表述精炼 |
| 任务契合度 | TaskFit | 5 | 精准回应问题 |

**总分范围：** 0–100。

---

## 四、多维度评分可视化

以下图表基于 600 条评测样本的统计结果生成。

### 4.1 总分对比（SFT vs Base）

![总分对比]({{ site.baseurl }}/images/sft/fig1_total_score.png)

v2.8 的 SFT 均分最高（约 87），且 Base 均分相对较低（约 79），说明 decode 约束显著提升了整体表现。v2.5 的 SFT 均分明显低于 Base，存在系统性退化。

### 4.2 版本 Delta 趋势（SFT - Base）

![Delta趋势]({{ site.baseurl }}/images/sft/fig2_delta_trend.png)

v2.8 的 Δ 最大（+8.09），是唯一在稳健统计上全面为正的版本。v2.5 的 Δ 为 -13.73，表现最差。

### 4.3 六维度雷达图（v2–v2.7）

![六维度雷达图]({{ site.baseurl }}/images/sft/fig3_radar.png)

v2.7 在 ResponseMode、Fluency、TaskFit 上表现较好；v2.5 在 NonRepetition 上明显退化。

### 4.4 各维度 Delta 热力图

![维度热力图]({{ site.baseurl }}/images/sft/fig4_heatmap.png)

绿色表示 SFT 优于 Base，红色表示 SFT 劣于 Base。v2.5 在 NonRepetition 上明显为负。

### 4.5 子集分层对比（wiki / zhihu / wikihow）

![子集对比]({{ site.baseurl }}/images/sft/fig5_subset.png)

v2.8 在三个子集上均为正；v2.7 在 zhihu 上略正，wikihow 上略负；v2.5 在三个子集上均为负。

### 4.6 参数影响：max_length vs Delta

![max_length影响]({{ site.baseurl }}/images/sft/fig6_maxlength.png)

max_length 从 512 到 1024 时（v2.5）出现退化，说明单纯拉长窗口会放大重复问题；v2.6/v2.7 在 attention-only + 低学习率下，1024/1280 表现更稳。

### 4.7 参数影响：Learning Rate vs Delta

![学习率影响]({{ site.baseurl }}/images/sft/fig7_lr.png)

学习率从 1e-4 降到 2.5e-5 时，整体趋势向好；v2.5 的 5e-5 配合 attn+MLP 导致退化。

### 4.8 LoRA 目标类型对比（attn+MLP vs attn-only）

![LoRA类型]({{ site.baseurl }}/images/sft/fig8_lora.png)

attn-only 平均 Delta 明显优于 attn+MLP，说明减少 MLP 更新有助于保护 base prior。

### 4.9 v2.9 vs v2.7 六维度对比

![v2.9 vs v2.7]({{ site.baseurl }}/images/sft/fig9_v29_v27.png)

v2.9 在 NonRepetition 上优于 v2.7（+0.30），在 Structure 上略逊（-0.76），UL-lite 在训练侧有效改善了重复问题。

---

## 五、主要工作与成果

- **多版本迭代：** 从 v2 到 v2.9，系统化探索 LoRA 目标、学习率、max_length、decode 约束与 UL-lite 等参数对中文长回答质量的影响。

- **LoRA 架构优化：** 发现 attn-only 相比 attn+MLP 显著提升 Delta（约 -5.2 → +2.6），减少对 base prior 的破坏。

- **超参数调优：** 通过 Learning Rate 与 max_length 的联合实验，确定 2.5e-5 + 1280 为较优配置。

- **推理侧工程：** v2.8 通过 repetition_penalty=1.16 与 no_repeat_ngram_size=4 实现最佳整体表现。

- **训练侧反重复：** v2.9 引入 UL-lite loss（λ=0.2, ngram=4），在 NonRepetition 维度取得提升。

- **评测体系搭建：** 依托 LLM-as-Judge（MiniMax 2.7 / Gemini Pro 3）与 Pairwise 盲评，构建六维度可解释评测流程。

---

## 六、参考文档

- [LLM DataProcessing Agent GitHub](https://github.com/zhangbomingnice/LLM_dataprocessing_agent)
- 完整项目经理报告见项目仓库或本地 `Project_Manager_Report.md`
