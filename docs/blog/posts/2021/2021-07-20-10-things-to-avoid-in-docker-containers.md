---
categories:
- Review
date: '2021-07-20'
tags:
- Docker
- Container
---

# 10 things to avoid in docker containers

[10 things to avoid in docker containers](https://developers.redhat.com/blog/2016/02/24/10-things-to-avoid-in-docker-containers)

原文寫於 2016 年，距今約 5 年前，提出了 10 個使用 Docker Container 時應該避免的行為

1. Don't store data in containers  
   不要在 Container 中儲存需要永久保留的資料，應使用 Volume。
2. Don't ship your application in two pieces  
   有些人會把 Container 完全視為 Virtual Machine，所以試圖把 application 部署至運行中的 Container。但正確的做法為把 application 與可運行環境的 base image 打包成一個新的 image。
3. Don't create large images  
   過肥的 image 會影響部署速度。
4. Don't use a single layer image  
   避免做出只有一層 layer 的 image，可以 OS 一層、User 設定一層、各種 package 安裝一層、config 一層，最後 application 自己一層。透過這樣的分層未更動的 layer 在建置的時候能夠使用 cache，可以加快建置的速度，因為在一般情況下都是 application 變動。
5. Don't create images from running containers  
   不要使用 Docker commit 的方式將運行中的 Container 匯出成 image，應使用 Dockerfile 建置。
6. Don't use only the "latest" tag  
   latest 不具有任何識別性，應加上其他 tag 供識別，如版本號、commit id、時間戳記等。
7. Don't run more than one process in a single container  
   Container 中只運行一個 process，同時運行多個 process 無法有效透過 Docker 管理 Container 中 process 的狀態。
8. Don't store credentials in the image. Use environment variables  
   不要把機敏資訊儲存於 Image 中，如 DB 帳密、各種 SaaS 的 api key，可以透過環境變數的方式放入。
9. Don't run processes as a root user  
   Process 不要使用 root user，如果執行的服務有安全漏洞可能會讓駭客更加容易取得 Container 的 root 權限。
10. Don't rely on IP addresses  
    不要依賴 Container 的 IP，Container 在重新啟動後會被重新分配 IP。

雖然已經是很舊的文章了，不過還是有其參考價值。有一些內容在現在已經可以算是基本常識了，如不要在 Container 中儲存資料，不要把服務部署到 Container 中。也有一些則繼續延伸，如不要只使用 latest tag，現在大多提倡直接棄用 latest tag，每個 image 都要賦予可辨識的 tag，避免在部署時意外將 latest 部署出去。

下面也有網友針對 credentials 提出不同的看法，隨著技術的推展社群也提出其他更好的方式設定 credentials，例如使用 Volume 的方式掛入寫有 credentials 的檔案，可以避免環境變數被意外寫出至 Log 或是被入侵時輕易地找出。而到了 K8s 風行的時代又更針對 credentials 提出更多處理方式，如使用 Secrets 或是使用 [Vault](https://www.vaultproject.io/) 這類工具進行管理等。