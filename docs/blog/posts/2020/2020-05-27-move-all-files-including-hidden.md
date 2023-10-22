---
categories:
- Tip
date: 2020-05-27
tags:
- Unix
- Jenkins
---

# Move all files including hidden

需求：搬移指定資料夾中的檔案，同時包括隱藏的檔案

解法：使用 bash 的 ```shopt``` 設定 dotglob 跟 nullglob 讓 wildcard 可以取到 ```.``` 開頭的檔案 

```bash
shopt -s dotglob nullglob
mv Foo/* Bar/
```

[How do you move all files (including hidden) from one directory to another?](https://unix.stackexchange.com/a/6397) 提供了其他各種不同 shell 的解法。

在 Jenkins Pipeline 中若要使用 bash 需要在 ```sh``` 指令中指定 interpreter，[Jenkins Pipeline Doc](https://www.jenkins.io/doc/pipeline/steps/workflow-durable-task-step/#sh-shell-script)。

```groovy
node {
    sh """#!/bin/bash
        shopt -s dotglob nullglob
        mv Foo/* Bar/
    """
}
```

注意一定要設定為 ```"""#!/bin/bash```，這樣這份 shell 的第一行才是設定 interpreter。

Reference:

1. [How do you move all files (including hidden) from one directory to another?](https://unix.stackexchange.com/a/6397)
