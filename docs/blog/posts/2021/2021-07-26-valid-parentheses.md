---
categories:
- Algorithm
date: '2021-07-26'
tags: []
---

# Valid Parentheses

[20. Valid Parentheses](https://leetcode.com/problems/valid-parentheses/)

```python
class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0:
            return False
        stack = []
        left = ["(", "{", "["]
        right = [")", "}", "]"]
        for char in s:
            if len(stack) == 0 or char in left:
                stack.append(char)
            else:
                if stack[-1] == left[right.index(char)]:
                    stack.pop()
                else:
                    return False
        return len(stack) == 0

```

Reference:

1. [Blind Curated 75](https://leetcode.com/list/xoqag3yj/)