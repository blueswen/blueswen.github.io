---
layout: post
title: "[14] ARTS Algorithm - Rotate List"
subtitle: ""
author: "Blueswen"
header-style: text
tags:
    - ARTS
    - Algorithm
---

[61. Rotate List](https://leetcode.com/problems/rotate-list/)

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if head is None or k == 0: # 為空或 k=0 時直接回傳原 list
            return head
        # 計算 list 的長度，決定要從哪邊切斷
        list_len = 1
        tail = head # 同時紀錄 tail node
        while tail.next:
            list_len += 1
            tail = tail.next
        # k > list_len 時，實際只需移動對 k 取 list_len 餘數次
        k = k % list_len
        if k == 0: # 取完餘數為零回傳原 list
            return head

        cur_node = head
        # 移動 list_len - k - 1 找到新的 head 的前一個 node
        for _ in range(list_len - k - 1):
            cur_node = cur_node.next
        new_head = cur_node.next
        tail.next = head
        cur_node.next = None
        return new_head
```

Example:

```txt
Input: 1->2->3->4->5->NULL, k = 2
Output: 4->5->1->2->3->NULL
Explanation:
rotate 1 steps to the right: 5->1->2->3->4->NULL
rotate 2 steps to the right: 4->5->1->2->3->NULL
```

```txt
list_len - k
     ^
{    |    }
1 -> 2 -> 3 -> 4 -> 5 -> NULL
          ^    ^
          |    |
          |    new_head
          cur_node
```

Reference:

1. [花花酱 LeetCode 61. Rotate List - 刷题找工作 EP365](https://youtu.be/a4XZu2VVE9Q)
