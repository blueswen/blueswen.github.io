---
categories:
- Review
date: 2020-11-03
tags:
- K8s
---

# 10 most common mistakes using kubernetes

[10 most common mistakes using kubernetes](https://blog.pipetail.io/posts/2020-05-04-most-common-mistakes-k8s/)

1. resources - requests and limits
   1. CPU request 不要不設定或設太低，當 node 資源太滿的時候，pod 仍會被運行，但會拿到非常少的 CPU，導致 app 延遲或 timeout
   2. Memory 應該使用 Guaranteed QoS setting，request == limit。CPU 取不到無法多取的時候頂多造成延遲，但 Memory 無法擴張會導致 OOM
2. liveness and readiness probes
   1. liveness probe 失敗時會重啟 pod
   2. readiness probe 失敗時不會有任何連線送至 pod 中
   3. 兩種 probe 在整個 Pod 的生命週期中都會不停探測
   4. 不要讓任何一種 probe 因為 dependencies 下線而失敗，會導致 Pod 連鎖失敗
3. LoadBalancer for every http service
   1. 不要為每一個 service 都開一個 LoadBalancer，可以用 nginx-ingres-controller 作為唯一的 NodePort endpoint
4. non-kubernetes-aware cluster autoscaling
5. Not using the power of IAM/RBAC
6. self anti-affinities for pods
   1. 善用 affinity 讓 pod 生成在不同 node 上，以達到 HA
7. no poddisruptionbudget
   1. 使用 PodDisruptionBudget 在 draining node 時確保 pod 數量
8. more tenants or envs in shared cluster
   1. namespace 並不會提完整的硬體隔離性
9. externalTrafficPolicy: Cluster
10. pet clusters + stressing the control plane too much
    1. 不要把 cluster 當寵物在養，要練習 Disaster Recovery，隨時有機會得重新建出一個完全一致的 cluster
    2. 不要過度依賴 control plane，隨著 cluster 成長，上面的各種服務會越來越多，control plane 會開始變得緩慢，操作性變差

- bonus: using latest tag
  - 不要使用 latest tag

本文最後附上了 [Kubernetes Failure Stories](https://k8s.af/)，收集了各種使用 Kubernetes 時發生的慘案，以供借鑒。
