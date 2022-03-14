---
layout: post
title: "Why we switched from Flask to FastAPI for production machine learning"
subtitle: ""
author: "Blueswen"
header-style: text
tags:
    - ARTS
    - Review
    - Python
    - API
---

[Why we switched from Flask to FastAPI for production machine learning](https://towardsdatascience.com/why-we-switched-from-flask-to-fastapi-for-production-machine-learning-765aab9b3679)

[Cortex](https://github.com/cortexlabs/cortex) 是一個提供 ML 服務的 Infra，支援多種不同框架 TensorFlow、PyTorch、scikit-learn 等，並提供 autoscaling、rolling updates、log 管理等。在他們的 0.14 版之後將 API 的底層從 Flask 換成了 [FastAPI](https://fastapi.tiangolo.com/)，之後經歷了多次更新對於更換成 FastAPI 感到非常滿意。

以下三點是他們決定更換的原因

### 1. ML inference benefits from native async support

Cortex 從原本的依據 CPU 使用率的 autoscaling 策略，改成依據 request 的數量。但 Flask 因為沒有原生支援 async，一次只能從 queue 取出數個他能夠處理的 request 進行運算，無法得知 queue 有多少筆待處理的 request。而基於 Uvicorn 的 FastAPI 得力於 ASGI server 的特性，原生就支援 async event loop，所有 request 都會直接進到 FastAPI 中，而不會在服務外排成一個 queue，所以就能夠取到當下 request 的筆數。

### 2. Improved latency is a huge deal for inference

在實際場景中服務的速度對使用者的影響是非常巨大的，如果 Gmail 的文句自動完成功能比使用者打字慢的話，那這個功能就完全喪失了他了價值。在 [Web Framework Benchmarks](https://www.techempower.com/benchmarks/) 中 FastAPI 比 Flask 快了 300%。

### 3. FastAPI is easy to switch to—by design

從 Flask 轉換至 FastAPI 是非常輕鬆的，兩者個寫法基本上非常相似，轉換成本在轉換框架時也是一個非常重要的參考因素。

Flask API endpoint example

```python
@app.route("/hello", methods=["GET"])
def hello():
    return "Hello, World"
```

FastAPI API endpoint example

```python
@app.get("/hello")
async def hello():
    return "Hello, World"
```

### Nice to haves

除了上述的優點外，FastAPI 也提供了資料格式驗證、更友善的錯誤處理、自動生成的 API Spec 等功能。

---

Flask 做為每一個寫 Python API 的 Developer 第一個使用的 Package，完善的生態圈讓他有著幾乎不可撼動的地位。資料驗證、API Spec 等功能其實也有對應的 Package 可以使用如 [Flask-RESTX](https://flask-restx.readthedocs.io/en/latest/)。但內建非同步確實是一個很吸引人的功能，最近也是一樣有遇到無法取得 request 數量的問題，只能夠透過外部的 gateway 去取得，沒想 FastAPI 能夠輕鬆解決這個問題。後續會再多針對 FastAPI 與 ASGI Server 進行比較深入的研究，
