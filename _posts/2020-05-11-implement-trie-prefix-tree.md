---
layout: post
title: "[5] ARTS Algorithm - Implement Trie (Prefix Tree)"
subtitle: ""
author: "Blueswen"
header-style: text
tags:
    - ARTS
    - Algorithm
---

[208. Implement Trie (Prefix Tree)](https://leetcode.com/problems/implement-trie-prefix-tree/)

```python
class Trie:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = {} # 用 dict 來儲存 node，key 為值，val 為子結點

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        cur_node = self.root
        for char in word:
            if char not in cur_node:
                cur_node[char] = {}
            cur_node = cur_node[char]
        cur_node["#"] = True # 有 hash tag 表示為該詞最後一個點

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        query_node = self.query(word)
        return query_node is not None and "#" in query_node

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        query_node = self.query(prefix)
        return query_node is not None

    def query(self, word: str) -> object:
        cur_node = self.root
        for char in word:
            if char not in cur_node:
                return None
            cur_node = cur_node[char]
        return cur_node


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)

```

[Trie](https://zh.wikipedia.org/wiki/Trie)：又稱字首樹或字典樹，讀作 tree 或 try。

Reference:

1. [花花酱 LeetCode 208. Implement Trie (Prefix Tree) - 刷题找工作 EP73](https://www.youtube.com/watch?v=f48wGD-MuQw)
