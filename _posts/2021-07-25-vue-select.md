---
layout: post
title: "[20] ARTS Share - Vue Select"
subtitle: ""
author: "Blueswen"
header-style: text
tags:
    - ARTS
    - Share
    - Vue
---

[Vue Select](hhttps://vue-select.org/) 是一個擴充了多種功能的 Select Component。包括了篩選、搜尋、Tag、自訂顯示等功能，同時主打輕量化並可客製化。

簡單寫了一些範例，詳細程式碼如下，也可以參考 [CodeSandbox](https://codepen.io/blueswen/pen/mdmpOwM)。

1. country 為基礎的選單
2. author 的資料來源為 object list，可以自訂 value 與 label 要使用哪些值
3. customer 的資料來源為 object list，可以自訂下拉選單的呈現方式與查無訊息，並覆寫 [filter-by](https://vue-select.org/api/props.html#filterby) 同時用 customer.title 篩選

{% raw %}
```html
<script src="https://cdn.jsdelivr.net/npm/vue"></script>
<script src="https://unpkg.com/vue-select@latest"></script>
<link rel="stylesheet" href="https://unpkg.com/vue-select@latest/dist/vue-select.css">

<div id="app">
  <template>
    <div>
      <v-select v-model="country" :options="['Canada', 'United States']"></v-select>
      <div>country: {{ country }}</div>
      <v-select v-model="author_id" label="name" :reduce="item => item.id" :options="authorList" :clearable="false">
      </v-select>
      <div>author_id: {{ author_id }}</div>
      <v-select v-model="customer_code" label="code" :reduce="customer => customer.code" :options="customers" :filter-by="customerFilter">
        <template slot="no-options">
          查無客戶名稱或編號
        </template>
        <template slot="option" slot-scope="option">
          <div class="d-center">
            {{ option.code }} | {{ option.title }}
          </div>
        </template>
      </v-select>
      <div>customer_code: {{ customer_code }}</div>
    </div>
  </template>
</div>
```
{% endraw %}

```js
var Main = {
  data() {
    return {
      country: "",
      customer_code: "",
      customers: [
        { code: "001", title: "Apple" },
        { code: "002", title: "Microsoft" },
        { code: "003", title: "Facebook" }
      ],
      author_id: "",
      authorList: [
        { id: "001", name: "John" },
        { id: "002", name: "Peter" },
        { id: "003", name: "Jim" }
      ]
    };
  },
  methods: {
    customerFilter: function (option, label, search) {
      return (
        (label || "").toLowerCase().indexOf(search.toLowerCase()) > -1 ||
        (option["title"] || "").toLowerCase().indexOf(search.toLowerCase()) > -1
      );
    }
  }
};
Vue.component("v-select", VueSelect.VueSelect);
var vue = Vue.extend(Main);
new vue().$mount("#app");
```
