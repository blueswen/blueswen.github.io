---
categories:
- Tip
date: 2024-01-02
tags:
- Harbor
- Container
---

# Harbor REST API

## REST API

Harbor 提供 [REST API](https://editor.swagger.io/?url=https://raw.githubusercontent.com/goharbor/harbor/main/api/v2.0/swagger.yaml) 供使用者進行管理，例如 GET `/projects/{project_name}/repositories/{repository_name}/artifacts/{reference}` 可以取得指定的 Artifact 資訊，包含像是 Image 的 Entry Point、Command、Env、Label 等等。

## Authentication

使用時透過 Basic Authentication 進行認證，如使用 `curl` 時可以透過 `-u` 參數指定帳號與密碼：

```bash
curl -u admin:Harbor12345 -X GET "https://harbor.example.com/api/v2.0/projects/test/repositories/test/artifacts/latest"
```

或是透過 `Authorization` Header 進行認證，Value 為 `Basic <base64 encoded username:password>`：

```bash
curl --header "Authorization: Basic YWRtaW46SGFyYm9yMTIzNDU= -X GET "https://harbor.example.com/api/v2.0/projects/test/repositories/test/artifacts/latest"
```

## Reference

1. [Harbor FAQs](https://github.com/goharbor/harbor/wiki/Harbor-FAQs#api)
