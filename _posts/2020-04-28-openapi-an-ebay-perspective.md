---
layout: post
title: "[3] ARTS Review - OpenAPI – An eBay Perspective"
subtitle: ""
author: "Blueswen"
header-style: text
tags:
    - ARTS
    - Review
    - API
    - OpenAPI
---

[OpenAPI – An eBay Perspective](https://tech.ebayinc.com/engineering/openapi-an-ebay-perspective/)

在本文中 eBay 說明了為何選用 OpenAPI 作為他們的 API contract，以及如何將從舊的 API contract 遷移至 OpenAPI。

以下為選用的原因與帶來的影響：

選擇 OpenAPI 的原因：

1. Structural integrity and richness：具有完善的結構規範以及強大的可擴充性；共用的資料結構能以參照外部檔案的方式引用，提高跨 API 共用資料的可管理性
2. Futuristic and evolving：OpenAPI 仍不斷地在發展與增加功能
3. Tooling Support：大量的 open source project 讓 OpenAPI 的易用性大增，如 Swagger UI 提供可互動操作的網頁，Swagger Codegen 能夠生成 40 種語言的 servers side、client side 程式碼
4. 透過 OpenAPI 的工具，無論是 code first 或是 contract first，都能夠得到良好的 API 設計與開發體驗
5. Open Source，完全可控，能針對特殊需求客制

OpenAPI 對系統與組織帶來的影響：

1. Standards and Compliance：成為共同的資料標準，因此能夠導入自動化的檢核
2. Bootstrapping development across technology stacks：與語言無關的 API Spec 可以馬上融入在不同的技術棧中，有效提高了開發品質與速度
3. Downstream Service Integration：透過 Swagger UI、Swagger Codegen 使用者可以快速測試 API
4. Continuous Delivery：因為 API Contract 與語言無關，所以 API 都可以使用同樣的 Pipeline 進行測試
5. Application Security：輸入與輸出都會明確列出，可以加上掃瞄或過濾的機制避免不明的參數進到 server 端

在微服務中，提供機器可讀的 API Spec 能提高整體的可維護性，而與語言無關能讓群集可容納不同技術生成的服務，兩者都大幅提升了微服務的可管理性。
