---
categories:
- Review
date: 2020-12-01
tags:
- DevOps
---

# Technologies & Tools to Watch in 2021

[Technologies & Tools to Watch in 2021](https://medium.com/dev-genius/technologies-tools-to-watch-in-2021-a216dfc30f25)

本文分享了幾個 2021 值得 DevOps Engineers 與 SREs 關注的工具

1. Managing Cloud Services via Kubernetes CRDs

    現在在 K8s 上都能使用 custom resource definitions (CRDs) 啟用與管理 AWS, Azure 與 GCP 上的服務。AWS 使用 [AWS Controllers for Kubernetes (ACK)](https://github.com/aws/aws-controllers-k8s)；Azure 使用 [Azure Service Operator (for Kubernetes)](https://github.com/Azure/azure-service-operator)；GCP 使用 [Config Connector](https://cloud.google.com/config-connector/docs/overview)。好處是無論是 K8s 或 cloud services 都能用 K8s 的 API 操作，但缺點就是跟 K8s 有太深的耦合。

2. Pulumi

   [Pulumi](https://www.pulumi.com/) 是一個 IaC 的工具，與一般常見用 JSON 或 YAML 為基礎的 IaC 不同，他能夠直接使用 Go, Python, Javascript 來做 IaC，能夠帶來更高的彈性，並可以使用原本語言就有的測試框架進行測試。

3. Terragrunt & TFSEC

   [Terragrunt](https://terragrunt.gruntwork.io/) 將 Terraform 包裝起來，提供更多功能便於管理大型的 Terraform 專案，並支援版本的管理方式。[TFSEC](https://github.com/tfsec/tfsec) 提供掃描 Terraform 專案中 IaC 可能的安全問題。

4. Tekton

   [Tekton](https://tekton.dev/) 是 Cloud Native 的 CI/CD 工具，專注在 K8s 的 workloads。Pipeline 都是透過 CRDs 定義，因此能繼承 K8s 一些良好的特性，如 rollbacks，也能跟 JenkinsX 或 ArgoCD 有良好的介接。

5. Trivy

   [Trivy](https://github.com/aquasecurity/trivy) 能夠掃描 Container 與 OS 安裝的 Package 是否有安全漏洞，可以很輕易地串接在 CI 流程中。

6. ShellCheck

   [shellcheck](https://github.com/koalaman/shellcheck) 可以檢查 Shell 中常見的錯誤，有提供 web 版、CLI，甚至還有各種編輯器的 plugin。

7. Pitest/Stryker

   [Pitest](http://pitest.org/) (Java) 與 [Stryker](https://stryker-mutator.io/) (Javascript, C#, Scala) 都是 Mutation Test 的工具。Mutation Test 的假設是如果程式碼有變動，一個好的單元測試應該要因為這個變動而失敗，因此這兩個工具都會自動加入變動到程式中，藉此驗證單元測試或測試案例是否是好的測試。

8. Litmus

   [Litmus](https://github.com/litmuschaos/litmus) 是一個 chaos engineering tool，輕量且易於使用，有良好的實驗設計功能而非單純的隨意刪除 Pod，另外也直接提供了 ChaosResult CRD 直接查看結果。

Reference:

1. [變異測試 (Mutation Test) — 一種提高測試和代碼質量的 ”新” 方法速記](https://medium.com/@loverjersey/%E8%AE%8A%E7%95%B0%E6%B8%AC%E8%A9%A6-mutation-test-%E4%B8%80%E7%A8%AE%E6%8F%90%E9%AB%98%E6%B8%AC%E8%A9%A6%E5%92%8C%E4%BB%A3%E7%A2%BC%E8%B3%AA%E9%87%8F%E7%9A%84-%E6%96%B0-%E6%96%B9%E6%B3%95%E9%80%9F%E8%A8%98-35bde79a5c7a)
