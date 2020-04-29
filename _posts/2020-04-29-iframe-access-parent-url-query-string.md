---
layout: post
title: "[3] ARTS Tip - iframe access parent URL query string"
subtitle: ""
author: "Blueswen"
header-style: text
tags:
    - ARTS
    - Tip
    - JavaScript
---

需求：主頁面以 iframe 包裝功能，主畫面不可更動，iframe 要可以根據指定參數動作

解法：以帶 query string 的 URL 開啟主頁面，iframe 取得主頁面 (parent) 的 query string 執行動作

1. iframe 取得 parent URL

    [Access parent URL from iframe](https://stackoverflow.com/a/7739035)

    ```js
    var url = (window.location != window.parent.location)
                ? document.referrer
                : document.location.href;
    ```

    ***此解法主要是避同源政策無法取 ```window.parent.location.href```，但如果 iframe 被轉址過 document.referrer 無法取到實際 parent 的 URL。***

    當 iframe 與 parent 都是同源的話可以直接用 ```window.parent.location.href```，多層的 iframe 時多取幾次 parent ```window.parent.parent.location.href```。

2. 解析 URL 中的 query string

    [How can I get query string values in JavaScript?](https://stackoverflow.com/a/901144)

    使用 [URLSearchParams](https://developer.mozilla.org/en-US/docs/Web/API/URLSearchParams)，但 IE 與較舊版本的瀏覽器不支援（[Ref](https://caniuse.com/#feat=urlsearchparams)）

    ```js
    const urlParams = new URLSearchParams(window.location.search);
    const myParam = urlParams.get('myParam');
    ```

    Vanilla JS 解法，使用正則把 query string 取出

    ```js
    function getParameterByName(name, url) {
        if (!url) url = window.location.href;
        name = name.replace(/[\[\]]/g, '\\$&');
        var regex = new RegExp('[?&]' + name + '(=([^&#]*)|&|#|$)'),
            results = regex.exec(url);
        if (!results) return null;
        if (!results[2]) return '';
        return decodeURIComponent(results[2].replace(/\+/g, ' '));
    }

    // query string: ?foo=lorem&bar=&baz
    var foo = getParameterByName('foo'); // "lorem"
    var bar = getParameterByName('bar'); // "" (present with empty value)
    var baz = getParameterByName('baz'); // "" (present with no value)
    var qux = getParameterByName('qux'); // null (absent)
    ```

Reference:

1. [SecurityError: Blocked a frame with origin from accessing a cross-origin frame](https://stackoverflow.com/a/25098153)
