---
categories:
- Review
date: '2020-09-18'
tags:
- DevOps
---

# The Future of Ops Jobs

[The Future of Ops Jobs](https://acloudguru.com/blog/engineering/the-future-of-ops-jobs)

本篇介紹了維運的改變以及維運工程師的未來職涯走向

### 維運的改變

1. From monolith to microservices  
   從 monolith 到 microservices，數量的增加讓維運的難度大幅提升
2. From monitoring to observability  
   從基礎的監控（如 Prometheus）到進階的觀測（如 zipkin、jaeger）
3. From magic autoinstrumentation to instrumenting with intent  
   Autoinstrumentation 雖然能夠快速分析或監控程式，但卻無法針對特定的需求調整，所以仍有必要撰寫自己的 instrumentation 程式

### 維運工程師的未來職涯方向

與過去相比現在的維運工程師可以不止依附在各公司底下，infrastructure software as a service 的形式讓維運工程師也能有很好的發展，像是 AWS 或 Azure。

若是選擇在各公司底下擔任維運工程師，專注在讓工程團隊順暢地發布產品，盡可能減少自己打造 infrastructure。另外作者也提供了幾個職涯方向：

1. Vendor engineering
   1. 透過詢價與試探性的問題評估廠商和他們的產品
   2. 評估團隊可以付出的人力與時間，盡可能削減人力的投入，專注在本業上
   3. 衡量產品的實際，教育與推廣合適的解決方案給內部人員，特別是主管與財務人員
2. Product engineering
   1. 加入開發團隊一段時間，了解他們怎麼思考與開發
   2. 跟開發團隊建立良好的關係
3. Sociotechnical systems engineering
   1. 精簡 deploy pipeline，優化測試、CI/CD 等等讓部署更加自動化
   2. 設計與優化開發新功能與修復 Bug 的循環
   3. 建立當責的文化
4. Managing the portfolio of technical investments
   1. 學會優雅地遷移，不要殘留舊產品或架構的產出物
   2. 加入各種工具時要先問自己『要這個工具的維護計畫是什麼？』
   3. 多學習、多增加影響力