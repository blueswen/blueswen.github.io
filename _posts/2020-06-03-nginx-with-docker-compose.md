---
layout: post
title: "[8] ARTS Tip - Nginx with Docker Compose"
subtitle: ""
author: "Blueswen"
header-style: text
tags:
    - ARTS
    - Tip
    - Nginx
    - Docker
    - jupyter notebook
---

使用 Docker Compose 快速啟動一個 Nginx Server 做靜態伺服器與 Proxy。若要做其他 container 的 Proxy 必須在同一個 Network 下，可以直接都設定成 Docker 的預設 bridge network。設定 proxy 時如果遇到 gateway timeout 基本上就是網路沒有通，優先檢查 container 間的網路設定。

以用 Nginx 做 jupyter notebook container proxy 為例：

### nginx docker-compose yaml

```yaml
version: '2.3'
services:
  web:
    image: nginx:1.18.0
    ports:
      - 80:80
    network_mode: bridge
    volumes:
      - ./conf.d:/etc/nginx/conf.d
      - ./log:/var/log/nginx
      - ./www:/var/www
```

```network_mode: bridge``` 使用 Docker 預設的 Network，network name 即為 bridge，執行 ```docker run``` 時的 network 就是 bridge。

### jupyter notebook docker-compose yaml

```yaml
version: '2.3'
services:
  notebook:
    image: ufoym/deepo:all-py36-jupyter
    ports:
      - 8080:8888
    network_mode: bridge
    volumes:
      - ./root:/root
    command: jupyter notebook --no-browser --ip=0.0.0.0 --allow-root --notebook-dir='/root' --NotebookApp.base_url='/notebook/'
```

```ports: 8080:8888```，若只需要從 proxy 進入則可以不設定 expose，在做 proxy 時是認 container 內使用的 port，與 expose 在 host 的 port 無關。

```network_mode: bridge``` 使用 Docker 預設的 Network，network name 即為 bridge，執行 ```docker run``` 時的 network 就是 bridge。

```NotebookApp.base_url``` 可以設定 prefix，跟 nginx 的 location 設定一樣就不用再設定移除 prefix，可以避免各種頁面讀取 static file（css, js ...）的問題，

### nginx config

設定加在 ```conf.d/default.conf``` 中

```txt
server {
    client_max_body_size 100M;

    listen         80 default_server;

    location /notebook {
        proxy_pass http://172.17.0.4:8888;
    }

    location / {
        root   /var/www/;
    }
}
```

```client_max_body_size```，可以設定 client 上傳檔案的最大限制，預設為 1 M。

container ip 可以透過 ```docker inspect [container-name]``` 或 ```docker inspect [container-name] -f "{{json .NetworkSettings.Networks }}"``` 查詢。

### update nginx setting

更新 nginx config 後需要重新載入設定

```bash
nginx -s reload
```

Reference:

1. [How to NGINX Reverse Proxy with Docker Compose](https://dzone.com/articles/how-to-nginx-reverse-proxy-with-docker-compose)
2. [How to Configure NGINX](https://www.linode.com/docs/web-servers/nginx/how-to-configure-nginx/)
3. [How to Limit File Upload Size in Nginx](https://www.tecmint.com/limit-file-upload-size-in-nginx/)
4. [How to join the default bridge network with docker-compose v2?](https://stackoverflow.com/questions/43754095/how-to-join-the-default-bridge-network-with-docker-compose-v2)
