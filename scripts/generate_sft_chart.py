#!/usr/bin/env python3
"""生成 Base vs SFT 柱状图：总分、格式输出(ResponseMode)、语言结构(Structure+Org)、重复率(NonRep)

用法：
  cd scripts && pip install pandas matplotlib -q && python generate_sft_chart.py
"""
import os
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('Agg')

# 使用支持中文的字体
plt.rcParams['font.sans-serif'] = ['Arial Unicode MS', 'SimHei', 'DejaVu Sans']
plt.rcParams['axes.unicode_minus'] = False

script_dir = os.path.dirname(os.path.abspath(__file__))
repo_root = os.path.dirname(script_dir)
csv_path = os.path.join(repo_root, 'data', 'all_versions_base_sft_means_clean.csv')
out_path = os.path.join(repo_root, 'images', 'sft', 'base_sft_comparison.png')

df = pd.read_csv(csv_path)
versions = df['version'].tolist()
x = range(len(versions))
width = 0.35

fig, axes = plt.subplots(2, 2, figsize=(12, 10))

# 1. 总分 Total
ax1 = axes[0, 0]
ax1.bar([i - width/2 for i in x], df['Base_Total'], width, label='Base', color='#4A90D9')
ax1.bar([i + width/2 for i in x], df['SFT_Total'], width, label='SFT', color='#50C878')
ax1.set_ylabel('分数')
ax1.set_title('总分 (0-100)')
ax1.set_xticks(x)
ax1.set_xticklabels(versions)
ax1.legend()
ax1.axhline(y=0, color='gray', linestyle='-', linewidth=0.5)

# 2. 格式输出 ResponseMode (满分20)
ax2 = axes[0, 1]
ax2.bar([i - width/2 for i in x], df['Base_Mode'], width, label='Base', color='#4A90D9')
ax2.bar([i + width/2 for i in x], df['SFT_Mode'], width, label='SFT', color='#50C878')
ax2.set_ylabel('分数')
ax2.set_title('格式输出 / ResponseMode (满分20)')
ax2.set_xticks(x)
ax2.set_xticklabels(versions)
ax2.legend()
ax2.set_ylim(0, 22)

# 3. 语言结构 Structure + Organization
ax3 = axes[1, 0]
base_struct_org = df['Base_Struct'] + df['Base_Org']
sft_struct_org = df['SFT_Struct'] + df['SFT_Org']
ax3.bar([i - width/2 for i in x], base_struct_org, width, label='Base', color='#4A90D9')
ax3.bar([i + width/2 for i in x], sft_struct_org, width, label='SFT', color='#50C878')
ax3.set_ylabel('分数')
ax3.set_title('语言结构 (Structure + Organization, 满分45)')
ax3.set_xticks(x)
ax3.set_xticklabels(versions)
ax3.legend()
ax3.set_ylim(0, 50)

# 4. 重复率 NonRepetition (满分15)
ax4 = axes[1, 1]
ax4.bar([i - width/2 for i in x], df['Base_NonRep'], width, label='Base', color='#4A90D9')
ax4.bar([i + width/2 for i in x], df['SFT_NonRep'], width, label='SFT', color='#50C878')
ax4.set_ylabel('分数')
ax4.set_title('非重复性 NonRepetition (满分15)')
ax4.set_xticks(x)
ax4.set_xticklabels(versions)
ax4.legend()
ax4.set_ylim(0, 16)

plt.tight_layout()
os.makedirs(os.path.dirname(out_path), exist_ok=True)
plt.savefig(out_path, dpi=150, bbox_inches='tight')
print(f'Saved to {out_path}')
