#!/usr/bin/env python3
"""生成 Version 3 两组 head-to-head 对比图：v3_main vs v2.7、v3_bestdecode vs v2.8

用法：cd scripts && pip install matplotlib -q && python generate_v3_chart.py
"""
import os
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import matplotlib
matplotlib.use('Agg')

plt.rcParams['font.sans-serif'] = ['Arial Unicode MS', 'SimHei', 'DejaVu Sans']
plt.rcParams['axes.unicode_minus'] = False

script_dir = os.path.dirname(os.path.abspath(__file__))
repo_root = os.path.dirname(script_dir)
out_path = os.path.join(repo_root, 'images', 'sft', 'version3_head_to_head.png')
out_delta = os.path.join(repo_root, 'images', 'sft', 'version3_delta.png')

label6 = ['回复模式', '结构', '组织', '流畅度', '非重复', '任务契合']

# v3_main vs v2.7
b1_6 = [19.975, 22.162, 17.912, 14.325, 13.025, 4.598]
v1_6 = [20.0, 22.35, 18.125, 14.45, 13.35, 4.67]
b1_t, v1_t = 91.997, 92.945

# v3_bestdecode vs v2.8
b2_6 = [19.605, 21.888, 18.063, 14.31, 14.722, 4.625]
v2_6 = [19.553, 21.79, 17.982, 14.302, 14.692, 4.592]
b2_t, v2_t = 93.23, 92.91

x6 = range(6)
width = 0.35

fig = plt.figure(figsize=(14, 7))
gs = gridspec.GridSpec(2, 2, height_ratios=[2.2, 1], hspace=0.35, wspace=0.25)

# (0,0) 六维度 v3_main vs v2.7
ax = fig.add_subplot(gs[0, 0])
ax.bar([i - width/2 for i in x6], b1_6, width, label='v2.7', color='#4A90D9')
ax.bar([i + width/2 for i in x6], v1_6, width, label='v3_main', color='#E67E22')
ax.set_ylabel('分数')
ax.set_title('v3_main vs v2.7 — 六维度（600 条）')
ax.set_xticks(x6)
ax.set_xticklabels(label6, rotation=22, ha='right')
ax.legend(loc='upper right', fontsize=9)
ax.set_ylim(0, 26)

# (0,1) 六维度 v3_bestdecode vs v2.8
ax = fig.add_subplot(gs[0, 1])
ax.bar([i - width/2 for i in x6], b2_6, width, label='v2.8', color='#27AE60')
ax.bar([i + width/2 for i in x6], v2_6, width, label='v3_bestdecode', color='#9B59B6')
ax.set_ylabel('分数')
ax.set_title('v3_bestdecode vs v2.8 — 六维度（600 条）')
ax.set_xticks(x6)
ax.set_xticklabels(label6, rotation=22, ha='right')
ax.legend(loc='upper right', fontsize=9)
ax.set_ylim(0, 26)

# (1,0) 总分
ax = fig.add_subplot(gs[1, 0])
ax.bar([0 - width/2], [b1_t], width, label='v2.7', color='#4A90D9')
ax.bar([0 + width/2], [v1_t], width, label='v3_main', color='#E67E22')
ax.set_ylabel('总分')
ax.set_xticks([0])
ax.set_xticklabels(['总分 (0–100)'])
ax.legend(fontsize=9)
ax.set_ylim(88, 95)
ax.set_title('总分对比：v3_main vs v2.7')

# (1,1) 总分
ax = fig.add_subplot(gs[1, 1])
ax.bar([0 - width/2], [b2_t], width, label='v2.8', color='#27AE60')
ax.bar([0 + width/2], [v2_t], width, label='v3_bestdecode', color='#9B59B6')
ax.set_ylabel('总分')
ax.set_xticks([0])
ax.set_xticklabels(['总分 (0–100)'])
ax.legend(fontsize=9)
ax.set_ylim(88, 95)
ax.set_title('总分对比：v3_bestdecode vs v2.8')

plt.savefig(out_path, dpi=150, bbox_inches='tight')
print(f'Saved to {out_path}')

# Delta 图（七项含总分，同一 Δ 轴）
x7 = range(7)
label7 = label6 + ['总分']
delta1 = [v1_6[i] - b1_6[i] for i in range(6)] + [v1_t - b1_t]
delta2 = [v2_6[i] - b2_6[i] for i in range(6)] + [v2_t - b2_t]
colors1 = ['#2ECC71' if d >= 0 else '#E74C3C' for d in delta1]
colors2 = ['#2ECC71' if d >= 0 else '#E74C3C' for d in delta2]

fig2, axes2 = plt.subplots(1, 2, figsize=(13, 4.2))
axes2[0].bar(x7, delta1, color=colors1, edgecolor='gray', linewidth=0.4)
axes2[0].axhline(0, color='black', linewidth=0.9)
axes2[0].set_xticks(x7)
axes2[0].set_xticklabels(label7, rotation=22, ha='right')
axes2[0].set_ylabel('Δ (V3 − 基线)')
axes2[0].set_title('v3_main − v2.7（均值差）')
axes2[1].bar(x7, delta2, color=colors2, edgecolor='gray', linewidth=0.4)
axes2[1].axhline(0, color='black', linewidth=0.9)
axes2[1].set_xticks(x7)
axes2[1].set_xticklabels(label7, rotation=22, ha='right')
axes2[1].set_ylabel('Δ (V3 − 基线)')
axes2[1].set_title('v3_bestdecode − v2.8（均值差）')
plt.tight_layout()
plt.savefig(out_delta, dpi=150, bbox_inches='tight')
print(f'Saved to {out_delta}')
