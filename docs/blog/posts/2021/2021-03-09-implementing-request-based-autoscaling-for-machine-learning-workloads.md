---
categories:
- Review
date: 2021-03-09
tags:
- Python
- API
- K8s
---

# Implementing request-based autoscaling for machine learning workloads

[Implementing request-based autoscaling for machine learning workloads](https://towardsdatascience.com/implementing-request-based-autoscaling-for-machine-learning-workloads-feb41572956)

[Cortex](https://github.com/cortexlabs/cortex) 是一個提供 ML 服務的 Infra，支援多種不同框架 TensorFlow、PyTorch、scikit-learn 等，並提供 autoscaling、rolling updates、log 管理等。本篇是 Cortex 團隊之所以要從 Flask 轉換成 FastAPI 的始末（[Why we switched from Flask to FastAPI for production machine learning](https://towardsdatascience.com/why-we-switched-from-flask-to-fastapi-for-production-machine-learning-765aab9b3679) ），說明他們在重新設計 autoscaling strategy 的思路。

ML inference 的一些特性讓 instance 的 scaling 相較一般服務有不同的挑戰性：

1. Model can be huge: ML 的模型有時候可能會很大，例如超過 5 GB，所以會需要更大的 instance
2. Concurrency is a pain: 單純執行一個預測可能就會使用到 instance 的所有資源，所以為了能夠負擔足夠的 Concurrency 就必須多開 instance
3. Latency can be expensive: Latency 過長會嚴重影響使用者的體驗，但很多時候只有使用 GPU 才能達到令人滿意的 Latency

基於上面的原因，為了達到更好的體驗，instance 需要夠好（有 GPU），還要夠大（Model 可能很大）。如果不巧服務非常熱門，為了解決 Concurrency 的問題，還得開很多個。這些因素都會讓 instance 的相關費用急速增長，而一套好的 autoscaling strategy，能夠讓每一分錢花得更有效益。

### Idea #1 Based on CPU utilization

CPU 是最常見的 autoscaling metrics，但在 ML 的情境裡，單純使用 CPU 進行 inference 時都會吃滿所有 CPU，而能使用 GPU 時又不太會需要使用 CPU。因此 CPU 使用量在這裡就不是一個很有效的指標。

### Idea #2 Based on inference latency

用 latency 的長短來判斷是否需要 scaling 似乎是一個滿直觀的想法，但深入研究後會發現有其他問題：

1. latency 的估計都是基於當前的模型，但模型更版時可能會讓 latency 永遠無法達到設定的值，導致無限 scaling
2. latency 難以作為 scaling down 的指標
3. 如果 API 需要呼叫第三方 API，這時第三方 API 的 latency 就會嚴重影響到原 API 的 latency

### Idea #3 Based on queue length

使用在排隊等待的 request 數量作為 scaling 也是另一個直觀的做法，同時也能作為 scaling down 的指標。他們一開始提出了一些可能的做法：

1. 建立一個 request forwarder，負責計算有多少 request 進入
2. 從 Istio 改為 [Gloo](https://github.com/solo-io/gloo)，因為 Gloo 有提供 [requests in flight](https://docs.solo.io/gloo-edge/latest/guides/observability/prometheus/metrics/) 的 metics

但兩個方案執行成本都偏高，第一項需要投入過多的開發人力，而第二項則需要大幅度調整已建立好的 Istio。因此他們把目標轉向了利用 FastAPI 與 Uvicorn 替代 Flask 與 Gunicorn，利用 Uvicorn 的 async event loop 能夠在實際執行 inference 前計算 request 數目。

使用 FastAPI 與 Uvicorn 的新架構能夠確保 autoscale 足夠的 instance，並且盡可能降低建立 instance 的費用。

最後他們也提到還可以根據 queue length 建立更細緻的 metrics，像是使用 queue length 的變動速率（對 queue length 作微分）。例如 queue length 開始快速減少，這時表示當下的 instance 足以消耗掉等待中的 request，因此不需要多開 instance，反之則需要 scale up。

---

前陣子也有在研究該如何替 Python 的 ML deployment 設定 scaling metrics，架構同樣是使用 Flask 搭配 Gunicorn。一開始也是想單純使用 CPU 或 Memory 這些基礎指標，但一樣是遇到本篇提到的 CPU 使用問題，然後因為 Python GIL 的特性，一次必定指執行一個 thread，就算 Gunicorn 更換不同的 worker type 都無法讓 CPU 或 Memory 有什麼特殊的變化。

而因為我們目前使用的 K8s 是 HPE 的 KEM，scale metrics 只能設定 CPU 或 Memory，不支援任何其他自訂 metrics，所以最後也只能暫時宣告放棄。待未來切換到 OKD 時，再來好好嘗試 queue length 的變動速率這種有趣的指標。
