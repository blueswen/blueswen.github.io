---
layout: post
title: "Remove Nth Node From End of List"
subtitle: ""
author: "Blueswen"
header-style: text
tags:
    - ARTS
    - Algorithm
---

[19. Remove Nth Node From End of List](https://leetcode.com/problems/remove-nth-node-from-end-of-list/)

### List

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        node_list = []
        cur = head
        while cur != None:
            node_list.append(cur)
            cur = cur.next
        size = len(node_list)
        if n == 1 and n == size: # remove the only one node
            return None
        if n == size: # remove head
            return node_list[1]
        node_list[-n - 1].next = node_list[-n].next
        return head
```

### One pass algorithm

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        target_node = None # parent of removed node
        count = 0
        cur = head
        while cur is not None:
            if count == n:
                if target_node is None:
                    target_node = head
                else:
                    target_node = target_node.next
            else:
                count += 1
            cur = cur.next
        if target_node == head and target_node.next is None: # remove the only one node
            return None
        if target_node is None: # remove head
            return head.next
        target_node.next = target_node.next.next
        return head

```

Reference:

1. [Blind Curated 75](https://leetcode.com/list/xoqag3yj/)
