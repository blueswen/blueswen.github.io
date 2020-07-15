---
layout: post
title: "[12] ARTS Tip - Use Local Images in Minikube"
subtitle: ""
author: "Blueswen"
header-style: text
tags:
    - ARTS
    - Tip
    - Docker
    - K8s
---

問題：Minikube 無法使用 host 的 docker image

解法：

1. 設定環境變數 ```eval $(minikube docker-env)``` 切換到 minikube VM 的 docker 中
2. 重新 build 要使用的 docker image

Reference:

1. [How to use local docker images with Minikube?](https://stackoverflow.com/a/42564211/13582118)
2. [Reusing the Docker daemon](https://github.com/kubernetes/minikube/blob/0c616a6b42b28a1aab8397f5a9061f8ebbd9f3d9/README.md#reusing-the-docker-daemon)
