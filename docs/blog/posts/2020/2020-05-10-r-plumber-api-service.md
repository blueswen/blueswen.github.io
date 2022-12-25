---
categories:
- Share
date: '2020-05-10'
tags:
- R
- Docker
---

# R Plumber - API Service

[Plumber](https://www.rplumber.io/) 是一個可以用於架設 API 服務的 R package，並能根據註解內容產生 Swagger Spec，不過目前還沒有支援 requestBody 的 Swagger Spec 生成。

範例如下，主要分為定義 API 的 ```api.R``` 與執行服務的 ```run.R```

```R
# api.R

#* Echo back the input
#* @param msg The message to echo
#* @get /echo
function(msg=""){
  list(msg = paste0("The message is: '", msg, "'"))
}

#* Return the sum of two numbers
#* @param a The first number to add
#* @param b The second number to add
#* @post /sum
function(a, b){
  as.numeric(a) + as.numeric(b)
}
```

```R
# run.R
library(plumber)
r <- plumb("api.R")  # Where 'plumber.R' is the location of the file shown above
r$run(port=8000)
```

Plumber 提供了多種 [Hosting](https://www.rplumber.io/docs/hosting.html) 的範例，其中也包括了 Docker，並提供了可以使用的 Image [trestletech/plumber](https://hub.docker.com/r/trestletech/plumber)。

在 Plumber 的 [Dockerfile](https://hub.docker.com/r/trestletech/plumber/dockerfile) 可以發現他們是使用 ```install2.r``` 這個 Script 安裝 package。與 python 不同 R 並沒有像是 pip 這種 package manager，因此要在建置 Image 時安裝 package 並沒有一個比較通用的方法。[littler](http://dirk.eddelbuettel.com/code/littler.html) 的 [install2.r](https://github.com/eddelbuettel/littler/blob/master/inst/examples/install2.r) 提供了比較偏向 CLI 的方式安裝 R 的 Package，並支援了多種功能，如平行安裝加快安裝速度等。

install2.r 使用範例：

```bash
install2.r -l /tmp/lib Rcpp BH                    # install into given library
install2.r -- --with-keep.source drat             # keep the source
install2.r -- --data-compress=bzip2 stringdist    # prefer bz2 compression
install2.r \".\"                                  # install package in current directory
install2.r -n 6 ggplot2                           # parallel install: (6 processes)
```

Reference:

1. [What is the current state of R package mangers in 2019?](https://community.rstudio.com/t/what-is-the-current-state-of-r-package-mangers-in-2019/25143/3)