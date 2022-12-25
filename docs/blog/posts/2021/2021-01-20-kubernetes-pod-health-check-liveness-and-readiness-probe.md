---
categories:
- Review
date: '2021-01-20'
tags:
- K8s
---

# Kubernetes Operator for Beginners — What, Why, How

[Kubernetes Operator for Beginners — What, Why, How](https://medium.com/swlh/kubernetes-operator-for-beginners-what-why-how-21b23f0cb9b1)

本文介紹了 Operator 的功能以及如何建立 Operator

#### What is an operator

利用 Custom Resource (CRD) 操作 K8s 上的其他資源，並且符合 K8s 的 Control loop 機制，可以用 K8s native api 管理

#### Why you need an operator

以 Code 的方式自動化對 K8s 的操作，提高維運的可靠性

#### How to write an Operator

1. Kudo
2. Helm
3. Dynamic Operator: 彈性高，需要手動撰寫許多程式碼
   1. Operator SDK
   2. Kubebuilder

#### Is Operator Necessary

1. 不要沈溺於自動化。如果這個工作一個月只需要花十分鐘處理，那完全不值得花一週或甚至更多的時間來特地寫一個 Operator
2. 如果已經有 Helm Chart 或 Kudo template 可以使用的話，不要硬用 Operator SDK 或 Kubebuilder 重新實作，YAML 永遠比 Go Code 簡單更多
3. 如果可以的話，比起客制 Operator，選擇醜陋但簡單的 bash script 有時候會更輕鬆一點