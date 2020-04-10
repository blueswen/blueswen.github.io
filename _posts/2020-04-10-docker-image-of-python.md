---
layout: post
title: "[0] ARTS Share - The best Docker base image for your Python application"
subtitle: ""
author: "Blueswen"
header-style: text
tags:
    - ARTS
    - Share
    - Docker
    - python
---

[The best Docker base image for your Python application](https://pythonspeed.com/articles/base-image-python-docker-images/)

一般 Docker Base Image  大多數文章都會推薦使用 Alpine Linux，因為非常的小，但實際上用起來會遇到許多的問題，如 Docker Build 很慢，Dependencies 東缺西缺，因此作者不建議使用 Alpine。

文中列出在選擇 Base Image 時應考量到的幾個重點

1. 穩定性：OS 所提供的 library 跟架構不會隨著版本更動有大幅變動，否則基底更新時無法使用相同的方式建置 Image
2. 安全性更新：當 OS 有安全漏洞時能夠及時地更新
3. 工具相依性：有一些基礎的 Tool (e.g. gcc, g++)，也要能支援一些比較少見的 Tool
4. 新版的 Python：可以省去自己安裝 Python 的步驟
5. 越小越好：在部署服務的能夠有更好的效能

據此作者給了兩種建議選項

1. 以 Ubuntu LTS、CentOS、Debian 為基底再去安裝所需的 Python
2. [Docker Hub](https://hub.docker.com/_/python) 上提供的 Python Image，如 slim-buster 是 Debian Buster 輕量的版本

之前都使用 Ubuntu 為 base，還要另外自己安裝特定版本的 python，目前使用了 slim-buster 的版本作為 base image，除了 make 是沒有內建需要額外安裝外，使用體驗很不錯，安裝 tensorflow 也很順利不用額外多安裝什麼東西。
