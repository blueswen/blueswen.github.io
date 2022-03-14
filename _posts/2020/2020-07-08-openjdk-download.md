---
layout: post
title: "Open JDK Download"
subtitle: ""
author: "Blueswen"
header-style: text
tags:
    - ARTS
    - Tip
    - Unix
---

問題：在沒有辦法連網的狀況下載與安裝 OpenJDK

解法：下載 binary 檔

- Oracle 的 OpenJDK 頁面下載 [https://jdk.java.net/archive/](https://jdk.java.net/archive/)，可以下載各種版本的 OpenJDK Binary，有 Windows、Mac、Linux 版
- [ojdkbuild](https://github.com/ojdkbuild/ojdkbuild) 提供了各種版本的 Binary，有 Windows、Linux x86_64、Linux ARM32

### windows 設定

1. 解壓下載的 Binary
2. 開啟環境變數，電腦 => 右鍵內容 => 進階系統設定 => 環境變數 => 新增或編輯系統變數
3. 新增環境變數 ```JAVA_HOME``` 指向 Binary 資料夾
4. 編輯環境變數 ```PATH```，最前面加入 ```%JAVA_HOME%\bin;```

### Linux 設定

解壓下載的 Binary，編輯 ```~/.bash_profile```，增加 JAVA_HOME

```txt
export JAVA_HOME=[Binary 路徑]
export PATH=$JAVA_HOME/bin:$PATH
```

Reference:

1. [Windows Open JDK 替代方案研究](https://blog.darkthread.net/blog/openjdk-in-windows/)
2. [Java 要收費 ?! 是時候使用 OpenJDK 了](http://blog.tonycube.com/2018/11/java-openjdk.html)
