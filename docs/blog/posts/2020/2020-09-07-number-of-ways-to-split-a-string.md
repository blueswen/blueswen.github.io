---
categories:
- Algorithm
date: '2020-09-07'
tags: []
---

# Number of Ways to Split a String

[1573. Number of Ways to Split a String](https://leetcode.com/problems/number-of-ways-to-split-a-string/)

```python
class Solution:
    def numWays(self, s: str) -> int:
        total = 0
        for digit in s:
            total += int(digit)

        # total 無法被 3 整除必定無法切成三份
        if total % 3 != 0:
            return 0

        # 全為零的話有 n - 1 個切割點，C(n-1, 2) ＝> (n-1)! / (2!*(n-1-2)!)  => (n-1)(n-2) / 2
        if total == 0:
            return ((len(s) - 1) * (len(s) - 2) // 2) % (10 ** 9 + 7)

        # 找到單邊滿足足夠 1 到下一個 1 之間的切割點數量
        def count_cut(s: str, total: int) -> int:
            current_sum = 0
            cut_amount = 0
            for ind in range(0, len(s)):
                current_sum += int(s[ind])
                if current_sum > total / 3:
                    break
                elif current_sum == total / 3:
                    cut_amount += 1
            return cut_amount

        # 左邊切割點數量 * 右邊切割點數量
        return (count_cut(s, total) * count_cut(s[::-1], total)) % (10 ** 9 + 7)
```

切割點數量說明：

```txt
           | | | |     | | |  
0 0 1 0 0 1 0 0 0 1 0 1 0 0 1 1  
```

字串總和為 6，表示三份各自總和為 2，單邊開始逐一累加，累加為 2 時開始計算可切割點，當再遇到 1 就無法再切割，左右兩邊切割點相乘（4*3）為可能組合數。

Reference:

1. [花花酱 LeetCode 1573. Number of Ways to Split a String - 刷题找工作 EP354](https://youtu.be/gkFKRbkrIws)