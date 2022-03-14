---
layout: post
title: "Arrow keys not working in vim in Jupyter console"
subtitle: ""
author: "Blueswen"
header-style: text
tags:
    - ARTS
    - Tip
    - jupyter notebook
---

問題：vim 在 jupyter notebook console 使用時方向鍵行為異常，無法正常移動

解法：在 ```~/.vimrc``` 增加 ```:set term=builtin_ansi```

在 Windows 的 Unix console [Cmder](https://cmder.net/) 也有人遇到這個種問題，一樣可以用相同方式解決，但副作用為會影響 syntax highlighting。如果想要保持 syntax highlighting 可以參考[調整 key code mapping 的解法](https://github.com/microsoft/WSL/issues/1154#issuecomment-595951533)。

Reference:

1. [Arrow keys not working in vim in Jupyter console](https://github.com/jupyter/jupyter_console/issues/171)
