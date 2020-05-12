---
layout: post
title: "[5] ARTS Review - GitOps for Kubernetes with Jenkins"
subtitle: ""
author: "Blueswen"
header-style: text
tags:
    - ARTS
    - Review
    - K8s
---

[GitOps for Kubernetes with Jenkins](https://medium.com/stakater/gitops-for-kubernetes-with-jenkins-7db6304216e0)

本文介紹了以 GitOps 的方式來部署與管理 K8s，GitOps 的核心概念為使用 Git 作為 infrastructure 與 application 的 source of truth。在 K8s 中所有的設定都是透過各式 yaml 檔進行管理，這些檔案能夠被完美地被 Git 所管理，在 Repo 中可以清楚地看到服務所使用的設定。

作者所提出的 Pipeline 如下圖，將 Code 與 K8s Config 拆開成兩個 Repo。Code Repo 僅負責 Image 的建置，實際部署則由 Config Repo 所負責。

![GitOps with Jenkins](/img/in-post/2020-05-12-gitops-for-k8s-with-jenkins/gitops_with_jenkins.png)  
Source: [GitOps for Kubernetes with Jenkins](https://medium.com/stakater/gitops-for-kubernetes-with-jenkins-7db6304216e0)

在 K8s 的架構下所謂的部署是部署**「服務組態」**，而程式碼只是 Image 的來源。若依然從單體式應用的角度去規劃部署，當一個 Pod 使用兩個以上的 Image 時就會馬上遇到問題。
