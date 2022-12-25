---
categories:
- Algorithm
date: '2020-07-06'
tags: []
---

# Top K Frequent Words

[692. Top K Frequent Words](https://leetcode.com/problems/top-k-frequent-words/)

```python
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        word_map = {}
        for word in words:
            word_map[word] = word_map.get(word, 0) + 1
        return [
            item[0]
            for item in sorted(word_map.items(), key=lambda item: (-item[1], item[0]))[
                0:k
            ]
        ]
```

python 自訂排序邏輯使用 ```key``` 指定 function，組成 tuple 的話會依序往後比，在前面的 Priority 越高。

先 value(count) 大到小排列 => -item[1]，再 key(word) 字典排序(小到大) => item[0]，最後取前 K 筆。

Reference:

1. [Sort a list by multiple attributes?](https://stackoverflow.com/a/4233482/13582118)