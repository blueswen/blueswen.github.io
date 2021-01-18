---
layout: post
title: "[17] ARTS Algorithm - Longest Palindromic Substring"
subtitle: ""
author: "Blueswen"
header-style: text
tags:
    - ARTS
    - Algorithm
---

[5. Longest Palindromic Substring](https://leetcode.com/problems/longest-palindromic-substring/)

```python
class Solution:
    def longestPalindrome(self, s: str) -> str:
        def getLen(s, l, r):
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            return r - l - 1

        maxLen = 0
        start = 0
        for i in range(len(s)):
            curMax = max(getLen(s, i, i), getLen(s, i, i + 1))
            if curMax <= maxLen:
                continue
            maxLen = curMax
            start = i - (curMax - 1) // 2
        return s[start : start + maxLen]
```

Reference:

1. [Blind Curated 75](https://leetcode.com/list/xoqag3yj/)
2. [花花酱 LeetCode 5. Longest Palindromic Substring - 刷题找工作 EP292](https://youtu.be/g3R-pjUNa3k)
