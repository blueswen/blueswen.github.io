---
layout: post
title: "[2] ARTS Share - JSON end with newline"
subtitle: ""
author: "Blueswen"
header-style: text
tags:
    - ARTS
    - Share
    - Python
    - API
---

解析 JSON 前可以預先透過簡單的文字判斷是否是合法的 JSON 來節省資源開銷，如 [mayBeJSON](http://json-lib.sourceforge.net/apidocs/jdk15/net/sf/json/util/JSONUtils.html#mayBeJSON(java.lang.String)) 會以結尾是否為 ```]``` 或 ```}``` 判斷是否為 JSON，因此有換行符號的 JSON 字串會被當作非法的字串，導致解析失敗。但 Python 的 Flask Framework 回傳 JSON 時候會額外回傳換行符號，本篇針對為何要增加換行進行簡單介紹，以及提供針對這種特定判斷的解法。

## JSON 最後為何要加入 newline

一般常用的 ```json.dumps``` 是不會有換行符號的，畢竟只是一個普通字串。所以先來看看是在什麼時候 response 的 JSON 被加上了換行符號。[Flask](https://github.com/pallets/flask) 的 [flask.json.jsonify](https://github.com/pallets/flask/blob/master/src/flask/json/__init__.py#L306) 是在 response 最後加入換行

```python
...
return current_app.response_class(
    dumps(data, indent=indent, separators=separators) + "\n",
    mimetype=current_app.config["JSONIFY_MIMETYPE"],
)
...
```

而 [Flask RestPlus](https://github.com/noirbizarre/flask-restplus) 也同樣是在包裝 response 的時候加入換行，[flask_restplus.representations.output.json](https://github.com/noirbizarre/flask-restplus/blob/master/flask_restplus/representations.py#L25)

```python
...
# always end the json dumps with a new line
# see https://github.com/mitsuhiko/flask/pull/1262
dumped = dumps(data, **settings) + "\n"
...
```

根據 source code 中提到的註解，我們可以按址索驥發現加入的緣由

```python
# always end the json dumps with a new line
# see https://github.com/mitsuhiko/flask/pull/1262
```

在 Flask 1.0 前 jsonify 最後是不會加上換行符號的，經過了 [Add JSONIFY_END_WITH_NEWLINE config variable #1262](https://github.com/pallets/flask/pull/1262) 這次 PR 後才加上了換行符號，增加換行符號的原因是參考 [postmanlabs/httpbin#168](https://github.com/postmanlabs/httpbin/issues/168) 以及 [Why should text files end with a newline?](https://stackoverflow.com/questions/729692/why-should-text-files-end-with-a-newline)。主要的論點為 [POSIX](https://zh.wikipedia.org/wiki/%E5%8F%AF%E7%A7%BB%E6%A4%8D%E6%93%8D%E4%BD%9C%E7%B3%BB%E7%BB%9F%E6%8E%A5%E5%8F%A3) 規範了在文件中當一行文字不是以 newline character 結尾時不會被當作一行文字，而所有 UNIX tools 都會預期文件有遵循這個規範。如果文件沒有遵循可能會導致非預期的問題或錯誤，如 stackoverflow 中回答的範例。

雖然 JSON 字串並不是文件，POSIX 也沒針對 JSON 進行規範，但在一些操作中可能會透過 UNIX tools 處理回傳的 response，若是沒有加上換行符號就會導致其他問題。而在最後加上換行符號也並不違反 JSON 本身的規範，因此若能加上換行符號對於使用 UNIX Tools 操作 response 的使用者會比較友善。

## 解決方案

大多數的情況下我們可能無法要求 API 使用者更換他們原本的 JSON 解析方式，所以我們只能試著從 Python 端解決，以下提供 Flask 與 Flask-restplus 的解法。

### Flask 解決方案

客製一個沒有加上換行符號的 jsonify，之所以不直接使用 json.dumps 是因為 response header 的 Content-Type 就只會是 text/html 而不是 application/json，在回傳時應該要利用 header 清楚表達回傳的內容。

### Flask restplus 解決方案

Flask-restplus 是透過 [api.make_response](https://github.com/noirbizarre/flask-restplus/blob/master/flask_restplus/api.py#L346) 包裝 response， flask_restplus.Api 在建立時會預設一組 JSON 的 representations：

```python
# flask_restplus/api.py
...
DEFAULT_REPRESENTATIONS = [('application/json', output_json)]
...
class Api(object):
    def __init__(self):
        ...
        self.representations = OrderedDict(DEFAULT_REPRESENTATIONS)
        ...
```

因此解法就是把 DEFAULT_REPRESENTATIONS 中的 output_json 換成沒有換行符號的版本即可， 但 self.representations 沒有辦法在建立 Api 時直接取代掉，不過 Flask-restplus 提供了 [representation](https://flask-restplus.readthedocs.io/en/latest/api.html#flask_restplus.Api.representation) 這個 decorator，原意是讓 response 能夠依據 request 回傳不同格式，如 xml 或 csv 等，但其實也可以透過這個方式直接覆寫 application/json 這組 mediatype，達到更改輸出格式的目的。

```python
@api.representation("application/json")
def output_json(data, code, headers=None):
    """Makes a Flask response with a JSON encoded body"""

    settings = app.config.get("RESTPLUS_JSON", {})
    if app.debug:
        settings.setdefault("indent", 4)
    # dumps without newline
    dumped = dumps(data, **settings)

    resp = make_response(dumped, code)
    resp.headers.extend(headers or {})
    return resp
```
