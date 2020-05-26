---
layout: post
title: "[7] ARTS Review - How we implemented RED and USE metrics for monitoring"
subtitle: ""
author: "Blueswen"
header-style: text
tags:
    - ARTS
    - Review
    - SRE
---

[How we implemented RED and USE metrics for monitoring](https://medium.com/thron-tech/how-we-implemented-red-and-use-metrics-for-monitoring-9a7db29382af)

本文介紹 Monitoring 的基本知識，以及說明他們從原本的工具遷移至 Prometheus 跟 Grafana 的原因。

The Four Golden Signals，四項由 Google 提出的系統監控指標，出自 [Site Reliability Engineering: How Google Runs Production Systems](https://landing.google.com/sre/sre-book/toc/index.html) Monitoring Distributed Systems 章節：

1. Latency : 每個 request 執行的時間
2. Traffic : 有多少流量在使用系統
3. Errors : 錯誤的比率
4. Saturation : 系統的飽和度，離系統資源耗盡多近

作者的團隊並沒有直接選用 The Four Golden Signals，而是選用從這四點衍生出來的 RED Method 與 USE Method。

[RED Method](https://thenewstack.io/monitoring-microservices-red-method/)，主要應用於微服務架構中，關注服務的狀態：

1. Rate: 每秒服務收到的 request
2. Error: 每秒失敗的 request 數量
3. Duration: 每個 request 執行的時間

三個指標非常直觀，基本上所有微服務都可以測量這三個指標。有共同的指標就可以使用相同的管理方式，從監控方式到維運組的應對方案的設計。降低維運的複雜性能夠減輕認知負荷(cognitive load)，避免在高壓的環境下導致更嚴重的錯誤。

[USE Method](http://www.brendangregg.com/usemethod.html) 關注 infrastructure 的狀態，如網路、CPU、記憶體用量等：

1. Utilization: 資源的使用量
2. Saturation: 資源使用的飽和程度
3. Errors: 錯誤事件的數量

透過 USE Method 可以發現系統上的瓶頸，再採取適當的措施，如調整系統參數或增加資源。

在遷移至新的監控系統時他們面臨到兩個挑戰：

1. 因為他們的監控系統是 Container Based，但 Container 原生沒有提供 persistent storage，因此他們選用了 [REX-Ray](https://github.com/rexray/rexray) 讓 Docker 能有 persistent storage。不過我認為這個問題在 K8s 使用 persistent volume 應該就可以解決了。
2. Grafana 原生沒有提供 API 可以建立 Dashboard 與設定 alerts，這產生了大量的手動設定工作。[grafanalib](https://github.com/weaveworks/grafanalib) 這個 python 的 package 可以直接用 python script 設定與版控 Grafana Dashboard。
