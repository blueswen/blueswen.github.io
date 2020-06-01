---
layout: post
title: "[8] ARTS Algorithm - Pseudo-Palindromic Paths in a Binary Tree"
subtitle: ""
author: "Blueswen"
header-style: text
tags:
    - ARTS
    - Algorithm
    - Tree
    - Bitwise
---

[1457. Pseudo-Palindromic Paths in a Binary Tree](https://leetcode.com/problems/pseudo-palindromic-paths-in-a-binary-tree/)

計算 Binary Tree 中可以排列出回文的路徑。如果要能夠排列為回文的話，每個數字都是偶數個或只有一個數字是奇數個。

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
```

## 計數解

```python
class Solution:
    def pseudoPalindromicPaths(self, root: TreeNode) -> int:
        count = [0 for _ in range(9)] # 共用的計數 table

        def solve(node: TreeNode) -> int:
            if node is None:
                return 0
            count[node.val - 1] += 1
            c = 0
            if node.left is None and node.right is None:
                # leaf node，判斷是否符合回文條件
                odd = 0
                for i in range(9):
                    if count[i] % 2 == 1:
                        odd += 1
                if odd <= 1:
                    c = 1
            l = solve(node.left) # 計算左邊
            r = solve(node.right) # 計算右邊
            count[node.val - 1] -= 1 # 因為是共用的，所以要回復原狀
            return c + l + r

        return solve(root)
```

## Bitwise 解

其實並不需要計算每個的數量，只需要知道奇偶的狀態，因此可以使用 XOR(```^```) 來操作狀態變化。

0（偶） ^ 1 == 1（奇）；1（奇） ^ 1 == 0（偶）

000000000 ^= (1 << n)，第 n 個數字的奇偶變換

```python
class Solution:
    def pseudoPalindromicPaths(self, root: TreeNode) -> int:
        def solve(root: TreeNode, s: int) -> int:
            if root is None:
                return 0
            s ^= 1 << root.val
            ans = 0
            if root.left is None and root.right is None:
                if bin(s).count("1") <= 1: # 轉為 binary 後計算 1（奇）的數量
                    ans += 1
            ans += solve(root.left, s) # 算左邊
            ans += solve(root.right, s) # 算右邊
            # 與上面解法相比，因為是 int 所以是 call by value
            # 每個遞迴會拿到自己的一份，就不用共用與復原
            return ans

        return solve(root, 0) # s 初始為 0 == 000000000
```

Reference:

1. [花花酱 LeetCode 1457. Pseudo-Palindromic Paths in a Binary Tree - 刷题找工作 EP329](https://youtu.be/Ia2OAm9OzP0)
