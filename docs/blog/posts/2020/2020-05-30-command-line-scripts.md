---
categories:
- Share
date: 2020-05-30
tags:
- Python
---

# Python package include command line tools

許多 Python package 都會附帶 command line tools，如 [cookiecutter](https://github.com/cookiecutter/cookiecutter) 安裝後執行是直接執行 ```cookiecutter [template]```。command line tools 可以讓使用者更簡便地使用 package，而不用涉及任何 python 相關知識。

python 的 command line tools 共有 ```scripts``` 與 ```console_scripts``` 兩種，可以設定在 package 的 ```setup.py``` 中。

## scripts

```scripts``` 撰寫一個獨立的 shell script：

```txt
funniest/
    funniest/
        __init__.py
        ...
    setup.py
    bin/
        funniest-joke
    ...
```

```funniest-joke``` 檔案如下，透過設定 interpreter 的方式執行 python script

```python
#!/usr/bin/env python

import funniest
print funniest.joke()
```

在 ```setup.py``` 中設定為：

```python
setup(
    ...
    scripts=['bin/funniest-joke'],
    ...
)
```

安裝該 package 時會複製 script 到 PATH 中，就能以一般 command tool 的方式使用：

```bash
$ funniest-joke
```

因為 ```scripts``` 其實就是一個 shell，所以也可以單純寫一個 shell 或是定義其他的 interpreter，也不一定要執行 python script。

## console_scripts

```console_scripts``` 讓 python **function** 被註冊成一個 command line tool，package 結構如下：

```txt
funniest/
    funniest/
        __init__.py
        command_line.py
        ...
    setup.py
    ...
```

```command_line.py``` 中定義要用 command line tool 執行的 ```main``` function：

```python
import funniest

def main():
    print funniest.joke()
```

在 ```setup.py``` 中設定為：

```python
setup(
    ...
    entry_points = {
        'console_scripts': ['funniest-joke=funniest.command_line:main'],
    }
    ...
)
```

安裝該 package 時會生成一個 ```shim``` script，執行 ```command_line.py``` 並呼叫 ```main``` function，一樣以一般 command tool 的方式使用：

```bash
$ funniest-joke
```

Reference:

1. [python-packaging: Command Line Scripts](https://python-packaging.readthedocs.io/en/latest/command-line-scripts.html)
