---
permalink: /
title: "张博铭"
author_profile: true
redirect_from:
  - /about/
  - /about.html
---

### 研究兴趣

1. LLM 算法  
2. 深度学习与强化学习  
3. 数学建模以及数值模拟  

---

### 教育经历

<div class="home-edu">
  <div class="home-edu__row">
    <div class="home-edu__logo"><img src="{{ site.url }}{{ site.baseurl }}/images/edu-sdu.png" alt="山东大学" /></div>
    <div class="home-edu__detail">
      <strong>山东大学 (SDU)</strong><span class="home-edu__time">09/2021 — 06/2025</span><br />
      应用物理学 理学学士 · GPA 89.43/100
    </div>
  </div>
  <div class="home-edu__row">
    <div class="home-edu__logo"><img src="{{ site.url }}{{ site.baseurl }}/images/edu-upenn.png" alt="宾夕法尼亚大学" /></div>
    <div class="home-edu__detail">
      <strong>宾夕法尼亚大学（Upenn）</strong><span class="home-edu__time">08/2025 — 至今</span><br />
      电气工程 硕士 · GPA 4.0/4.0
    </div>
  </div>
</div>

---

### 论文发表

**CL 模型非线性动力学仿真与分形分析**（指导老师：姜云国，山东大学）

- **高维度数值模拟：** 基于 MATLAB 自主研发高性能非线性系统数学建模，集成 RK4（四阶龙格-库塔）与二阶有限差分算法，解决复杂标量场演化中的非线性迭代与收敛问题；系统支持动态能量密度追踪与智能截断机制，实现对孤子对碰撞过程中高维能量交换模式的精准建模与逻辑还原。  
- **非线性特征提取：** 利用极高分辨率参数空间搜索与多层次可视化分析，挖掘非线性系统演化中的分形结构并首次发现 CL 模型参数与出射速度之间的自相似模式，并定量求解 Hausdorff 维数。  

**arXiv:** [2503.20799](https://arxiv.org/abs/2503.20799)

---

### 项目经历

<p class="section-entry-title">1. <a href="{{ site.baseurl }}/portfolio/sft-longanswer/">针对于中文（孤立语）的LLM 长回答优化</a></p>
<span class="section-entry-meta">03/2026 – 至今</span>

- 面向中文长回答中的结构松散、主题漂移、重复回环与长序列质量衰退，探究长序列后半段稳定性与 CoT 在长文本中的外推；基于 Hugging Face 约 4.4 万条语料完成筛选与 LLM judge 质量评估，构建高质量训练集。
- 基于 Qwen3.5-3B 搭建后训练 workflow（SFT、推理对比、离线评测与版本迭代），系统对照 LoRA、max_length、learning rate、decode 等变量，定位重复与长序列回答等核心瓶颈。
- 构建 LLM-as-a-Judge agent，引入 MiniMax 2.7、Gemini Pro 3、GLM 5.1 与多类统计与规则后处理；并开展 prompt 长度效应实验及 RL-friendly SFT、CoT 与分段生成等探索。  

<p class="section-entry-title">2. <a href="{{ site.baseurl }}/portfolio/photonics/">面向混合离散-连续设计的光学多层膜逆向学习驱动搜索框架</a></p>
<span class="section-entry-meta">12/2023 – 05/2024</span>

- 将可见光多层膜设计建模为 MDO 问题，结合 TMM 前向评估、ValueNet 学习筛选与 GA/PSO 演化搜索，处理离散材料选择与连续层厚、目标不可导带来的高维非凸优化。  
- 在 450–500 nm 防蓝光等任务上得到约 11 层、总厚约 630 nm 的代表性设计，目标区平均透过率约 2.3%；代码见 [1Dthinfilm_design](https://github.com/zhangbomingnice/1Dthinfilm_design)。  

<p class="section-entry-title">3. <a href="{{ site.baseurl }}/portfolio/rydberg/">里德堡原子交互式计算平台开发</a></p>
<span class="section-entry-meta">07/2023 – 02/2024 · 指导老师：贾凤东（中国科学院大学）</span>

- 面向 Rb/Cs 计算场景提出基于耦合强度的自适应基组截断算法，结合异步任务处理与 Docker 标准化部署，在有限云资源下提升多用户并发响应与计算吞吐量，并将数值收敛精度由 10⁻¹ 提升至 10⁻² 量级。  
- 基于 React + FastAPI 设计前后端分离架构，将传统 ARC 3.0 原子物理仿真流程封装为可并发、可扩展的 SaaS 化计算平台，支持跃迁波长、Stark Map 与相关系数等核心能力，并完成中国科学院大学科创计划项目交付。  

<p class="section-entry-title">4. <a href="{{ site.baseurl }}/portfolio/nuclear/">基于数据分析的核物理能级结构搭建</a></p>
<span class="section-entry-meta">05/2022 – 03/2024</span>

- 面向中国原子能科学研究院（CIAE）HI-13 串列加速器实验采集的 8.15×10⁸ 条 γ-γ 两重符合事件，自研基于 SQL 检索与 Pandas 清洗的数据处理管线，将跨 12 种核素背景的原始探测信号转化为标准化分析矩阵。  
- 基于 γ-γ 符合关系与伴生核素已知能级约束完成复杂信号分离，在原有能级纲图基础上发现 17 条新射线跃迁和 6 个新能级，刷新 ⁹⁶Rh 最完善能级结构记录，并完成目标核内部结构模型的验证与修正。  

<p class="section-entry-title">5. <a href="{{ site.baseurl }}/portfolio/crossplatform/">跨平台效率工具产品开发</a></p>
<span class="section-entry-meta">02/2026 – 至今</span>

- 独立主导并交付两款覆盖 iOS、鸿蒙及安卓系统与 Web 端的应用，通过继承 Claude Code、Opencode 等搭建 App 开发工作流，实现业务逻辑在多端的高效同步和迭代。  
- 从 UI 设计、3D 视觉渲染到后端数据库完成全栈开发；项目周期内探索 AI 工具链在交付过程中的辅助提升，具备多端产品从 0 到 1 的完整交付能力。  

---

### 实习经历

<p class="section-entry-title">科大讯飞股份有限公司</p>
<p class="section-entry-title-sub">大模型实习生 · 智能座舱助手 · 12/2025 – 02/2026</p>

- 多 Agent 座舱对话（音乐/空调/手册问答）与 ReAct 工具链；RAG（BM25+BGE-M3、Milvus）；Qwen3-14B LoRA + DPO；分层记忆与自动化评测、CI/CD 回归。  

<p class="section-entry-title">猿辅导</p>
<p class="section-entry-title-sub">大模型实习生 · 英语智能助手 · 05/2025 – 07/2025</p>

- K12 英语多 Agent 协同与约 5 万条教师风格 LoRA 微调；BGE-M3 + Milvus 混合检索与 RAGAS 评测；任务完成率与解题准确率显著提升。  

<p class="section-entry-title">时代骐骥新能源科技（大同）有限公司（宁德时代）</p>
<p class="section-entry-title-sub">算法优化工程师 · 07/2024 – 09/2024</p>

- 针对大同地区重型卡车交付网络，利用空间数据分析与设备选址模型，对充电站点与交付中心进行精细化地理布局；结合物流动线与充电需求，有效降低车队空车率，提升区域补能效率与交付时效。  
- 深入参与当地政府部门沟通对接，协调新能源建设与城市交通规划融合，通过政策与多方资源整合，确保补能网络在当地快速从 0 到 1 落地。  
