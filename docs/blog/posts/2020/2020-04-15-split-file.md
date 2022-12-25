---
categories:
- Tip
date: '2020-04-15'
tags:
- Unix
---

# split large csv file

分割過大的 csv file 供使用，先使用 `split` 切分，再透過 `sed` 插入標頭。

```bash
# -l 每 3 行切分，-d 改用數字編碼分割後檔案
split -l 3 -d file.csv file.csv.part.

# 取得 header
header=$(head -n 1 file.csv)

# 移除第一份的 header
tail -n +2 file.csv.part.00 > file.csv.part.00.tmp
mv file.csv.part.00.tmp file.csv.part.00
rm file.csv.part.00.tmp

# 切割後的資料在第一行都加上 header
sed -i '1i$header' file.csv.part.*
```

Reference:

1. [How to Split Large Text File into Smaller Files in Linux](https://linoxide.com/linux-how-to/split-large-text-file-smaller-files-linux/)
2. [BASH: Prepend A Text / Lines To a File](https://www.cyberciti.biz/faq/bash-prepend-text-lines-to-file/)
3. [Split large csv file and keep header in each part](https://stackoverflow.com/a/37386401)