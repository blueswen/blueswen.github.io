---
layout: post
title: "[13] ARTS Share - Vue Bootstrap Admin Menu"
subtitle: ""
author: "Blueswen"
header-style: text
tags:
    - ARTS
    - Share
    - Vue
---

[vue-bootstrap-admin](https://github.com/Blueswen/vue-bootstrap-admin/tree/naive-dynamic-menu)：仿照 [vue-element-admin](https://github.com/PanJiaChen/vue-element-admin) 使用 Bootstrap 與 vue-router 依 Router 生成 Menu 的 Template。

Features:

1. 依 [router](https://github.com/Blueswen/vue-bootstrap-admin/blob/naive-dynamic-menu/src/router/index.js) 動態生成 Navbar，最多支援兩層的選單
2. 子選單 active 時，母選單也會有 active style

### Router

在 Router 中每個一級選單都視為一組 Group，第一個階 component 為 Layout，且都至少需要一個 Child 作為 router-view 內的內容，如 Home 的 Router 設定：

```js
{
  path: '/',
  redirect: '/home',
  component: Layout, // <== 第一階為 Layout
  children: [
    { // <== 實際要顯示的頁面
      path: '/home',
      name: 'Home',
      component: () => import('@/views/home'),
      meta: {
        title: 'Home' // <== 顯示在 Menu 的 Title
      }
    }
  ]
}
```

顯示兩層選單時，Child 則為多組，母選單的 Title 設定回歸第一階進行設定，如 About 的 Router 設定：

```js
{
  path: '/about',
  component: Layout,
  meta: {
    title: 'About' // <== 顯示在 Menu 第一層 的 Title
  },
  children: [
    {
      path: '/about',
      name: 'About',
      component: () => import('@/views/about'),
        meta: {
          title: 'About'
        }
    },
    {
      path: '/contact',
      name: 'Contact',
      component: () => import('@/views/contact'),
      meta: {
        title: 'Contact'
      }
    }
  ]
}
```

若有 Router 沒有要顯示在選單中，則可以設定 ```hidden=true```，如 Task 或 User 的 Router 設定：

```js
{
path: '/task',
  redirect: '/task/list',
  component: Layout,
  children: [
    {
      path: '/task/list',
      name: 'Task',
      component: () => import('@/views/task/task-list'),
      meta: {
        title: 'Task' // <== 因為 children 只剩下一個可顯示的選單，此 child 變為第一層選單，顯示在 Menu 第一層的 Title 由此決定
      }
    },
    {
      path: '/task/detail/:id',
      name: 'TaskDetail',
      component: () => import('@/views/task/task-detail'),
      hidden: true, // <== 不顯示在選單中
      props: true,
      meta: {
        title: 'Task Detail'
      }
    }
  ]
}
```

```js
{
  path: '/user',
  redirect: '/user/list',
  component: Layout,
  meta: {
    title: 'User' // <== 排除掉 hidden children 後，children 數 > 0，仍生成兩層選單，Menu 第一層 的 Title 由此決定
  },
  children: [
    {
      path: '/user/list',
      name: 'User',
      component: () => import('@/views/user/user-list'),
      meta: {
        title: 'User List'
      }
    },
    {
      path: '/user/detail/:id',
      name: 'UserDetail',
      component: () => import('@/views/user/user-detail'),
      hidden: true, // <== 不顯示在選單中
      props: true,
      meta: {
        title: 'User Detail'
      }
    },
    {
      path: '/user/dashboard',
      name: 'UserDashboard',
      component: () => import('@/views/user/dashboard'),
      meta: {
        title: 'User Dashboard'
      }
    }
  ]
}
```

Reference:

1. [vue-element-admin](https://github.com/PanJiaChen/vue-element-admin)
2. [vue-element-admin Document](https://panjiachen.gitee.io/vue-element-admin-site/zh/)
