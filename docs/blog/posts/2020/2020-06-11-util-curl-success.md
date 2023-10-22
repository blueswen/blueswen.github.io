---
categories:
- Tip
date: 2020-06-11
tags:
- Unix
---

# Until curl success

需求：模擬 K8s 的 [probe](https://www.innoq.com/en/blog/kubernetes-probes/)，持續探測指定的 endpoint 是否有回應

解法：重複執行 curl 直到取得正常回應

```bash
until $(curl --output /dev/null --silent --head --fail http://myhost:myport); do
    printf '.'
    sleep 5
done
```

當條件成立時 until 的迴圈就會終止，在 shell 中 0 為 true，其他則為 false

curl options:

* --output /dev/null：將 output 輸出到指定檔案，在 linux 中 ```/dev/null``` 指向一個空的設備，可以作為垃圾桶用，導向這個設備的資料都會被拋棄
* --silent：不會顯示進度或是錯誤訊息
* --head：只取 header，因為只需探測是否有回應
* --fail：一般 request 失敗時 server 會回覆一份 HTML 檔案，此設定可以略過 server 回覆的內容

Reference:

1. [How to create a loop in bash that is waiting for a webserver to respond?](https://stackoverflow.com/a/21189440/13582118)
2. [Bash: Loop until command exit status equals 0](https://stackoverflow.com/questions/21982187/bash-loop-until-command-exit-status-equals-0)
3. [Why 0 is true but false is 1 in the shell?](https://stackoverflow.com/a/2933855/13582118)
4. [curl Doc](https://www.mit.edu/afs.new/sipb/user/ssen/src/curl-7.11.1/docs/curl.html)
