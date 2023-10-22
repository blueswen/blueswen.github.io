---
categories:
- Algorithm
date: 2020-04-06
tags:
- Tree
---

# Sum of Left Leaves

[404. Sum of Left Leaves](https://leetcode.com/problems/sum-of-left-leaves/)

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        return sum_left_node(root, False)

def sum_left_node(root:TreeNode, is_left:bool) -> int:
    if root is None:
        return 0
    if root.left or root.right:
        return sum_left_node(root.left, True) + sum_left_node(root.right, False)
    else:
        if is_left:
            return root.val
        else:
            return 0
```

用 recursive 解，透過 is_left 當 flag 判斷是否要加該 node 的值
