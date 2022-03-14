---
layout: post
title: "K8s 節點資源耗盡"
subtitle: ""
author: "Blueswen"
header-style: text
tags:
    - ARTS
    - Tip
    - K8s
---

問題：K8s 的 node 出現 EvictionThresholdMet NodeHasDiskPressure 狀況，導致 Pod 無法建立，但實際上空間還很充足

解法：調高 Threshold

1. 確認 kubelet 的狀態

    ```txt
    $ sudo systemctl status kubelet
    ● kubelet.service - kubelet: The Kubernetes Node Agent
    Loaded: loaded (/lib/systemd/system/kubelet.service; enabled; vendor preset: enabled)
    Drop-In: /etc/systemd/system/kubelet.service.d
            └─10-kubeadm.conf
    Active: active (running) since 一 2017-10-16 10:25:09 CST; 6h ago
        Docs: http://kubernetes.io/docs/
    Main PID: 13640 (kubelet)
        Tasks: 18
    Memory: 62.0M
        CPU: 18min 15.235s
    CGroup: /system.slice/kubelet.service
            ├─13640 /usr/bin/kubelet --kubeconfig=/etc/kubernetes/kubelet.conf --require-kubeconfig=true --pod-manifest-path=/etc/kubernetes/manifests --allow-privileged=true --
            └─13705 journalctl -k -f
    ...
    ```

2. 與 kubelet 有關的設定有兩個

    ```txt
    - /lib/systemd/system/kubelet.service
    Drop-In: /etc/systemd/system/kubelet.service.d
            └─10-kubeadm.conf
    ```

3. /etc/systemd/system/kubelet.service.d/10-kubeadm.conf 是用來覆寫 /lib/systemd/system/kubelet.service 中的配置，內容如下

    ```txt
    [Service]
    Environment="KUBELET_KUBECONFIG_ARGS=--kubeconfig=/etc/kubernetes/kubelet.conf --require-kubeconfig=true"
    Environment="KUBELET_SYSTEM_PODS_ARGS=--pod-manifest-path=/etc/kubernetes/manifests --allow-privileged=true"
    Environment="KUBELET_NETWORK_ARGS=--network-plugin=cni --cni-conf-dir=/etc/cni/net.d --cni-bin-dir=/opt/cni/bin"
    Environment="KUBELET_DNS_ARGS=--cluster-dns=10.96.0.10 --cluster-domain=cluster.local"
    Environment="KUBELET_AUTHZ_ARGS=--authorization-mode=Webhook --client-ca-file=/etc/kubernetes/pki/ca.crt"
    Environment="KUBELET_CADVISOR_ARGS=--cadvisor-port=0"
    ExecStart=
    ExecStart=/usr/bin/kubelet $KUBELET_KUBECONFIG_ARGS $KUBELET_SYSTEM_PODS_ARGS $KUBELET_NETWORK_ARGS $KUBELET_DNS_ARGS $KUBELET_AUTHZ_ARGS $KUBELET_CADVISOR_ARGS $KUBELET_EXTRA_ARGS
    ```

4. 修改 10-kubeadm.conf 的內容調高上限，增加一個 Environment 並加入在 ExecStart 的最後

    ```txt
    Environment="KUBELET_EVICTION_POLICY_ARGS=--eviction-hard=nodefs.available<5%"
    ExecStart=
    ExecStart=/usr/bin/kubelet $KUBELET_KUBECONFIG_ARGS $KUBELET_SYSTEM_PODS_ARGS $KUBELET_NETWORK_ARGS $KUBELET_DNS_ARGS $KUBELET_AUTHZ_ARGS $KUBELET_CADVISOR_ARGS $KUBELET_EXTRA_ARGS $KUBELET_EVICTION_POLICY_ARGS
    ```

5. reaload 並重啟 kubelet 就可以重新載入設定

    ```txt
    $ sudo systemctl daemon-reload
    $ sudo systemctl restart kubelet
    ```

Reference:

1. [Kubernetes节点资源耗尽状态的处理](https://tonybai.com/2017/10/16/out-of-node-resource-handling-in-kubernetes-cluster/)
2. [排查 kubelet、kubeadm init 問題](https://ithelp.ithome.com.tw/articles/10209357)
