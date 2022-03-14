---
layout: post
title: "npm ERR! code SELF_SIGNED_CERT_IN_CHAIN"
subtitle: ""
author: "Blueswen"
header-style: text
tags:
    - ARTS
    - Tip
    - Node.js
---

問題：```npm install``` 出現 npm ERR! code SELF_SIGNED_CERT_IN_CHAIN 錯誤訊息

原因：舊版的 npm 將自簽的 CA file 綁定在 client 中，因此當 npm registry 更新簽證時會發生簽證不吻合

有三種解法：

1. 更新 npm 版本

    ```bash
    npm install npm -g --ca=null
    ```

2. 不使用 npm 內建的 CA，改使用 node 的 CA

    ```bash
    npm config set ca=""
    ```

3. 停用 SSL 嚴格模式，忽略 SSL 的錯誤，但會有安全疑慮

    ```bash
    npm set strict-ssl false
    ```

Reference:

1. [nodejs “npm ERR! code SELF_SIGNED_CERT_IN_CHAIN”](https://stackoverflow.com/a/34945326/13582118)
2. [More help with SELF_SIGNED_CERT_IN_CHAIN and npm](https://blog.npmjs.org/post/78165272245/more-help-with-selfsignedcertinchain-and-npm)
