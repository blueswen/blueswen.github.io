---
layout: post
title: "Balance a Binary Search Tree"
subtitle: ""
author: "Blueswen"
header-style: text
tags:
    - ARTS
    - Algorithm
    - Tree
---

[1382. Balance a Binary Search Tree](https://leetcode.com/problems/balance-a-binary-search-tree/)

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        vals = get_node_vals(root)
        return build_tree(vals)


def get_node_vals(root: TreeNode) -> list:
    if root is None:
        return []
    else:
        # 原本的樹為 binary search tree，所以左邊小右邊大，照順序即為小、中、大
        return get_node_vals(root.left) + [root.val] + get_node_vals(root.right)


def build_tree(val_list):
    list_len = len(val_list)
    if list_len == 0:
        return None
    else:
        root = TreeNode(val_list[list_len // 2])
        # 最左邊到中間的 list
        root.left = build_tree(val_list[: list_len // 2])
        # 中間到最右邊的 list
        root.right = build_tree(val_list[list_len // 2 + 1 :])
        return root

```

分兩步驟解，先把值取出來，再重建新的樹

1. 遞迴取值  
   因為後面建樹的時候會需要已經排序好的值，透過遞迴建 list 的時候要依照大小順序  
   時間複雜度為 ```O(n)```，要遍歷 n 個 node  
   空間複雜度為 ```O(n)```，要儲存長度為 n 的 list  
2. 遞迴建樹  
   如果想要平衡的樹的話，會需要取 list 中間的值當作 node，這樣左邊跟右邊的數量就會相等或只差一，遞迴這樣的操作即可  
   時間複雜度為 ```O(n)```，```2\*T(n/2) + O(1)```，```n/2``` 為對半分，```2\*T(n/2)``` 為左右各做一遍，```O(1)``` 為建 node 的操作  
   空間複雜度為 ```O(n))```，n 個節點  

Reference:

1. [花花酱 LeetCode 1382. Balance a Binary Search Tree - 刷题找工作 EP315](https://www.youtube.com/watch?v=U24USYuOWzw)
2. [花花酱 LeetCode 108 Convert Sorted Array to Binary Search Tree - 刷题找工作 EP306](https://www.youtube.com/watch?v=O5BSAhg4n0M)
