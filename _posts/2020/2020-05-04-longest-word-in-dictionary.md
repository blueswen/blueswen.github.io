---
layout: post
title: "Longest Word in Dictionary"
subtitle: ""
author: "Blueswen"
header-style: text
tags:
    - ARTS
    - Algorithm
---

[720. Longest Word in Dictionary](https://leetcode.com/problems/longest-word-in-dictionary/)

```python
class Solution:
    def longestWord(self, words: List[str]) -> str:
        best = ""
        for word in words:
            if (len(word)<len(best)) or (len(word) == len(best) and word > best):
                # 比 best 的短跳過，跟 best 一樣長，但字典排序比 best 大也跳過
                continue
            prefix = ""
            valid = True
            for ind in range(len(word)):
                prefix += word[ind]
                if not prefix in words:
                    valid = False
                    break
            if valid:
                best = word
        return best
```

Find the longest word in words that can be built one character at a time by other words in ```words```.  
找到一個最長，且這個字的從頭開始每增加一個字母的詞都在 ```words``` 中。

保留最佳解，如果遇到更好的再換掉，利用條件刪去不用判斷的

Reference:

1. [花花酱 LeetCode 720. Longest Word in Dictionary - 刷题找工作 EP109](https://www.youtube.com/watch?v=TqrZg4wYP1U)
