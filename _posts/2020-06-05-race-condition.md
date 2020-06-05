---
layout: post
title: "[8] ARTS Share - Race Condition"
subtitle: ""
author: "Blueswen"
header-style: text
tags:
    - ARTS
    - Share
    - Go
    - Python
    - Thread
---

Race Condition 競爭條件，或稱作 Race Hazard 競爭危害，此詞源自於兩個訊號試著彼此競爭，來影響誰先輸出。常見的情景是當兩個 Thread 同時修改一個變數時，導致變數出現非預期的結果，如有兩個 Thread 想要執行 ```a++```，而實際上 ```a++``` 需要執行三個動作：

1. 取得 a
2. 執行 a + 1
3. 執行結果存回 a

執行結果可能如下圖：

![Race Condition](/img/in-post/2020-06-05-race-condition/rece-condition.png)

原本預期會要執行兩次 ```a++``` 變為 32，但結果卻是 31。

Race Condition 是利用 Multi Thread 做 Concurrency（併發）會產生的現象，為了避免這個問題可以在非 Thread-Safe 的操作加上鎖的機制包裝。

#### Golang

Go 可以利用 goroutine(```go func()```) 快速建立多個 thread，```sync.Mutex.Lock()``` 與 ```sync.Mutex.Unlock()``` 可以用於上鎖與解鎖。

```go
func main() {
    a := 0
    times := 10000
    c := make(chan bool)

    var m sync.Mutex

    for i := 0; i < times; i++ {
        go func() {
            m.Lock() // <== 上鎖
            a++
            m.Unlock() // <== 解鎖
            c <- true
        }()
    }

    for i := 0; i < times; i++ {
        <-c
    }
    fmt.Printf("a = %d\n", a)
}
```

#### Python

在 python 的 CPython 中因為 GIL (Global Interpreter Lock) 的關係，一個 process 必定只會有一個 thread 在執行 python，其他的執行緒都在等待 IO 或是睡覺。但 GIL 並不能保證不會出現 race condition，例如執行 ```a+=1``` 時在切換到別的 thread 的時候可能會剛好切在中間，因此仍須要鎖來保護共用變數。

```python
a = 0
lock = threading.Lock()

def foo():
    global a
    with lock: # <== 上鎖
        a += 1
```

也因為 GIL 的關係 multi thread 並無法加速 CPU bound 任務，只能用來加速 IO bound 任務，如併發大量 http request 等。如果要加速 CPU bound 任務的話要使用 multi process，若使用 multi thread 反而會因為頻繁操作 GIL 導致比單 thread 更慢。

Reference:

1. [用一個小例子談談 Golang 中的 Race Condition](https://larrylu.blog/race-condition-in-golang-c49a6e242259)
2. [深入 GIL: 如何寫出快速且 thread-safe 的 Python](https://blog.louie.lu/2017/05/19/%E6%B7%B1%E5%85%A5-gil-%E5%A6%82%E4%BD%95%E5%AF%AB%E5%87%BA%E5%BF%AB%E9%80%9F%E4%B8%94-thread-safe-%E7%9A%84-python-grok-the-gil-how-to-write-fast-and-thread-safe-python/)
3. [初淺聊聊 Python 的 GIL 及 Thread-safe](https://blog.gcos.me/post/2019-11-26_python-gil-and-thread-safe/)
4. [Does thread-safe mean no race conditions?](https://stackoverflow.com/questions/58720109/does-thread-safe-mean-no-race-conditions)
5. [Threading vs Multiprocessing in Python](https://medium.com/practo-engineering/threading-vs-multiprocessing-in-python-7b57f224eadb)
