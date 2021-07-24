---
layout: post
title: "[19] ARTS Share - Traefik with config hot reload"
subtitle: ""
author: "Blueswen"
header-style: text
tags:
    - ARTS
    - Share
    - Traefik
---

[Traefik](https://github.com/traefik/traefik) 支援 hot reload provider config，如果有透過 toml 設定的 Service 需要修改時，修改 toml 後即可立即生效。另外也可以將多個 Service 的 config 放在統一的資料夾中，達到動態設定多組不同的 Service。

完整範例可參考 [Traefik Template](https://github.com/Blueswen/traefik-template)

---

Traefik 的 docker-compose.yaml

```yaml
version: '3'

services:
  traefik:
    # The official v2 Traefik docker image
    image: traefik:v2.4.11
    container_name: traefik
    restart: always
    network_mode: bridge
    labels:
      traefik.enable: "true"
      traefik.http.routers.traefik.service: api@internal
      traefik.http.routers.traefik.entrypoints: http
    ports:
      # The HTTP port
      - "80:80"
    volumes:
      # So that Traefik can listen to the Docker events
      - /var/run/docker.sock:/var/run/docker.sock
      - $PWD/traefik.toml:/etc/traefik/traefik.toml
      - $PWD/conf:/etc/traefik/conf    
```

network_mode 設定為 bridge，不使用 compose 預設建立的 network，改用 docker 的 default bridge network。其他 Container 若要使用 label 將 Service 註冊於 Traefik 只需要使用 default 的 bridge network 即可。

labels:

1. traefik.enable: "true" => 讓 Traefik 代理此 container
2. traefik.http.routers.traefik.service: api@internal => traefik 的 API 功能啟用時（traefik config traefik.toml 中設定），api@internal 這個 Service 會被自動建立，提供了多個 API 供檢視 Traefik 的各種資訊 [Traefik Doc about API](https://doc.traefik.io/traefik/operations/api/#configuration)。Dashboard 啟用時也可以使用此 Service 檢視 Dashboard。
3. traefik.http.routers.traefik.entrypoints: http => traefik config traefik.toml 中定義名為 http 的 entrypoint

volumes:

1. $PWD/traefik.toml:/etc/traefik/traefik.toml => 設定 traefik 的 config
2. $PWD/conf:/etc/traefik/conf => 統一存放 file based provider 的位置

---

Traefik 的 config traefik.toml

```toml
[entryPoints]

  [entryPoints.http]
     address = ":80"

[providers]
  [providers.docker]
    defaultRule = "Host(`traefik.admin`)"
    exposedByDefault = false
  [providers.file]
    directory = "/etc/traefik/conf"
    watch = true

[api]
  dashboard = true
```

1. entryPoints.http: 定義一個名為 http 的 entryPoints，監聽 80 Port
2. providers.docker:
   1. defaultRule: 沒有定義 Rule 的 docker provider 都會使用這組 rule
   2. exposedByDefault: Container 只有在加上 traefik.enable: "true" 的 label Traefik 才會進行代理
3. providers.file:
   1. directory: config file 的目錄
   2. watch: true 表示監控檔案異動，異動發生時會 hot reload
4. api dashboard: 啟用 traefik dashboard

---

Traefik mount 的 conf 目錄中的 Service toml 範例 dynamic.toml

```toml
[http]
 [http.routers]
    [http.routers.file-based-app-router]
       entryPoints = ["http"]
       rule = "PathPrefix(`/file-based-app`)"
       service = "file-based-app"


 [http.services]
    [http.services.file-based-app.loadBalancer]
       [[http.services.file-based-app.loadBalancer.servers]]
           url = "http://[continaer file-based-app's ip]:80" # proxy url 須依實際位置調整
```

file-based-app 是 Service 名稱，可以依據需求調整

---

Reference:

1. [Serving Traefik’s internal dashboard behind Traefik itself](https://community.containo.us/t/serving-traefiks-internal-dashboard-behind-traefik-itself/3457/7)
