---
categories:
- Review
date: 2020-06-09
tags:
- Architecture
---

# Saving Files In A Database Or In A File System?

[Which Is Superior: Saving Files In A Database Or In A File System?](https://habiletechnologies.com/blog/better-saving-files-database-file-system/)

本文分析 Web Serer 管理上傳的檔案的兩種方式，使用 File System 與透過 DB 儲存。

### File System

#### Pros

1. 能夠有較好的效能，讀取檔案不用下查詢
2. 儲存與下載檔案比起用 DB 簡單很多
3. Scale 的時候 File System 比 DB 更便宜

#### Cons

1. 沒有 ACID，無法保證與 DB 間資料的關係
2. 安全性低，只要知道 File System 就可以取得檔案

#### 適用場景

1. 需要處理較大的檔案，如 5 MB 以上，並可能要儲存上千個檔案
2. 服務有大量的使用者時

### DB

#### Pros

1. ACID
2. 比 File System 安全

#### Cons

1. 檔案要轉換為 blob 才能存入 DB 中
2. DB 備份會變得很緩慢
3. 在讀寫時會耗費較多的記憶體資源，等同於降低服務效能

#### 適用場景

1. 檔案需要較高的安全性
2. 少量的檔案與少量的使用者

簡單總結選擇的策略，需要 ACID 的話選 DB，否則 File System 就好。
