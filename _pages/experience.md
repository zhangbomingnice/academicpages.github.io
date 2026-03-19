---
layout: archive
title: "项目与实习"
permalink: /experience/
author_profile: true
---

{% include base_path %}

## 项目经历

<p class="section-entry-title">1. <a href="{{ site.baseurl }}/portfolio/sft-longanswer/">LLM 后训练与数据评测 Agent 系统开发｜中文长回答优化方向</a></p>
<span class="section-entry-meta">02/2026 – 至今</span>

* 围绕中文长回答生成质量优化，基于 Qwen2.5-1.5B + LoRA + TRL SFTTrainer 搭建端到端后训练 workflow，完成 数据构建、SFT 微调、推理对比、离线评测与版本迭代 的闭环系统，重点解决长回答中的结构松散、后半段空转与重复生成问题。
* 自主设计并落地 LLM DataProcessing Agent，将数据清洗、样本重写、CoT 标注、质量筛查与评测分析流程 agent 化，形成可复用的数据处理基础设施；其中 Corpus Cleaner 负责训练语料质量提升，cn_eval 负责评测集自动化分析与结果聚合。
* 构建 Pairwise blind comparison + LLM-as-a-Judge 评测框架，引入 MiniMax 2.7 与 Gemini Pro 3 作为双裁判模型，结合 N-gram 重复率、结构统计、风格检测、多轮评审（K=3）与中位数聚合/规则后修正，实现面向中文长回答的自动化、多维度质量评估。
* 在约 6000 条训练样本、600 条评测样本 上推进 v2–v2.9 多版本实验，对 LoRA target、max_length、learning rate、decode 策略与 UL-lite loss 等关键变量进行系统对照，定位 NonRepetition 为核心瓶颈，并形成从训练侧到推理侧的专项优化路径。
* 推动最佳版本相较 base 获得 +8.09 分整体增益，验证了 attention-only LoRA + 低学习率 + decode 约束 在中文长回答场景中的有效性，并为后续 RLHF / Preference Optimization / reward design 提供可复用实验基线。

<p class="section-entry-title">2. <a href="{{ site.baseurl }}/portfolio/photonics/">基于 AI 的一维光子晶体逆向设计</a></p>
<span class="section-entry-meta">12/2023 – 05/2024</span>

* 基于 NumPy 与传输矩阵法（TMM）自研向量化物理模型，完成一维多层薄膜结构在多入射角（0°–60°）及 TE/TM 偏振态下的正向模拟，搭建「结构参数 → 物理仿真 → 光谱输出」的自动化数据管线。
* 构建融合阻带抑制、通带透过率与厚度/层数惩罚的多目标损失函数，搭建逆向设计闭环，输出可运行最小可行系统（MVS），并为后续引入代理模型与串联神经网络提供基线。

<p class="section-entry-title">3. <a href="{{ site.baseurl }}/portfolio/rydberg/">里德堡原子交互式计算平台开发</a></p>
<span class="section-entry-meta">07/2023 – 02/2024 · 指导老师：贾凤东（中国科学院大学）</span>

* 面向 Rb/Cs 计算场景提出基于耦合强度的自适应基组截断算法，结合异步任务处理与 Docker 标准化部署，在有限云资源下提升多用户并发响应与计算吞吐量，并将数值收敛精度由 10⁻¹ 提升至 10⁻² 量级。
* 基于 React + FastAPI 设计前后端分离架构，将传统 ARC 3.0 原子物理仿真流程封装为可并发、可扩展的 SaaS 化计算平台，支持跃迁波长、Stark Map 与相关系数等核心能力，并完成中国科学院大学科创计划项目交付。

<p class="section-entry-title">4. <a href="{{ site.baseurl }}/portfolio/nuclear/">基于数据分析的核物理能级结构搭建</a></p>
<span class="section-entry-meta">05/2022 – 03/2024</span>

* 面向中国原子能科学研究院（CIAE）HI-13 串列加速器实验采集的 8.15×10⁸ 条 γ-γ 两重符合事件，自研基于 SQL 检索与 Pandas 清洗的数据处理管线，将跨 12 种核素背景的原始探测信号转化为标准化分析矩阵。
* 基于 γ-γ 符合关系与伴生核素已知能级约束完成复杂信号分离，在原有能级纲图基础上发现 17 条新射线跃迁和 6 个新能级，刷新 ⁹⁶Rh 最完善能级结构记录，并完成目标核内部结构模型的验证与修正。

<p class="section-entry-title">5. <a href="{{ site.baseurl }}/portfolio/crossplatform/">跨平台效率工具产品开发</a></p>
<span class="section-entry-meta">02/2026 – 至今</span>

* 独立主导并交付两款覆盖 iOS、鸿蒙、安卓系统与 Web 端的应用，通过继承 Claude Code、Opencode 等搭建 App 开发工作流，实现业务逻辑在多端的高效同步和迭代。
* 从 UI 设计、3D 视觉渲染到后端数据库完成全栈开发；项目周期内探索 AI 工具链在交付过程中的辅助提升，具备多端产品从 0 到 1 的完整交付能力。

---

## 实习经历

<p class="section-entry-title">时代骐骥新能源科技（大同）有限公司（宁德时代）</p>
<p class="section-entry-title-sub">算法优化工程师 · 07/2024 – 09/2024</p>

* 针对大同地区重型卡车交付网络，利用空间数据分析与设备选址模型，对充电站点与交付中心进行精细化地理布局；结合物流动线与充电需求，有效降低车队空车率，提升区域补能效率与交付时效。
* 深入参与当地政府部门沟通对接，协调新能源建设与城市交通规划融合，通过政策与多方资源整合，确保补能网络在当地快速从 0 到 1 落地。
