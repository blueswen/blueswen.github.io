---
layout: post
title: "[18] ARTS Tip - Install node-sass without download the binding.node file from GitHub"
subtitle: ""
author: "Blueswen"
header-style: text
tags:
    - ARTS
    - Tip
    - Node.js
---

問題：安裝 [node-sass](https://www.npmjs.com/package/node-sass) 時，因為網路問題無法正常下載 GitHub 上的 binary，導致專案建置失敗

解法：參考 [https://github.com/sass/node-sass/issues/2133#issuecomment-477924161](https://github.com/sass/node-sass/issues/2133#issuecomment-477924161) 這則回覆中的方法，以自訂 Binary 網路位置的方式讓下載能正常執行

1. 手動下載要使用的 Binary 版本
2. 上傳至內部的 Nexus 的 Raw Repositories，URL 格式為 ```https://nexus.intra/repository/nodejs/vx.x.x/```
3. 在 npm 中設定 node-sass 抓取 Binary 指向網站

    ```bash
    npm config set sass-binary-site=https://nexus.intra/repository/nodejs/ --global
    ```

在這個 issue 中有人對安裝 npm package 預設居然是下載 Binary 檔提出質疑，這在資安上其實有很大的漏洞，而且大多數公司在建置環境下都是無法連外，只從 private repository 上下載檢核過的 package。

未來在安裝 package 也要多注意是否有這種下載 Binary 的情況，避免引入不必要的風險。

Reference:

1. [Is there a way to install node-sass without download the binding.node file from GitHub?](https://github.com/sass/node-sass/issues/2133)
