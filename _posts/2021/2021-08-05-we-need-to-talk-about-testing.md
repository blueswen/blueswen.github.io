---
layout: post
title: "We need to talk about testing"
subtitle: ""
author: "Blueswen"
header-style: text
tags:
    - ARTS
    - Review
    - Testing
---

[We need to talk about testing](https://dannorth.net/2021/07/26/we-need-to-talk-about-testing/)

### The purpose of testing

每次異動程式碼，都有可能破壞以下這些特性，導致壞事發生

1. Functional correctness: It doesn’t produce the results we expect.
2. Reliability: It mostly shows correct answers but sometimes it doesn’t.
3. Usability: Sure it works but it is inconsistent and frustrating to use.
4. Accessibility: Like usability, but exclusionary and probably illegal.
5. Predictability: It has random spikes in resources such as memory, I/O, or CPU usage, or occasionally hangs for a noticeable amount of time.
6. Security: It works as designed but it exposes security vulnerabilities.
7. Compliance: It works but it doesn’t handle personal information correctly, say.
8. Observability: It mostly works, but when it doesn’t it is hard to identify why.

組織中有一群人關心著以上這些特性，這些人即為 stakeholders。他們代表了這個產品在不同面向上所呈現的風險與品質。

The purpose of testing is to ***increase confidence*** for ***stakeholders*** through ***evidence***.

測試的目的是透過 **證據** 提高 **利益相關人** 對產品的 **信心**

1. Stakeholders: 不只是直接與產品直接相關的開發者、使用者，任何間接相關的人都算是 Stakeholder，例如維運人員、合規人員、稽核人員等任何關心上面提到的特性的人
2. Increasing confidence: 了解 Stakeholder 關心哪些事，讓他們晚上能夠睡得更好
3. Evidence: 透過資訊或數據證明，而不是要 Stakeholder 依賴你的承諾、保證或是名聲

Three “superpowers” that associate with a testing mindset

1. Empathy: 同理心，從 Stakeholder 的角度看問題，理解他們在意的事情，了解他們為什麼會有那些疑慮
2. Scepticism: 懷疑論，對任何事情都保持懷疑的態度，提出假設、設計實驗、試圖證偽，積極地提出預測並證實，而不只是透過歸納法解釋過去的觀測結果
3. Ingenuity: 匠心，把 Stakeholder 在意的事情做到最好的決心與能力

### Test-Driven Development - a sidebar

TDD, BDD(behaviour-driven development), ATDD(acceptance test–driven development) 不是用來取代 Testing，而是被設計來作為一種開發技巧。

### Is test coverage a useful metric?

程式碼覆蓋度(test coverage or code coverage)是否有用端看 Stakeholders 關注的是什麼，若他關注的是安全性，程式碼覆蓋度無法提供任何資訊。程式碼覆蓋度只能確保這份 Code 有自動化測試，並符合定義的測試案例，無法保證任何案例都可以得到預期結果。

### What does it mean to “shift testing left”?

不單純只是盡早執行各種測試，而是要儘早把 Stakeholders 關注的東西納入考量中，例如開發時就思考合規、安全性等議題。

---

[Ant 大](https://www.facebook.com/yftzeng.tw)在 [FB](https://www.facebook.com/yftzeng.tw/posts/10216065373106529) 分享了這篇文章，[九一大](https://www.facebook.com/hatelove)在貼文下也針對文中說明提到 TDD, BDD, ATDD 不該取代 Testing 分享了他的看法

>針對2的部分，想用 TDD/BDD/ATDD 來做測試（達到測試目的）的人，是不是本身就該先了解一下這些名詞的「全名」。
>
>他們都是 development 的方法，他們也都不是用來取代測試。
>
>所以 yes, 如果拿這些來取代測試，是錯的。
>
>拿這些來做需求分析、情境分析、驗證「已知的東西」是否符合預期，都很合適。
>
>用來驗證那些你不知道的東西，就不是自動化能做的。
>
>這也是為什麼有一派的測試，指出自動化測試的部分不應該叫 testing, 而是 validation 或 check。
>
>真正的測試更偏向探索測試類型的。
>
>-Joey Chen
