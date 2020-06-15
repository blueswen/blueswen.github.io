---
layout: post
title: "[10] ARTS Algorithm - Binary Tree Coloring Game"
subtitle: ""
author: "Blueswen"
header-style: text
tags:
    - ARTS
    - Algorithm
    - Tree
---

[1145. Binary Tree Coloring Game](https://leetcode.com/problems/binary-tree-coloring-game/)

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def btreeGameWinningMove(self, root: TreeNode, n: int, x: int) -> bool:
        def nodes(root: TreeNode, x, pair) -> int:
            if root is None:
                return 0
            l = nodes(root.left, x, pair)
            r = nodes(root.right, x, pair)
            if root.val == x:
                pair.append(l)
                pair.append(r)
            return 1 + l + r

        pair = [] # call by ref 做暫存
        nodes(root, x, pair)
        return max(n - (sum(pair) + 1), max(pair)) > int(n / 2)
```

因為上色只能從 parent, left, right 選一個，所以後手可以截斷先手的路，當截斷的那一側數量大於 n/2 就必定獲勝。因此需取得先手的三側的數量，left 與 right 用 recursion 取得，parent 那一側減去 left 與 right 即可，三側的最大值大於 n/2 則為 True。

Reference:

1. [花花酱 LeetCode 1145. Binary Tree Coloring Game - 刷题找工作 EP261](https://youtu.be/0MGbvRHYZxc)
