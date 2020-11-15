---
layout: post
title: "[14] ARTS Share - Docker Multi-Stage Build"
subtitle: ""
author: "Blueswen"
header-style: text
tags:
    - ARTS
    - Share
    - Docker
---

在 CI 的過程中許多專案都會有 compile 或 build 的需求，而基於最小化的 Docker Image 的原則，建置時期相依的套件並不會一同打包進成品的 Image 中。在這種情境下常見的做法是透過 Pipeline 切分成兩段處理，第一步先利用已有的建置環境 Image compile 或 build 原始檔，第二步再將成品打包至 Runtime 的 Image 中。

不過利用 Pipeline 的缺點是會相依 shell script 或其他 CI 工具，因此 Docker 在 Docker 17.05+ 開始提供了 [Multi-Stage Build](https://docs.docker.com/develop/develop-images/multistage-build/) 的功能，能夠將多階段的 Docker Image 處理定義在一個 Dockerfile 中。

使用方法為透過 ```FROM [compile time image] AS [temp image]``` 的 ```AS``` 產生暫時的 Image，該 Image 可以被下一個階段的 Image 引用(FROM)，或是以 ```COPY --from=[temp image] /source /dist``` 的方式取出要用的成品。

```dockerfile
FROM [compile time image] AS [temp image]
WORKDIR /workspace
RUN touch artifact

FROM [runtime image]
WORKDIR /workspace
COPY  --from=[temp image] /workspace/artifact .
CMD ls -lha artifact
```

由於整份 Dockerfile 仍然是屬於同一個 build，因此如果有設定 ```.dockerignore``` 所有 Image 的 ```COPY``` 都是會被影響到的，這點在使用上時需多加注意。

以下提供 Golang 與 Vue.js 的兩個 Dockerfile 範例，相關程式碼可參考 [docker-multi-stage-build](https://github.com/Blueswen/docker-multi-stage-build)。

### Golang

```dockerfile
FROM golang:alpine3.12 AS builder
WORKDIR /workspace
COPY . /workspace/
RUN go build -o hello-world

FROM busybox:1.32.0
WORKDIR /workspace
COPY  --from=builder /workspace/hello-world .
CMD ./hello-world
```

### Vue.js

```dockerfile
FROM node:15.1.0-slim AS builder
WORKDIR /workspace
COPY ./hello-world/ /workspace/
RUN npm install && npm run build

FROM nginx:1.19.4-alpine
COPY  --from=builder /workspace/dist/ /usr/share/nginx/html/
```

Reference:

1. [透過 Multi-Stage Builds 改善持續交付流程](https://tachingchen.com/tw/blog/docker-multi-stage-builds/)
