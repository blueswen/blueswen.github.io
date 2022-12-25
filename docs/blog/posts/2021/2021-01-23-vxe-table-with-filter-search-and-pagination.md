---
categories:
- Share
date: '2021-01-23'
tags:
- Vue
---

# vxe-table with filter search and pagination

[vxe-table](https://github.com/x-extends/vxe-table) 是一款基於 Vue 的 PC 端表格元件，支援 CRUD、虛擬滾動、懶加載、分頁、樹狀顯示等功能，且有完善的 API 文件與大量範例。

文件中關於查詢與分頁的範例都較為複雜，一般常用以 filter 實現查詢的功能須自行實作。所以簡單寫了一個範例，詳細程式碼如下，也可以參考 [CodeSandbox](https://codesandbox.io/s/vxe-table-filter-search-nn8tf)。

App.js

```vue
<template>
  <div id="app">
    <vxe-grid
      border
      resizable
      show-overflow
      height="auto"
      :columns="tableColumn"
      :toolbar-config="{ slots: { buttons: 'toolbar_buttons' } }"
      :data="tableData"
      :pager-config="tablePage"
      @page-change="handlePageChange"
    >
      <template v-slot:toolbar_buttons>
        <vxe-form>
          <vxe-form-item title="Filter">
            <template v-slot>
              <vxe-input v-model="keyword" placeholder="Search" clearable />
            </template>
          </vxe-form-item>
        </vxe-form>
      </template>

      <template v-slot:empty>
        <span style="color: red">
          <p>Data Not Found</p>
        </span>
      </template>
    </vxe-grid>
  </div>
</template>

<script>
export default {
  name: "App",
  data() {
    return {
      tableColumn: [
        { field: "code", title: "Customer Code" },
        { field: "title", title: "Customer Name", showHeaderOverflow: true },
      ],
      tablePage: {
        total: 0,
        currentPage: 1,
        pageSize: 5,
        align: "center",
        layouts: [
          "PrevJump",
          "PrevPage",
          "Number",
          "NextPage",
          "NextJump",
          "FullJump",
          "Total",
        ],
        perfect: true,
      },
      customerList: [
        { code: "001", title: "one" },
        { code: "002", title: "two" },
        { code: "003", title: "three" },
        { code: "004", title: "four" },
        { code: "005", title: "five" },
        { code: "006", title: "six" },
        { code: "007", title: "seven" },
        { code: "008", title: "eight" },
        { code: "009", title: "nine" },
        { code: "010", title: "ten" },
      ],
      keyword: "",
    };
  },
  computed: {
    filteredData() {
      const lowerKeyworkd = this.keyword.toLowerCase();
      return lowerKeyworkd
        ? this.customerList.filter(
            (row) =>
              row.code.toLowerCase().includes(lowerKeyworkd) ||
              row.title.toLowerCase().includes(lowerKeyworkd)
          )
        : this.customerList;
    },
    tableData() {
      return this.filteredData.slice(
        (this.tablePage.currentPage - 1) * this.tablePage.pageSize,
        this.tablePage.currentPage * this.tablePage.pageSize
      );
    },
  },
  watch: {
    filteredData(newValue) {
      this.tablePage.total = newValue.length;
    },
  },
  methods: {
    handlePageChange({ currentPage, pageSize }) {
      this.tablePage.currentPage = currentPage;
      this.tablePage.pageSize = pageSize;
    },
  },
};
</script>

<style>
#app {
  margin: 20px;
}
</style>
```

main.js

```js
import Vue from "vue";
import App from "./App.vue";

import "xe-utils";
import VXETable from "vxe-table";
import VXETablePluginElement from "vxe-table-plugin-element";

Vue.config.productionTip = false;

Vue.use(VXETable);
VXETable.use(VXETablePluginElement);

new Vue({
  render: (h) => h(App)
}).$mount("#app");

```