---
permalink: /
title: "张博铭"
author_profile: true
redirect_from:
  - /about/
  - /about.html
---

## About Me

I am an M.S. student in Electrical Engineering at the [University of Pennsylvania](https://www.seas.upenn.edu/). I received my B.S. in Applied Physics from [Shandong University](https://www.sdu.edu.cn/). My work focuses on large language model algorithms, post-training, agent systems, deep reinforcement learning, and scientific computing.

Previously, I worked on LLM-based educational and in-car assistant systems, optical thin-film inverse design, Rydberg atom simulation platforms, and nuclear physics data analysis. I enjoy building complete research and engineering loops, from data and modeling to evaluation and deployable systems.

## Research Interests

- LLM algorithms: long-form generation, SFT/RL post-training, LLM-as-a-Judge evaluation
- Agentic AI: multi-agent routing, tool use, RAG systems, memory management
- Deep learning and reinforcement learning for optimization
- Numerical modeling and scientific computing

## Education

<div class="home-edu">
  <div class="home-edu__row">
    <div class="home-edu__logo"><img src="{{ site.url }}{{ site.baseurl }}/images/edu-upenn.png" alt="University of Pennsylvania" /></div>
    <div class="home-edu__detail">
      <strong>University of Pennsylvania</strong><span class="home-edu__time">08/2025 - Present</span><br />
      M.S. in Electrical Engineering · GPA 4.0/4.0
    </div>
  </div>
  <div class="home-edu__row">
    <div class="home-edu__logo"><img src="{{ site.url }}{{ site.baseurl }}/images/edu-sdu.png" alt="Shandong University" /></div>
    <div class="home-edu__detail">
      <strong>Shandong University</strong><span class="home-edu__time">09/2021 - 06/2025</span><br />
      B.S. in Applied Physics · GPA 89.43/100
    </div>
  </div>
</div>

## News

- [Mar. 2026] Started a Chinese long-form answer optimization project based on SFT/RL post-training and LLM-as-a-Judge evaluation.
- [Feb. 2026] Began building cross-platform productivity applications across iOS, HarmonyOS, Android, and Web.
- [Dec. 2025] Joined iFlytek as an LLM intern, working on multi-agent in-car assistant systems.
- [Aug. 2025] Started my master's study at the University of Pennsylvania.
- [Mar. 2025] Released the preprint [CL model nonlinear dynamics simulation and fractal analysis](https://arxiv.org/abs/2503.20799).

## Publications

<div class="pub-list">
  <div class="pub-item">
    <div class="pub-thumb"><img src="{{ site.url }}{{ site.baseurl }}/images/500x300.png" alt="CL model visualization" /></div>
    <div class="pub-body">
      <div class="pub-venue">arXiv preprint</div>
      <a class="pub-title" href="https://arxiv.org/abs/2503.20799">CL 模型非线性动力学仿真与分形分析</a>
      <div class="pub-authors">Boming Zhang, Yunguo Jiang</div>
      <div class="pub-desc">High-resolution numerical simulation and fractal analysis for nonlinear scalar-field dynamics.</div>
      <div class="pub-links"><a href="https://arxiv.org/abs/2503.20799">PDF</a></div>
    </div>
  </div>
</div>

## Selected Projects

<div class="pub-list">
  <div class="pub-item">
    <div class="pub-thumb"><img src="{{ site.url }}{{ site.baseurl }}/images/sft/version3_head_to_head.png" alt="LLM long answer evaluation" /></div>
    <div class="pub-body">
      <div class="pub-venue">LLM Post-training · 03/2026 - Present</div>
      <a class="pub-title" href="{{ site.baseurl }}/portfolio/sft-longanswer/">Chinese Long-form Answer Optimization for LLMs</a>
      <div class="pub-desc">Built a Qwen-based SFT/RL workflow, Chinese long-answer data filtering pipeline, and multi-model LLM-as-a-Judge evaluation system for repetition, drift, and long-sequence degradation.</div>
    </div>
  </div>

  <div class="pub-item">
    <div class="pub-thumb"><img src="{{ site.url }}{{ site.baseurl }}/images/editing-talk.png" alt="Optical thin-film inverse design" /></div>
    <div class="pub-body">
      <div class="pub-venue">Optimization · 12/2023 - 05/2024</div>
      <a class="pub-title" href="{{ site.baseurl }}/portfolio/photonics/">Learning-guided Search for Optical Multilayer Film Design</a>
      <div class="pub-desc">Modeled visible-light multilayer design as a mixed discrete-continuous optimization problem with TMM simulation, ValueNet filtering, and GA/PSO evolutionary search.</div>
    </div>
  </div>

  <div class="pub-item">
    <div class="pub-thumb"><img src="{{ site.url }}{{ site.baseurl }}/images/themes/homepage-light.png" alt="Rydberg atom simulation platform" /></div>
    <div class="pub-body">
      <div class="pub-venue">Scientific Computing · 07/2023 - 02/2024</div>
      <a class="pub-title" href="{{ site.baseurl }}/portfolio/rydberg/">Interactive Rydberg Atom Computing Platform</a>
      <div class="pub-desc">Designed a React + FastAPI platform with adaptive basis truncation, async task execution, and Docker deployment for Rb/Cs atom simulation workflows.</div>
    </div>
  </div>
</div>

## Industry Experience

<div class="experience-list">
  <div class="experience-item">
    <div class="experience-name">iFlytek</div>
    <div class="experience-role">LLM Intern · 12/2025 - 02/2026</div>
    <p>Built a multi-agent in-car assistant covering music control, climate control, and vehicle-manual QA. Improved RAG retrieval with hybrid BM25/BGE-M3 recall, reranking, Milvus-based updates, LoRA SFT, DPO, and automated evaluation.</p>
  </div>
  <div class="experience-item">
    <div class="experience-name">Yuanfudao</div>
    <div class="experience-role">LLM Intern · 05/2025 - 07/2025</div>
    <p>Developed a K12 English learning assistant with task-routing agents, question retrieval, knowledge explanation, recommendation tools, teacher-style LoRA tuning, and RAGAS-based retrieval evaluation.</p>
  </div>
  <div class="experience-item">
    <div class="experience-name">CATL-affiliated New Energy Project</div>
    <div class="experience-role">Algorithm Optimization Engineer · 07/2024 - 09/2024</div>
    <p>Used spatial data analysis and facility-location modeling to support charging-station and delivery-center planning for heavy-truck logistics in Datong.</p>
  </div>
</div>
