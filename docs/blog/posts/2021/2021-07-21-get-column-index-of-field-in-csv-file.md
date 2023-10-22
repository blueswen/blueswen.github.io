---
categories:
- Tip
date: 2021-07-21
tags:
- Unix
---

# Get column index of field in CSV file

get-column-index-of-field-in-csv-file

需求：取得有標頭的 CSV 檔中指定欄位的 index

解法：使用 ```sed``` 將標頭的分隔符號 ```,``` 取代為換行符號，接著使用 ```grep``` 搜尋要查詢的欄位名稱並回傳行數

```bash
# some.csv
# a,b,c,d,e,f,g
# 11,22,33,44,55,66,77
# ...

sed -n $'1s/,/\\\n/gp' some.csv | grep -nx 'e'
#output: 5:e

sed -n $'1s/,/\\\n/gp' some.csv | grep -nx 'e' | cut -f 1 -d :
#output: 5
```

sed 參數說明：

1. ```-n```: 同 ```--quiet``` 與 ```--silent```，只列出處理有處理過的那一行，sed 是預設印出所有內容
2. ```$'...'```: [ANSI-C Quoting](https://www.gnu.org/software/bash/manual/html_node/ANSI_002dC-Quoting.html)，能夠以 ```\n``` 或 ```\t``` 的方式表示換行或 Tab，單純的 quotes 只會被視為一般文字
3. ```1s/,/\\\n/gp```: 以 ```/``` 分割為四段
   1. ```1s```: ```1``` 表示只處理第一行，```s``` 表示進行取代
   2. ```,```: 要被取代的內容
   3. ```\\\n```: 要取代的內容，因為換行符號的 ```\``` 處理兩次跳脫，因此前面有額外的兩個 ```\```，一次為 sed 的正規表達式的跳脫，另一次為 shell 的跳脫
   4. ```gp```: ```g``` 表示所有內容都要取代，```p``` 表示把處理後的結果直接印出

grep 參數說明：

1. ```-n```: 同時回傳查詢到的行數
2. ```-x```: 只回傳整行都符合查詢內容的文字

或者也可以使用 ```tr``` 取代 ```sed``` 的取代功能

```bash
# some.csv
# a,b,c,d,e,f,g
# 11,22,33,44,55,66,77
# ...

head -n 1 some.csv | tr "," "\n" | grep -nx e
#output: 5:e
```

另外也可以再搭配 ```cut``` 直接取出該欄的整排資料

```bash
# some.csv
# a,b,c,d,e,f,g
# 11,22,33,44,55,66,77
# ...

cut -f $(sed -n $'1s/,/\\\n/gp' some.csv | grep -nx 'e' | cut -f 1 -d :) -d , some.csv
#output:
# e
# 55
```

Reference:

1. [How to get column index of field in unix shell](https://stackoverflow.com/a/39782016/13582118)
2. [How does the leading dollar sign affect single quotes in Bash?](https://stackoverflow.com/a/11966402/13582118)
3. [Pass the output of previous command to next as an argument](https://unix.stackexchange.com/a/108797)
4. [Remove backslashes from a text file](https://unix.stackexchange.com/a/169210)
