---
categories:
- Review
date: 2020-06-02
tags:
- Go
---

# Why we’re writing machine learning infrastructure in Go, not Python

[Why we’re writing machine learning infrastructure in Go, not Python](https://medium.com/@calebkaiser/why-were-writing-machine-learning-infrastructure-in-go-not-python-38d6a37e2d76)

[Cortex](https://github.com/cortexlabs/cortex) 是一個提供 ML 服務的 Infra，支援多種不同框架 TensorFlow、PyTorch、scikit-learn 等，並提供 autoscaling、rolling updates、log 管理等。平台有 87.5% 使用 Go 編寫，本篇文章說明選擇 Go 的原因。

### 1. Concurrency is crucial for machine learning infrastructure

使用者僅透過 Cortex 部署服務，並不會真正接觸到服務部署的 API，如 K8s API 或 AWS API，這些部署與監控的 API 操作都由 Cortex 處理。大量的 API 操作所產生的併發可能會導致 race condition 以及效能問題，Go 提供的 Goroutines 能夠有效管理 threads。

### 2. Building a cross-platform CLI is easier in Go

Go 可以根據不同環境編譯 Binary 執行檔，不再需要擔心相依套件或是執行環境。

### 3. The Go ecosystem is great for infrastructure projects

許多的 Infra projects 都適用 Go 撰寫，如 kubectl、minikube、helm、kops 等。

### 4. Go is just a pleasure to work with

與 Python 相比 Go 相對難上手了一點，但強型別與靜態語言能夠相對少寫出一些有 Bug 的 Code。

---

最近也開始學 Go 並寫了一些小工具，不用考慮相依套件與執行環境真的是很棒的優點，在 K8s 中如果要掛一個 sidecar 只需使用 busybox 當底就可以，大大降低了資源消耗。學習上幾乎沒有什麼太大的困難，不過指標與用 Structs 實現 OOP 讓人想起以前學 C 跟 C++ 的日子。

Cortex 包裝服務跟部署的方式滿簡單的，值得花時間研究一下，部署範例如下：

```python
# predictor.py

class PythonPredictor:
    def __init__(self, config):
        self.model = download_model()

    def predict(self, payload):
        return self.model.predict(payload["text"])
```

```yaml
# cortex.yaml

- name: sentiment-classifier
  predictor:
    type: python
    path: predictor.py
  compute:
    gpu: 1
    mem: 4G
```

```bash
$ cortex deploy

creating sentiment-classifier
```
