---
categories:
- Algorithm
date: 2020-04-13
tags:
- Bitwise
---

# Number of 1 Bits

[191. Number of 1 Bits](https://leetcode.com/problems/number-of-1-bits/submissions/)

```python
class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        while (n != 0):
            if (n >> 1 << 1 != n): # 右移再左移後不相等表示有一個 1 被丟掉
                count +=1
            n >>= 1
        return count
```

輸入為 int，判斷為二進位表示法時有幾個 1。使用二進位左移`<<` 跟右移`>>`([BitwiseOperators](https://wiki.python.org/moin/BitwiseOperators))，右移再左移後不相等表示有一個 1 被丟掉，一直右移到 n == 0 為止。
