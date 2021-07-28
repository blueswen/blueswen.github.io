---
layout: post
title: "[21] ARTS Tip - Maven block http repositories"
subtitle: ""
author: "Blueswen"
header-style: text
tags:
    - ARTS
    - Tip
    - Java
    - Maven
---

問題：maven build 時出現 ```Could not resolve dependencies for project ... Could not transfer artifact ... from/to maven-default-http-blocker (http://0.0.0.0/) ...``` 錯誤訊息，http repository 被 maven block 無法取得相依 jar，導致建置失敗

以相依 ```com.lowagie:itext:jar:2.1.7``` 為例，完整錯誤訊息如下：

```log
[ERROR] Failed to execute goal on project sample: Could not resolve dependencies for project 
com.sample:sample:jar:0.0.1-SNAPSHOT: Failed to collect dependencies at net.sf.jasperreports:
jasperreports:jar:6.16.0 -> com.lowagie:itext:jar:2.1.7.js8: Failed to read artifact descriptor 
for com.lowagie:itext:jar:2.1.7.js8: Could not transfer artifact com.lowagie:itext:pom:2.1.7.js8 
from/to maven-default-http-blocker (http://0.0.0.0/): Blocked mirror for repositories: 
[jaspersoft-third-party (http://jaspersoft.jfrog.io/jaspersoft/third-party-ce-artifacts/, 
default, releases+snapshots), jr-ce-releases (http://jaspersoft.jfrog.io/jaspersoft/jr-ce-releases, 
default, releases+snapshots)]
```

原因：Maven 在 3.8.1 之後為了避免被利用 http 執行中間人攻擊（[CVE-2021-26291](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-26291)），預設會 block 所有 http repositories

解法：在無法找到可使用的 https repository 時，可以在 maven 的 config 自訂 mirror 並將 blocked 設定關閉

以 ```http://jaspersoft.jfrog.io/``` 這個 http repository 為例：

```xml
<settings xmlns="http://maven.apache.org/SETTINGS/1.2.0"
          xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
          xsi:schemaLocation="http://maven.apache.org/SETTINGS/1.2.0 http://maven.apache.org/xsd/settings-1.2.0.xsd">
  <mirrors>
    <mirror>
      <id>jaspersoft-third-party-mirror</id>
      <mirrorOf>jaspersoft-third-party</mirrorOf>
      <url>http://jaspersoft.jfrog.io/jaspersoft/third-party-ce-artifacts/</url>
      <blocked>false</blocked>
    </mirror>
  </mirrors>
</settings>
```

如果是以 maven 的 Docker Image 建置專案可以參考以下的結構，在 ```.mvn``` 資料夾中寫入 ```maven.config``` 與 ```local-settings.xml``` 兩個檔案

```txt
├── Dockerfile
├── mvnw
├── pom.xml
├── src
└── .mvn
    ├── local-settings.xml
    ├── maven.config
    └── wrapper
```

### Dockerfile

```dockerfile
FROM maven:3.6.3-openjdk-8
WORKDIR /workspace
COPY . .
RUN unset MAVEN_CONFIG && ./mvnw package
```

### maven.config

```config
--settings ./.mvn/local-settings.xml
```

### local-settings.xml

```xml
<settings xmlns="http://maven.apache.org/SETTINGS/1.2.0"
          xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
          xsi:schemaLocation="http://maven.apache.org/SETTINGS/1.2.0 http://maven.apache.org/xsd/settings-1.2.0.xsd">
  <mirrors>
    <mirror>
      <id>jaspersoft-third-party-mirror</id>
      <mirrorOf>jaspersoft-third-party</mirrorOf>
      <url>http://jaspersoft.jfrog.io/jaspersoft/third-party-ce-artifacts/</url>
      <blocked>false</blocked>
    </mirror>
  </mirrors>
</settings>
```

Reference:

1. [Release Notes – Maven 3.8.1](https://maven.apache.org/docs/3.8.1/release-notes.html)
2. [How to disable maven blocking external HTTP repositores?](https://stackoverflow.com/a/67002852)
3. [Maven Build Failure — DependencyResolutionException](https://stackoverflow.com/a/67121849)
