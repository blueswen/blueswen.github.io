---
layout: post
title: "Populating Next Right Pointers in Each Node"
subtitle: ""
author: "Blueswen"
header-style: text
tags:
    - ARTS
    - Algorithm
    - Tree
---

[116. Populating Next Right Pointers in Each Node](https://leetcode.com/problems/populating-next-right-pointers-in-each-node/)

把一個 Perfect Binary Tree 加上 next 的 node

```python
"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""


class Solution:
    def connect(self, root: "Node") -> "Node":
        if root is None or root.left is None:
            # 因為是 Perfect Binary Tree 所以 left 沒有值就可以停了
            return root
        root.left.next = root.right
        if root.next is not None:
            root.right.next = root.next.left
        self.connect(root.left) # recursive 跑完左邊
        self.connect(root.right) # recursive 跑完右邊
        return root
```

單獨從一個 current node 來看，current.left 的 next 為 current.right，right 的 next 為 current.next.left。一次就是只能拿到一組（current、left、right）的訊息，其他訊息都是無法拿到的。

Reference:

1. [花花酱 LeetCode 116. Populating Next Right Pointers in Each Node - 刷题找工作 EP265](https://youtu.be/YNu143ZN4qU)
