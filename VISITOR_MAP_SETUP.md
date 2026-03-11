# Visitor Map Real Data Setup

当前页脚访客地图已经支持：

- 使用 `/_data/visitor_map.yml` 里的历史基线数字作为起点
- 通过 `assets/data/visitor-map-live.json` 叠加 Umami 的真实新增访问
- 使用 GitHub Actions 自动定时同步国家热力图数据
- 在页面前端注入 Umami 埋点脚本，开始真实记录新的访客访问

## 最省事方案：Umami Cloud

这是目前最推荐的路线，因为不用自己养服务器。

你需要在 Umami Cloud 中拿到：

- `Website ID`
- `API Key`

## 你需要先修改的文件

打开 `/_data/visitor_map.yml`，填写：

```yml
tracking:
  enabled: true
  script_url: "https://cloud.umami.is/script.js"
  website_id: "你的 website id"
  host_url: ""
  domains: "zhangbomingnice.github.io"
```

说明：

- `script_url`：Umami 的埋点脚本地址；用 Umami Cloud 时保持默认即可
- `website_id`：Umami 后台里这个网站的 ID
- `host_url`：只有在你把脚本和数据上报地址拆开时才需要，通常留空
- `domains`：限制只在指定域名生效，建议填你的站点域名

## 你需要配置的 GitHub Secrets

在仓库的 `Settings -> Secrets and variables -> Actions` 中添加：

### Umami Cloud

- `UMAMI_WEBSITE_ID`
  - 例：`xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx`
- `UMAMI_API_KEY`
  - 在 Umami Cloud 里生成

可选：

- `UMAMI_API_BASE_URL`
  - 默认不填即可，脚本会使用 `https://api.umami.is/v1`
- `UMAMI_START_AT`
  - 默认值：`2000-01-01T00:00:00Z`
- `UMAMI_END_AT`
  - 默认值：当前时间

### 自托管 Umami

如果你以后改成自托管，也可以用下面这组：

- `UMAMI_API_BASE_URL`
  - 例：`https://analytics.example.com/api`
- `UMAMI_WEBSITE_ID`
- `UMAMI_USERNAME`
- `UMAMI_PASSWORD`

## 启动方式

配置好后：

1. 打开 GitHub Actions
2. 运行 `Update Visitor Map Data`
3. 等 workflow 成功后，`assets/data/visitor-map-live.json` 会被自动更新并提交
4. GitHub Pages 部署完成后，网页底部地图就会显示真实新增访客数据

## 数据显示逻辑

最终页面显示的是：

`历史基线数据 + Umami 新增真实访问`

也就是说，你现在已经在页面上的这些数字不会清零，而是继续往上累计。
