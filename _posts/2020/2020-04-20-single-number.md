---
layout: post
title: "Single Number"
subtitle: ""
author: "Blueswen"
header-style: text
tags:
    - ARTS
    - Algorithm
---

[136. Single Number](https://leetcode.com/problems/single-number/)

```python
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        collect_set = set()
        for n in nums:
            if n in collect_set:
                collect_set.remove(n)
            else:
                collect_set.add(n)
        return collect_set.pop()
```

時間複雜度為 ```O(n^2)```，for loop 與 in 都會執行 ```O(n)``` 次。

空間複雜度為 ```O(n)```，collect_set 長可能為 ```O(n)```。
