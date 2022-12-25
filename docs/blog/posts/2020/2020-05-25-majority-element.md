---
categories:
- Algorithm
date: '2020-05-25'
tags: []
---

# Majority Element

[169. Majority Element](https://leetcode.com/problems/majority-element/)

```python
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count_map = {}
        max_count = 0
        majority = None
        for num in nums:
            cur_count = count_map.get(num, 0) + 1
            count_map[num] = cur_count
            if cur_count > max_count:
                majority = num
                max_count = cur_count
        return majority
```

Reference:

1. [花花酱 LeetCode 169. Majority Element - 刷题找工作 EP101](https://youtu.be/LPIvL-jvGdA)