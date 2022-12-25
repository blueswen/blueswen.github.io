---
categories:
- Algorithm
date: '2020-07-13'
tags:
- Tree
---

# Distribute Coins in Binary Tree

[979. Distribute Coins in Binary Tree](https://leetcode.com/problems/distribute-coins-in-binary-tree/)

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def distributeCoins(self, root: TreeNode) -> int:
        ans = [0]

        def balance(root: TreeNode, ans):
            if root is None:
                return 0
            l = balance(root.left, ans)
            r = balance(root.right, ans)
            ans[0] += abs(l) + abs(r)
            return root.val - 1 + l + r

        balance(root, ans)
        return ans[0]
```

Reference:

1. [花花酱 LeetCode 979. Distribute Coins in Binary Tree - 刷题找工作 EP243](https://youtu.be/zQqku1AXVF8)