---
categories:
- Tip
date: 2020-05-20
tags:
- Jenkins
- git
---

# Jenkins with Git Operation

需求：在 Jenkins pipeline 中操作 repo 做 commit 並 push 回 remote，但遇到需要登入的問題

解法：透過 ```git config --global credential.helper cache``` 暫存登入資訊

Jenkins pipeline：

```groovy
script{
    sh 'git config --global credential.helper cache'
}
checkout([$class: 'GitSCM', userRemoteConfigs: [[credentialsId: 'git_credential', url: "${git_url}"]]])
sh """
    git config --local user.email "test@mail.test"
    git config --local user.name "test"
    git add -A
    git commit -m "commit by jenkins"
    git push
    git config --global --unset credential.helper
    rm -r ~/.git-credential-cache/
"""
}
```

當使用 HTTP(S) 存取遠端 Repo 時可以使用 ```credential.helper``` 避免每次都要重新輸入密碼。在 Linux 環境下 ```credential.helper``` 有 ```cache``` 與 ```store``` 兩種模式，```cache``` 會暫存登入資訊，預設時間為 15 分鐘，並將資訊存放於 ```~/.git-credential-cache/socket``` 中；```store``` 則是會以明碼方式將帳號密碼儲存在 ```~/.git-credentials``` 下。

```checkout``` 前先設定將 global 的 ```credential.helper``` 設為 ```cache```，這樣即可以將 ```checkout``` 的登入資訊暫存起來，之後就可以利用暫存的登入資訊進行 push 等跟遠端 Repo 互動的操作。雖然 cache 預設 15 分鐘就會過期，但考量到帳號管控問題，在工作完成後主動清除會是一個比較好的做法。

在搜尋解法時我先以 [withCredentials](https://www.jenkins.io/doc/pipeline/steps/credentials-binding/) 做為可行的解決方案，但沒有搞清楚其實 ```withCredentials``` 其實就只是幫你把設定的資訊取出，還一直以為包在 ```withCredentials``` 中就可以自動登入遠端 Repo。雖然也可以直接取出 credential 中的帳號密碼在 push 時設定，如：```git push origin https://name:password@github.com/repo.git```，但這樣看起來就不是一個很漂亮的方式，因此還是選擇使用設定 ```credential.helper``` 達成目的。

Reference:

1. [如何透過 Git Credential 管理透過 HTTP 通訊協定存取儲存庫的帳號密碼](https://blog.miniasp.com/post/2018/05/28/Git-Credential-Howto)
2. [Is it possible to Git merge / push using Jenkins pipeline](https://stackoverflow.com/a/48523179/13582118)
3. [Git Credentials - Git SCM](https://git-scm.com/docs/gitcredentials)
