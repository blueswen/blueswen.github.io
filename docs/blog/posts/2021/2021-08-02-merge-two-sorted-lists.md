---
categories:
- Algorithm
date: '2021-08-02'
tags: []
---

# Merge Two Sorted Lists

[21. Merge Two Sorted Lists](https://leetcode.com/problems/merge-two-sorted-lists/)

## Iteratively

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 is None or l2 is None:
            return l1 or l2
        head = None
        pre_node = None
        while l1 is not None or l2 is not None:
            if l1 is None:
                pre_node.next = l2
                break
            elif l2 is None:
                pre_node.next = l1
                break
            if l1.val < l2.val:
                cur_node = l1
                l1 = l1.next
            else:
                cur_node = l2
                l2 = l2.next
            if head is None:
                head = cur_node
            else:
                pre_node.next = cur_node
            pre_node = cur_node
        return head

```

## Recursively

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 is None or l2 is None:
            return l1 or l2
        if l1.val < l2.val:
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoLists(l1, l2.next)
            return l2

```

Reference:

1. [Blind Curated 75](https://leetcode.com/list/xoqag3yj/)