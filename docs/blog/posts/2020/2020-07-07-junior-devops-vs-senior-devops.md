---
categories:
- Review
date: '2020-07-07'
tags:
- DevOps
---

# Differences Between Junior DevOps and Senior DevOps Engineers

[Differences Between Junior DevOps and Senior DevOps Engineers](https://medium.com/devops-dudes/differences-between-junior-devops-and-senior-devops-engineers-8d0f28b8b30b)

本篇說明了作者他認為 junior 跟 senior DevOps Engineers 在配置管理上的差別，無論是在實體機、VM 或是 K8s 中，配置都是一項非常重要的工作，完善的配置管理讓軟體與硬體的狀態可以被追蹤與重現，使配置成為 single source of truth。

五個配置管理的面向：

1. 管理 OS 與 Middleware Software 的安裝與設定
2. configuration-as-code
3. 無論環境如何變更的結果都會是相同的
4. 了解變更對系統可能帶來的副作用
5. networks-as-code

作者提倡善用 [Ansible](https://www.ansible.com/)、[Chef](https://www.chef.io/configuration-management/) 等配置設定工具，當面對問題時應思考 enterprise-scale 的層級，而不是單純只是解決當下的問題而已。

回覆中有人提到比起新技術，DevOps 的核心應該去關注 flow of work，如果新技術沒有考量或瞭解真正需要解決的商業問題，那這個新技術的導入就不會帶來任何益處。