---
categories:
- Tip
date: 2022-03-02
tags:
- Docker
---

# Connect docker host from inside a docker container

需求：在 Container 內直接使用 Hostname 與 Host 溝通

1. Container 中的 Application 與在 Host 上執行的 Application 溝通
2. 使用 Container 作為 Proxy（如 Traefik），需要 Proxy 的服務開在 Host 上

解法：

最暴力解的解法為直接將在 Container 內的目標指向 Host 的 IP，但這種當環境變動時就會需要手動調整，例如 DHCP、浮動 IP 或是切換到不同主機執行時。

[How to connect to the Docker host from inside a Docker container?](https://medium.com/@TimvanBaarsen/how-to-connect-to-the-docker-host-from-inside-a-docker-container-112b4c71bc66) 這篇文章介紹了在 Docker Desktop 與 Linux 上的 Docker Engine 的兩種解法

1. Docker Desktop

    在 Windows 或 Mac 要使用通常都會安裝 Docker Desktop，在官方的說明文件中（[Mac](https://docs.docker.com/desktop/mac/networking/#i-want-to-connect-from-a-container-to-a-service-on-the-host)、[Windows](https://docs.docker.com/desktop/windows/networking/#i-want-to-connect-from-a-container-to-a-service-on-the-host)），說明可以直接使用 ```host.docker.internal``` 這個 Hostname 從 Container 連接 Host。

2. Linux Docker Engine

    在 20.10 版後，Docker Engine 也支援了 ```host.docker.internal``` 這個 Hostname，但是無法開箱即用，在啟動 Container 時需要額外使用 ```--add-host``` 參數設定 Host，設定如下

    ```bash
    --add-host=host.docker.internal:host-gateway
    ```

    在 Docker Compose 中可以透過 ```extra_hosts``` 增加 Host，Compose 範例如下：

    ```yaml
    version: "3.8"
    services:

    ubuntu:
        image: ubuntu
        container_name: ubuntu
        extra_hosts:
        - "host.docker.internal:host-gateway"
        command: tail -f /dev/null
    ```

Reference:

1. [How to connect to the Docker host from inside a Docker container?](https://medium.com/@TimvanBaarsen/how-to-connect-to-the-docker-host-from-inside-a-docker-container-112b4c71bc66)
