---
layout: post
title: "[19] ARTS Tip - GitBook Base Path"
subtitle: ""
author: "Blueswen"
header-style: text
tags:
    - ARTS
    - Tip
    - GitBook
---

需求：有多份 [GitBook](https://github.com/GitbookIO/gitbook-cli) 需要掛載在同一個 web server 下，必須針對不同 GitBook 設定 base path

解法：使用 [GitBook Plugin Base](https://github.com/noamyoungerm/gitbook-plugin-base) 在 GitBook 的 ```book.json``` 設定 base 參數

```json
{
    "pluginsConfig": {
        "base":{
            "base": "/book-name/content"
        }
    }
}
```

這樣建構出來的 GitBook URL 都會以 ```/book-name/conten/``` 作為開頭
