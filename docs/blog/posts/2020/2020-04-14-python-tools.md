---
categories:
- Review
date: '2020-04-14'
tags:
- Python
---

# Understanding Best Practice Python Tooling by Comparing Popular Project Templates

[Understanding Best Practice Python Tooling by Comparing Popular Project Templates](https://medium.com/better-programming/understanding-best-practice-python-tooling-by-comparing-popular-project-templates-6eba49229106)

作者分析了 18 個 github 上熱門的 python project template 所選擇的工具，大部分的 template 都使用 cookiecutter 建立，pytest 為主要的 test tool。

Up and Coming 中提到 [Pyproject.toml](https://www.python.org/dev/peps/pep-0518/) 以及 [Poetry](https://github.com/python-poetry/poetry) 都滿有趣的，是以前沒有注意到的新東西，Pyproject.toml 用於取代 setup.py，Poetry 用於取代 pip。

文章中也推薦了幾個不錯的 Data Science ([kedro](https://github.com/quantumblacklabs/kedro)、[cookiecutter-data-science](https://github.com/drivendata/cookiecutter-data-science))、Django 的 template，Data Science 的 template 對於專案上的管理似乎會滿有幫助的，有標準的資料架構下在交接專案時能夠輕鬆許多。

作者在發表後發了一則 tweet tag [Guido van Rossum](https://en.wikipedia.org/wiki/Guido_van_Rossum) 想知道他的看法，Guido van Rossum 也很快回覆了，他認為 Black 過譽了，除非團隊常為了 style 吵架。

前陣子也開始嘗試用一些看起來很厲害的 template 建 project，但後來還是選擇比較精簡的 template，畢竟工具不停推陳出新，等真的需要再加進來也不遲，過早的優化似乎只是徒增自己的困擾而已。