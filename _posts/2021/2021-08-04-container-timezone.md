---
layout: post
title: "Container Timezone"
subtitle: ""
author: "Blueswen"
header-style: text
tags:
    - ARTS
    - Tip
    - Linux
    - Docker
    - Container
---

需求：Container OS 時區為 UTC+0，需要設定為指定時區，如台灣的 UTC+8

解決方案：依據所使用的 Linux 版本，以不同的方式設定 Timezone

### alpine

必須先安裝 ```tzdata```，並執行相關設定

Dockerfile:

```Dockerfile
FROM apline:3.14.0

RUN apk --update add tzdata && \
    apk upgrade && \
    cp /usr/share/zoneinfo/Asia/Taipei /etc/localtime && \
    echo "Asia/Taipei" > /etc/timezone
```

### 非 alpine 版本

只需設定環境變數 ```TZ```

Dockerfile:

```Dockerfile
FROM debian:buster

EVN TZ=Asia/Taipei
```

或者執行 Container 時直接設定

```sh
docker run -e "TZ=Asia/Taipei" debian:buster
```

Reference:

1. [使用 Dockerfile 設定 Container 時區](https://cynthiachuang.github.io/Change-Timezone-in-Dockerfile/)
2. [【筆記】Docker Timezone 設定](https://greddyblogs.gitlab.io/2020/01/31/dockerTimeZone/)
3. [Explanation of the “--update add” command for Alpine Linux](https://stackoverflow.com/a/43682030)
