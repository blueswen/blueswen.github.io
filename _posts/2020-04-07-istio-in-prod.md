---
layout: post
title: "[0] ARTS Review - Istio in Production"
subtitle: ""
author: "Blueswen"
header-style: text
tags:
    - ARTS
    - Review
    - K8s
---

[Everything We Learned Running Istio In Production — Part 1](https://engineering.hellofresh.com/everything-we-learned-running-istio-in-production-part-1-51efec69df65)  
[Everything We Learned Running Istio In Production — Part 2](https://engineering.hellofresh.com/everything-we-learned-running-istio-in-production-part-2-ff4c26844bfb)

分享導入 Istio 的一些做法與建議

1. Istio 提供許多功能，先 focus 在一兩個最需要的，再逐步加入其他功能
2. 不是所有 application 都與 Istio 相容，[checklist](https://github.com/istio/istio/issues/14743)
3. Istio 的導入數量作為 OKR
