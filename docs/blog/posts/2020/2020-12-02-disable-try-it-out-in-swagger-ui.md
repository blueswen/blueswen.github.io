---
categories:
- Tip
date: '2020-12-02'
tags:
- OpenAPI
---

# Disable 'Try it out' in Swagger UI

[Swagger UI](https://github.com/swagger-api/swagger-ui) 能生成一個完整的網頁呈現 OpenAPI 文件，且同時可以在頁面上直接發送 Request 進行測試。但在一些情況下會不希望使用者直接發送，例如文件只是供瀏覽，或後台尚未完成等等，這時候就會希望可以停用 Try it out 的功能。

在比較舊的版本可以透過 plugin 的方式停用 Try it out

```js
var SwaggerUIBundle = require('swagger-ui-dist').SwaggerUIBundle

const DisableTryItOutPlugin = function() {
  return {
    statePlugins: {
      spec: {
        wrapSelectors: {
          allowTryItOutFor: () => () => false
        }
      }
    }
  }
}

const ui = SwaggerUIBundle({
    url: "https://petstore.swagger.io/v2/swagger.json",
    dom_id: '#swagger-ui',
    presets: [
        SwaggerUIBundle.presets.apis,
        SwaggerUIBundle.SwaggerUIStandalonePreset
    ],
    plugins: [
        DisableTryItOutPlugin // <== 停用的 plugin
    ],
    layout: "StandaloneLayout"
})
```

比較新的版本則有 [supportedSubmitMethods](https://github.com/swagger-api/swagger-ui/blob/master/docs/usage/configuration.md#user-content-supportedsubmitmethods) 這個參數可以使用，參數值為正向表列可以要啟用 Try it out 的 HTTP method，為空時表示全部停用。

使用 Docker 的環境變數設定，以 docker-compose 為範例

```yaml
version: "3.8"
services:
  swagger-ui:
    image: swaggerapi/swagger-ui
    ports:
      - 80:8080
    environment:
      - SUPPORTED_SUBMIT_METHODS=[]
```

Javascript 的話則是

```js
var SwaggerUIBundle = require('swagger-ui-dist').SwaggerUIBundle

const ui = SwaggerUIBundle({
    url: "https://petstore.swagger.io/v2/swagger.json",
    dom_id: '#swagger-ui',
    presets: [
        SwaggerUIBundle.presets.apis,
        SwaggerUIBundle.SwaggerUIStandalonePreset
    ],
    supportedSubmitMethods: [], // <== 停用所有 HTTP method 的 Try it out
    layout: "StandaloneLayout"
})
```

Reference:

1. [How to disable 'Try it out' in Swagger UI 3.x](https://github.com/swagger-api/swagger-ui/issues/3725)
2. [Swagger UI Usage](https://swagger.io/docs/open-source-tools/swagger-ui/usage/installation/)