---
categories:
- Algorithm
date: 2020-05-18
tags: []
---

# Array Partition I

[561. Array Partition I](https://leetcode.com/problems/array-partition-i/)

```python
class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort() # 小到大排序
        result = 0
        for i in range(0, len(nums), 2): # 兩兩一組，取每組的第一個數字
            result += nums[i]
        return result
```

Reference:

1. [花花酱 LeetCode 561. Array Partition I - 刷题找工作 EP8](https://youtu.be/wDU72F6dhS4)
