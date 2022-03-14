---
layout: post
title: "Rules of thumb for a 1x developer"
subtitle: ""
author: "Blueswen"
header-style: text
tags:
    - ARTS
    - Review
    - Rules of thumb
---

[Rules of thumb for a 1x developer](https://muldoon.cloud/programming/2020/04/17/programming-rules-thumb.html#rule-6-when-to-use-a-hardcore-language)

作者借用了 10x developer 的名字，整理了他覺得 1x developer 可以作為工作指引的 20 個經驗法則，透過這些法則希望能夠成為 1.1x developer。

總分為九類的法則：

1. Meta
   - Rule 1: Rules are good
     - 透過各種經驗法則建立思考的框架，利用邏輯結構化各種問題
2. Productivity and learning
   - Rule 2: Most of what I learn is useless outside of its immediate context
     - 如果工作中有大量沒有價值的部分，應該盡可能地避免，盡量關注在有價值的地方就好
   - Rule 3: Focus “learning time” on things that compound
     - 學習能夠產生複利的東西，或是進行能產生複利的行為，形成一個正向的循環。e.g. 閱讀無法產生複利，但如果能夠實際應用，甚至是分享就能達到複利。
3. Programming languages
   - Rule 4: When to use Java or C#
     - 大型商用軟體
   - Rule 5: When to use Python or Ruby
     - AI or ML
   - Rule 6: When to use a hardcore language
     - Go, Rust, Haskell, Erlang, Clojure, Kotlin, Scala 歸為此類
     - Go, Rust 用於對於效能需求較高的服務
     - Haskell, Erlang 用於簡潔或是數學方面的程式
   - Rule 7: How to do Javascript
     - 使用 Typescript，人生可以更簡單
     - 業務邏輯盡可能做在後端就好
     - 有互動需求使用 Vue 或 React
     - 記得做 unit tests
   - Rule 8: When to use C or C++
     - 通常不是你選擇 C，而是 C 選擇了你，因應場景被迫使用
     - C++ 有較佳的效能，常用在機器人或是高頻交易
   - Rule 9: Use PHP or Hack if you want to test server changes without rebuilding
4. Technologies
   - Rule 10: When to make a serverless function
     - 每一隔一段時間要執行的一小片段程式
   - Rule 11: Which database technology to choose
     - 有 ACID 需求就是乖乖用 SQL，推薦 PostgreSQL
5. Testing
   - Rule 12: When to write a unit test
     - 評估缺陷的可能性＊缺陷帶來的損失，如果寫測試的成本遠超過了期望值，似乎也沒有寫的必要。但每個片段的程式碼仍應該是要盡可能做到測試，或至少要寫的是可測試的。
   - Rule 13: When to write an integration test
     - 當功能包含不屬於你的 Code 時就要做 integration test，特別是 Code 可能在你不知情的狀況下被更動
   - Rule 14: When to write an end-to-end test
     - 可以定義為一個使用者案例，使用者可能是一個人或機器
     - 三個情境
       - 對於成品沒有完全瞭解，建立一些案例當作 Smoke Test，確保東西至少沒有壞
       - 需要迴歸執行的測試，可用於未來重構的依據
       - 牽涉複雜的計算，驗證一些其他的 Code 是否會對他產生影響
6. DevOps
   - Rule 15: When to bring on a dedicated support engineer
7. Security
   - Rule 16: If you delegate all your IT security to the InfoSec, they will come up with draconian rules
     - 如果讓資安部門決定所有資安相關規範，只會建立出極度嚴苛的規範
8. Designing and Whiteboarding
   - Rule 17: Make the design session about input, not approval
9. Project management
   - Rule 18: Estimates serve more for creating pressure than for project planning
     - 時程通常是只是用來製造壓力，而不是作為規劃的指引
   - Rule 19: Be explicit about the difference between hard deadlines, soft deadlines, internal deadlines, and expected completion dates
     - 分清楚四種不同的 Deadline
       - Hard deadline: Delay 會讓老闆或是公司很難看的狀況
       - Soft deadline: Delay 會讓某些人很難看的狀況
       - Internal deadline: 只會影響到團隊內的人，但不會影響到外部的人
       - Expected completion date: 團隊內部預期要完成的日期
   - Rule 20: When somebody says Agile, push for Kanban, not Scrum
     - 如果要跑 Agile 用 Kanban 不要用 Scrum
       - Scrum: 在這兩週完成這些事，外部給予的時間壓力
       - Kanba: 做兩週能完成的事，內部評估可完成的工作量
