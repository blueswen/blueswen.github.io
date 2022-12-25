---
categories:
- Tip
date: '2020-04-22'
tags:
- Docker
---

# 防止 Container 啟動後退出

在建置完 Image 後時常會發現 Image 不如預期中運作，如預設的 CMD 莫名地 Crash 等，這時候就會需要進入 container 中，使用 ```tail -f /dev/null``` 作為 CMD 就可以讓 container 一直處於 running 的狀態，隨時可以進入檢測。另一個常用的情境是透過這個方式起一個永久 running 的 container，這樣就可以作為虛擬環境使用。

```bash
docker run -d python tail -f /dev/null
```

在 Docker 的機制中 container 的運作狀態是跟隨其 CMD 或 ENTRYPOINT 所執行的程序，當程序意外停止或執行完成時就會變為 Exited，因此要讓 container 處於永久 running 的狀態就需要執行一個會不停執行的程序。

```tail -f``` 會跟蹤並印出指定檔案的最末端，而 ```/dev/null```  為 Linux 中一個特殊的檔案，檔案內容永遠只有 EOF，因此合併後的效果就是跟蹤一個永遠為空的檔案，成為一個永久執行但消耗極少資源的程序。

Reference:

1. [利用 tail -f /dev/null 命令防止 container 启动后退出](https://blog.ponycool.com/archives/121.html)
2. [Linux 學習——/dev/null 的簡介及作用](https://kknews.cc/zh-tw/code/valkama.html)
3. [Linux tail command](https://www.computerhope.com/unix/utail.htm)