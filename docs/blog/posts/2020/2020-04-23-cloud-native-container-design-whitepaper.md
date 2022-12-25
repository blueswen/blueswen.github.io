---
categories:
- Review
date: '2020-04-23'
tags:
- K8s
- Cloud Native
---

# Principles of container-based application design

[Principles of container-based application design](https://www.redhat.com/en/resources/cloud-native-container-design-whitepaper)

這篇是由 Red Hat 針對 container-based application 提出的白皮書，簡述了幾個建議遵守的原則。從下載的檔案名稱可以發現應該是於 2017 年 10 月所發表的第三版，但因為都是很基礎的原則，到目前為止還沒有過時的問題。

PRINCIPLES OF SOFTWARE DESIGN

* KISS  —   Keep it simple, stupid.
* DRY — Don’t repeat yourself.
* YAGNI — You aren’t gonna need it.
* SoC — Separation of concerns.

Red Hat 在 cloud-native 的情境下提供了幾點原則：

* Single concern principle (SCP)：如同 SOLID 的 single responsibility principle (SRP)，container 應該只負責執行一個 process。
* High observability principle (HOP)：container 要可以很好地被觀測，如是否可以提供服務 (readiness)、是否運作正常 (liveness)，log 應該要以 standard error (STDERR) 及 standard output (STDOUT) 輸出。
* Life-cycle conformance principle (LCP)：針對 container 在生命週期中不同階段所接收到的 Signal，執行指定的操作。如 container 關閉前釋放資源或把當下未完成的任務完成等，藉此達到 graceful shutdown。
* Image immutability principle (IIP)：在不同環境下所使用的 Image 都為同一份，與環境相關的參數與設定檔都應該透過 Kubernetes ConfigMap 進行設定。
* Process disposability principle (PDP)：container 應該要為 stateless 或是將狀態保存於外部，這樣就可以隨時被銷毀或生成，藉此達到 auto-scaling 等需要自動增刪 container 的功能。
* Self-containment principle (S-CP)：container 只放置執行時所需要的東西，如 language runtime、dependencies 等，會隨部署環境變動的 config 透過 Kubernetes ConfigMap 在執行時載入。
* Runtime confinement principle (RCP)：container 所需使用的硬體資源應清楚說明，如 CPU、memory、網路、硬碟用量等，讓平台能有更好的調度。

文末也列出了幾個常見的 best practice，如盡可能縮小 Image、避免使用 sudo 或特定 userid 執行 container 等，都很值得參考實踐。

Reference:

1. [优雅地关闭kubernetes中的nginx](https://segmentfault.com/a/1190000008233992)