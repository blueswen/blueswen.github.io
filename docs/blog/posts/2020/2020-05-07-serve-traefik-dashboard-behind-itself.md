---
categories:
- Tip
date: '2020-05-07'
tags:
- Traefik
---

# Serving Traefik’s internal dashboard behind Traefik itself 

Traefik 內建有 Dashboard 可以查看服務與設定狀態，預設會開啟在 8080 port。特定 port 時常會因為防火牆的因素被阻擋，所以可以利用 Traefik 代理自己的 Dashboard 到常用的 80 port。

```yaml
version: "2.3"

services:
  traefik:
    image: traefik:v2.2
    container_name: traefik
    command:
      - --log.level=INFO
      - --entrypoints.web.address=:80
      - --api
      - --providers.docker.exposedbydefault=false
      - --providers.docker.network=proxy
      {% raw  %}- '--providers.docker.defaultRule=Host(`{{ index .Labels "com.docker.compose.service" }}.localhost`)'{% endraw %}
      # hostname = {compose service name}.localhost
    ports:
      - "80:80"
    volumes:
      - "/var/run/docker.sock:/var/run/docker.sock:ro"
    networks:
      - proxy
    labels:
      traefik.enable: true
      traefik.http.routers.traefik.service: api@internal
      traefik.http.routers.traefik.entrypoints: web

networks:
  proxy:
    external: true
```

自定 Header 的 extension [ModHeader](https://bewisse.com/modheader/)，可以用來快速切換 HOST 或加其他 Header。

Reference:

1. [Serving Traefik’s internal dashboard behind Traefik itself](https://community.containo.us/t/serving-traefiks-internal-dashboard-behind-traefik-itself/3457/7)