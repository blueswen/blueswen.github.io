---
categories:
- Algorithm
date: 2020-11-30
tags: []
---

# Longest Substring Without Repeating Characters

[3. Longest Substring Without Repeating Characters](https://leetcode.com/problems/longest-substring-without-repeating-characters/)

```python
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hash_dict = {}
        ans = 0
        i = 0
        for j, w in enumerate(s):
            i = max(i, hash_dict.get(w, -1) + 1)
            ans = max(ans, j - i + 1)
            hash_dict[w] = j
        return ans
```

Reference:

1. [Blind Curated 75](https://leetcode.com/list/xoqag3yj/)
2. [花花酱 LeetCode 3. Longest Substring Without Repeating Characters - 刷题找工作 EP295](https://youtu.be/LupZFfCCbAU)
