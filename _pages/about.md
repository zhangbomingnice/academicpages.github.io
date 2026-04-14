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
<p class="section-entry-title-sub">大模型实习生 · 12/2025 – 02/2026</p>

<p><strong>项目名称：</strong>智能座舱助手</p>

<p><strong>项目背景：</strong>面向智能汽车座舱场景，为解决传统车机交互僵化、复杂指令理解低、开放问答与多轮交互一致性上的不足，设计并实现了一套基于大语言模型的多Agent 对话系统，覆盖音乐控制、空调控制与车辆手册问答三类核心任务，提升座舱交互性和准确性。</p>

<p><strong>项目内容：</strong></p>

1. **多Agent 架构：** 基于LangChain 搭建主Agent + 专用子Agent 的多Agent 架构，构建意图路由与三大主要Agent（音乐，空调，问答）。其中音乐Agent 集成切歌、上下首等控制工具；空调Agent 集成温度与风量调节工具；问答Agent 对接车辆手册知识库，引入ReAct 范式实现工具选择、参数提取与执行闭环，提升复杂车控指令的解析与调用准确性。
2. **RAG 问答优化：** 面向车辆手册问答场景构建RAG 检索优化模块，采用「语义切分」以及「父子切块分」方式保留章节上下文信息，并设计BM25 与BGE-M3 的RRF 混合召回流程，经BGE-Reranker 精排后提升检索质量；基于Milvus 管理向量数据库，支持增量更新，使问答系统能够兼顾知识覆盖、检索精度与增量维护能力。
3. **模型SFT 和RL：** 针对车控指令的多样性与工具调用鲁棒性问题，构建5000 条高质量指令微调数据集，基于Qwen3-14B 基座模型进行LoRA 微调，工具调用成功率从87.3% 提升至95.2%，意图识别准确率从91.2% 提升至93.5%；并进一步采用DPO 进行优化，工具调用成功率以及意图识别准确率分别达98.1% 和98.6%。
4. **多轮记忆管理：** 设计分层记忆机制，包括短期对话缓存（记录最近的20 轮对话）和长期向量记忆数据库（存储用户偏好以及关键交互信息），通过滑动窗口压缩以及关键信息动态抽取注入prompt，有效的解决长对话中的上下文遗忘问题，提升多轮交互一致性。
5. **评估体系建立：** 建立覆盖意图识别准确率、工具调用成功率、问答准确率等核心指标的评估体系，构建1200 条测试集并引入大模型judge 完成自动化评测，实现CI/CD 回归；通过对比实验验证混合检索、重排序、记忆管理与后训练优化对整体系统性能的贡献，形成从系统搭建、模型优化到评测验证的完整工程pipline 闭环。

<p class="section-entry-title">猿辅导</p>
<p class="section-entry-title-sub">大模型实习生 · 05/2025 – 07/2025</p>

<p><strong>项目名称：</strong>英语智能助手</p>

<p><strong>项目背景：</strong>面向K12 英语辅导场景，设计并开发了一套基于多Agent 协同的英语教学助手，通过主Agent 调度、子Agent 分工执行、结合RAG 检索与记忆管理，实现面向英语学习精准解题和知识答疑。</p>

<p><strong>项目内容：</strong></p>

1. **多Agent 结构设计：** 设计面向英语教学任务的多Agent 协同架构，由主Agent 负责用户请求理解与任务分发，包含解题Agent（负责选择题答疑，调用历史题目检索和知识点提取工程）、推题Agent（基于学生错题以及学生个人信息，调用知识库对相似题目进行举一反三）与知识解答Agent（针对语法、词汇等知识点进行科普，调用知识介绍库检索工具）。引入记忆管理机制记录用户历史交互，实现上下文连贯的对话式辅导。
2. **模型微调：** 面向教师风格教学对话，我们收集并清洗英语教师真实对话数据（涵盖解题思路讲解、知识点答疑、错题分析等），构造5 万条指令微调数据集，采用LoRA 高效微调技术对Qwen3-14B 进行微调。人工评估中教师口吻一致性从62% 提升至89%。
3. **RAG 构建与检索优化：** 使用BGE-M3 模型对2.3 万条英语题干及知识点进行向量化，存入Milvus 向量数据库并绑定对应答案与解析。检索阶段采用RRF 策略，融合BGE-M3 语义召回与BM25 关键词召回结果，再经BGE-Reranker 模型精排。经RAGAS 框架评测，混合检索+ 精排相比单路语义检索，命中率从82.4% 提升至94.7%，MRR 从76.3% 提升至91.2%，Context Relevancy 达92.5%。
4. **Agent 工具链：** 解题Agent 先通过历史题目检索工具查重，再调用知识点提取工具识别考点，结合检索到的相似题与解析生成分步讲解；推题Agent 基于错题提取薄弱知识点，结合学生年级信息调用题目知识库查询工具，检索难度适配的推荐题并生成推题说明；知识解答Agent 调用知识介绍库获取结构化知识点后组织语言进行通俗化讲解。
5. **系统评测：** 模型微调效果通过人工评估与自动化指标（BLEU、Rouge）对比验证；RAG 检索质量采用RAGAS 评测框架，从检索命中率、上下文相关性、答案忠实度等指标评估；整体任务完成率达94.3%，工具调用准确率91.8%，解题准确率87.2%（对比微调前76.5%）。

<p class="section-entry-title">时代骐骥新能源科技（大同）有限公司（宁德时代）</p>
<p class="section-entry-title-sub">算法优化工程师 · 07/2024 – 09/2024</p>

1. 针对大同地区重型卡车交付网络，利用空间数据分析与设备选址模型，对充电站点与交付中心进行精细化地理布局；结合物流动线与充电需求，有效降低车队空车率，提升区域补能效率与交付时效。  
2. 深入参与当地政府部门沟通对接，协调新能源建设与城市交通规划融合，通过政策与多方资源整合，确保补能网络在当地快速从 0 到 1 落地。  

---

### 论文发表

**CL 模型非线性动力学仿真与分形分析**（指导老师：姜云国，山东大学）

- **高维度数值模拟：** 基于 MATLAB 自主研发高性能非线性系统数学建模，集成 RK4（四阶龙格-库塔）与二阶有限差分算法，解决复杂标量场演化中的非线性迭代与收敛问题；系统支持动态能量密度追踪与智能截断机制，实现对孤子对碰撞过程中高维能量交换模式的精准建模与逻辑还原。  
- **非线性特征提取：** 利用极高分辨率参数空间搜索与多层次可视化分析，挖掘非线性系统演化中的分形结构并首次发现 CL 模型参数与出射速度之间的自相似模式，并定量求解 Hausdorff 维数。  

**arXiv:** [2503.20799](https://arxiv.org/abs/2503.20799)
