---
categories:
- Algorithm
date: 2021-01-25
tags: []
---

# Container With Most Water

[11. Container With Most Water](https://leetcode.com/problems/container-with-most-water/)

```python
class Solution:
    def maxArea(self, height: List[int]) -> int:
        ans = 0
        l = 0
        r = len(height) - 1
        while l != r:
            ans = max(ans, min(height[l], height[r]) * (r - l))
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return ans
```

Reference:

1. [Blind Curated 75](https://leetcode.com/list/xoqag3yj/)
2. [花花酱 LeetCode 11. Container With Most Water - 刷题找工作 EP121](https://youtu.be/IONgE6QZgGI)
