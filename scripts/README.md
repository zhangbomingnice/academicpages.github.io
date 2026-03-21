# 脚本说明

## generate_sft_chart.py

生成 SFT 项目详情页的 Base vs SFT 柱状图（总分、格式输出、语言结构、重复率）。

**依赖：** `pip install pandas matplotlib`

**运行：**
```bash
cd scripts && pip install pandas matplotlib -q && python generate_sft_chart.py
```

输出：`images/sft/base_sft_comparison.png`

---

## generate_v3_chart.py

生成 Version 3 两组对照图：`v3_main vs v2.7`、`v3_bestdecode vs v2.8`（均值柱状图 + Δ 图）。

**依赖：** `pip install matplotlib`

**运行：**
```bash
cd scripts && pip install matplotlib -q && python generate_v3_chart.py
```

输出：`images/sft/version3_head_to_head.png`、`images/sft/version3_delta.png`
