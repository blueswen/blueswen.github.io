---
layout: post
title: "OpenVPN for Docker"
subtitle: ""
author: "Blueswen"
header-style: text
tags:
    - ARTS
    - Share
    - Toolbox
---

[OpenVPN for Docker](https://github.com/kylemanna/docker-openvpn) 把 OpenVPN 打包成 Docker Image，透過 Docker 可以快速建立一個 OpenVPN Server。

建立 OpenVPN Server 步驟：

透過 Docker Volume 相關檔案都會產生於當前目錄下的 opnevpn 資料夾中(\`pwd\`/openvpn)

1. 建立相關設定與憑證，會要求設定 passphrase

    ```bash
    # VPN.SERVERNAME.COM 需改為實際的 domain 或 ip
    docker run -v `pwd`/openvpn:/etc/openvpn --log-driver=none --rm kylemanna/openvpn ovpn_genconfig -u udp://VPN.SERVERNAME.COM
    docker run -v `pwd`/openvpn:/etc/openvpn --log-driver=none --rm -it kylemanna/openvpn ovpn_initpki
    ```

2. 啟動 OpenVPN Server

    ```bash
    docker run -v `pwd`/openvpn:/etc/openvpn -d -p 1194:1194/udp --cap-add=NET_ADMIN kylemanna/openvpn
    ```

3. 生成沒有 passphrase 的 client certificate

    ```bash
    docker run -v $OVPN_DATA:/etc/openvpn --log-driver=none --rm -it kylemanna/openvpn easyrsa build-client-full CLIENTNAME nopass
    ```

4. 生成帶有認證的 OpenVPN Client 設定檔

    ```bash
    docker run -v $OVPN_DATA:/etc/openvpn --log-driver=none --rm kylemanna/openvpn ovpn_getclient CLIENTNAME > CLIENTNAME.ovpn
    ```

OpenVPN Client：

1. Mac 推薦使用 [Tunnelblick](https://tunnelblick.net/)，設定檔匯入的方式是將 .ovpn 檔拖曳到 Menubar 的 Tunnelblick icon 上
2. windows 可以使用 OpenVPN 提供的 [Client](https://openvpn.net/community-downloads/)，設定檔匯入的方式是將 .ovpn 檔複製至 OpenVPN 的 config 資料夾中，大多為 ```C:\Program Files\OpenVPN\config```

Reference:

1. [OpenVPN for Docker](https://github.com/kylemanna/docker-openvpn)
