---
layout: archive
title: "项目与实习"
permalink: /experience/
author_profile: true
---

{% include base_path %}

## 项目经历

<p class="section-entry-title">1. <a href="{{ site.baseurl }}/portfolio/sft-longanswer/">针对于中文（孤立语）的LLM 长回答优化</a></p>
<span class="section-entry-meta">03/2026 – 至今</span>

* 面向中文长回答生成中结构松散、主题漂移、重复回环与长序列质量衰退等问题，探究长序列后半段稳定性与 CoT 在长文本回答中的外推表现。
* 数据侧：使用 Hugging Face 约 4.4 万条高质量原始语料，完成中文长回答问题筛选与基于 LLM judge 的长回答质量评估，剔除字符型/段落型/语义型重复及无有效信息增量样本，保障训练数据质量。
* 系统侧：基于 Qwen3.5-3B 搭建中文长回答后训练 workflow，覆盖训练样本构建、SFT 微调、推理对比、离线评测与版本迭代；围绕 LoRA、max_length、learning rate、decode 策略等变量做系统对照，定位重复、文本结构性与长序列回答质量等核心瓶颈。
* 评测侧：构建 LLM-as-a-Judge 的 agent，引入 MiniMax 2.7、Gemini Pro 3、GLM 5.1 作为裁判，结合 N-gram 重复率、结构统计、风格检测、多轮评审、中位数聚合与规则后修正，对重复、拖尾、结构失稳与主题漂移做系统分析与误差归因。
* 扩展实验：在控制变量下研究 prompt 长度对长回答性能的影响（无关 token、空格填充、padding mask 等），比较 Qwen3.5-9B、MiniMax M2.7-Lightning、K2.5-8B 在长文本条件下的质量变化；并探索 RL-friendly SFT 与 CoT、大纲规划、分段生成等对结构稳定性、信息密度与 CoT 外推的影响。

<p class="section-entry-title">2. <a href="{{ site.baseurl }}/portfolio/photonics/">面向混合离散-连续设计的光学多层膜逆向学习驱动搜索框架</a></p>
<span class="section-entry-meta">12/2023 – 05/2024</span>

* 面向可见光波段多层膜结构，将材料库选择（离散）、层厚（连续）与不可导目标建模为 Mixed Discrete-continuous Optimization（MDO）问题，构建结合 TMM 物理评估、神经网络筛选与 GA/PSO 的学习驱动逆向设计框架。
* 基于 Transfer Matrix Method（TMM）实现多层膜透过谱前向评估，在物理闭环上接入 GA/PSO 优化器，对高维、非凸、不可导搜索空间中的候选结构迭代搜索与性能优化。
* 设计 ValueNet 作为学习驱动的候选筛选模块：对可变层数做固定长度编码（最大层数对齐、材料 one-hot、厚度归一化、mask、目标特征拼接），结合回归误差与长度归一化损失，强化对随机过程中高潜力 seed 的识别与排序。
* 构建 ValueNet-screening → GA/PSO 协同流程：从大规模候选池筛选高潜力初值，再经真实物理评估与演化优化精修；并设计统一 benchmark，在相同目标、约束与计算预算下公平比较 pure GA、pure PSO 与 ValueNet-assisted 方案。
* 在给定材料库与多角度约束下，以 450–500 nm 防蓝光任务为例，得到约 11 层、总厚度约 630 nm 的代表性设计，目标区平均透过率约 2.3%；光谱与优化轨迹可视化验证了方法在复杂光学设计空间中的有效性。[代码仓库](https://github.com/zhangbomingnice/1Dthinfilm_design)

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

<p class="section-entry-title">科大讯飞股份有限公司</p>
<p class="section-entry-title-sub">大模型实习生 · 智能座舱助手 · 12/2025 – 02/2026</p>

* 面向智能汽车座舱场景，搭建基于大语言模型的多 Agent 对话系统，覆盖音乐控制、空调控制与车辆手册问答三类任务，缓解传统车机交互僵化、复杂指令理解弱、多轮一致性不足等问题。
* 基于 LangChain 实现主 Agent + 专用子 Agent 架构与意图路由；音乐/空调 Agent 集成车控工具；问答 Agent 对接车辆手册知识库，采用 ReAct 完成工具选择、参数提取与执行闭环。
* RAG：语义切分与父子切块保留章节上下文；BM25 与 BGE-M3 的 RRF 混合召回，经 BGE-Reranker 精排；Milvus 管理向量库并支持增量更新。
* 基于约 5000 条高质量指令数据对 Qwen3-14B 进行 LoRA 微调，工具调用成功率由 87.3% 提升至 95.2%，意图识别准确率由 91.2% 提升至 93.5%；进一步采用 DPO，两项指标分别达 98.1% 与 98.6%。
* 分层记忆（近期约 20 轮对话缓存 + 长期向量记忆）与滑动窗口压缩、关键信息动态注入；构建约 1200 条测试集与大模型 judge 自动化评测及 CI/CD 回归，形成搭建—优化—评测的完整工程 pipeline。

<p class="section-entry-title">猿辅导</p>
<p class="section-entry-title-sub">大模型实习生 · 英语智能助手 · 05/2025 – 07/2025</p>

* 面向 K12 英语辅导，设计多 Agent 协同架构：主 Agent 负责任务分发；解题 Agent（历史题检索、考点提取）、推题 Agent（错题驱动举一反三）与知识解答 Agent（语法词汇科普）分工协作，并引入记忆机制保持对话连贯。
* 收集并清洗约 5 万条英语教师真实对话数据，采用 LoRA 微调 Qwen3-14B，人工评估中教师口吻一致性由 62% 提升至 89%。
* 使用 BGE-M3 对约 2.3 万条题干与知识点向量化并存入 Milvus；检索阶段 RRF 融合语义与 BM25 关键词召回，再经 BGE-Reranker 精排；RAGAS 评测下混合检索+精排较单路语义检索命中率、MRR、Context Relevancy 等指标显著提升。
* 完善解题/推题/知识解答的工具链与分步讲解流程；通过人工评估与 BLEU、Rouge 及 RAGAS 等多维指标验证，整体任务完成率约 94.3%，工具调用准确率约 91.8%，解题准确率约 87.2%（对比微调前约 76.5%）。

<p class="section-entry-title">时代骐骥新能源科技（大同）有限公司（宁德时代）</p>
<p class="section-entry-title-sub">算法优化工程师 · 07/2024 – 09/2024</p>

* 针对大同地区重型卡车交付网络，利用空间数据分析与设备选址模型，对充电站点与交付中心进行精细化地理布局；结合物流动线与充电需求，有效降低车队空车率，提升区域补能效率与交付时效。
* 深入参与当地政府部门沟通对接，协调新能源建设与城市交通规划融合，通过政策与多方资源整合，确保补能网络在当地快速从 0 到 1 落地。
