---
categories:
- Share
date: '2020-12-06'
tags:
- Python
- Django
- JWT
---

# Django Custom User with DRF and Simple JWT

Django 內建 [User Model](https://docs.djangoproject.com/en/3.1/ref/contrib/auth/#user-model) 供認證，但[官方文件](https://docs.djangoproject.com/en/3.1/topics/auth/customizing/#using-a-custom-user-model-when-starting-a-project)強烈建議在專案一開始就使用自訂的 User Model。因為未來若對 User Model 有調整需求，例如增加欄位，都只能使用自訂的 User Model，在一開始就使用內建的 User Model 會因為牽涉到各種 foreign ken 與多對多關係導致難以遷移([Changing to a custom user model mid-project](https://docs.djangoproject.com/en/3.1/topics/auth/customizing/#changing-to-a-custom-user-model-mid-project))。

[官方文件](https://docs.djangoproject.com/en/3.1/topics/auth/customizing/#a-full-example)提供了一個比較複雜的 Custom User 建立方式，但使用 AbstractBaseUser 或是 AbstractUser 是大家比較常用而且也相對簡單的方式。AbstractBaseUser 需要補充許多 User Model 的實作細節，而 AbstractUser 是 AbstractBaseUser 的 subclass，已經實作出一個完整的 User Model，單純只是調整欄位使用 AbstractUser 是最簡便的方式。

本範例使用 [Django REST framework](https://www.django-rest-framework.org/)(DRF) 做 API，並利用 [Simple JWT](https://github.com/SimpleJWT/django-rest-framework-simplejwt) 進行驗證。完整範例請參考 [Django Custom User with DRF and Simple JWT](https://github.com/Blueswen/django-custom-user)。

### Setup

1. 使用 virtualenv 建立虛擬環境
2. 安裝 package
3. 初始 Django project website
4. 建立 Django application account 用於放置 Custom User Model

```bash
$ mkdir django-custom-user && cd django-custom-user
$ python -m venv .venv
$ source .venv/bin/activate
$ pip install Django==3.1.4 djangorestframework==3.12.2 djangorestframework-simplejwt==4.6.0
(.venv) $ django-admin.py startproject website .
(.venv) $ python manage.py startapp account
(.venv) $ python manage.py runserver
```

### Custom User Model

1. 建立 Custom User Model
2. 更新 ```website/settings.py```，將 User Model 改為 Custom User Model
3. 執行 ```makemigrations``` 與 ```migrate``` 更新 DB
4. 建立 superuser admin 帳號

在 ```account/models.py``` 新增我們要用的 Custom User Model，這時就可以增加需要的欄位，例如生日等。

```py
# account/models.py
from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    birthday = models.DateField(null=True, blank=True, default=None)
    # add additional fields in here

    def __str__(self):
        return self.username

```

在 ```website/settings.py``` 需要加入我們增加的 account application，並增加 ```AUTH_USER_MODEL``` 設為我們新建的 Custom User Model，取代原本內建的 User Model。

```py
# website/settings.py
...
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'account.apps.AccountConfig', # new
]
...
AUTH_USER_MODEL = "account.CustomUser"
```

完成 ```AUTH_USER_MODEL``` 的設定後就可以執行首次的 ```makemigrations``` 與 ```migrate```，在調整 ```AUTH_USER_MODEL``` 前切勿執行！

```bash
(.venv) $ python manage.py makemigrations
(.venv) $ python manage.py migrate
```

建立 superuser 之後用於驗證。

```bash
(.venv) $ python manage.py createsuperuser
```

### Django REST framework

1. 新增 ```account/serializers.py```, ```account/views.py``` 與 ```account/urls.py```
2. 更新 ```website/settings.py``` 與 ```website/urls.py```

序列化查詢結果，除了 Customer User Model 外也增加了內建的 Group Model。輸出的 ```fields``` 設定為全部欄位，可依需求調整。

```py
# account/serializers.py
from .models import CustomUser
from django.contrib.auth.models import Group
from rest_framework import serializers


class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = "__all__"


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = "__all__"

```

設定 View 作為 API interface。

```py
# account/views.py
from .models import CustomUser
from django.contrib.auth.models import Group
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import CustomUserSerializer, GroupSerializer


class CustomUserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """

    queryset = CustomUser.objects.all().order_by("-date_joined")
    serializer_class = CustomUserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """

    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]

```

將 View 註冊到 router 中。

```py
# account/urls.py
from django.urls import include, path
from rest_framework import routers

from . import views

router = routers.DefaultRouter()
router.register(r"account/user", views.CustomUserViewSet)
router.register(r"account/group", views.GroupViewSet)

urlpatterns = [
    path("", include(router.urls)),
]

```

在 ```website/settings.py``` 的 ```INSTALLED_APPS``` 增加 ```rest_framework```。

```py
# website/settings.py
...
INSTALLED_APPS = [
    ...
    "rest_framework", # new
]
...
```

include 前面在 account 中設定的 url，並增加 api-auth 用於通過 DRF 的內建網頁認證。

```py
# website/urls.py
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include("account.urls")), # new
    path("api-auth/", include("rest_framework.urls", namespace="rest_framework")), # new
]

```

完成後就可以使用 ```curl``` 測試 API，帳號使用先前建立的 superuser。

```bash
$ curl -H 'Accept: application/json; indent=4' -u admin:admin http://127.0.0.1:8000/api/account/user/
[
    {
        "id": 1,
        "password": "pbkdf2_sha256$216000$fHERFJ7toIcI$3QOXbA4or+srGXn+60aW+z4rslvJkQcW2wS0oWWzYHI=",
        "last_login": "2020-12-07T15:46:50.478483Z",
        "is_superuser": true,
        "username": "admin",
        "first_name": "",
        "last_name": "",
        "email": "admin@sample.com",
        "is_staff": true,
        "is_active": true,
        "date_joined": "2020-12-07T13:54:21.479125Z",
        "birthday": null,
        "groups": [],
        "user_permissions": []
    }
]
```

或是開起 DRF 內建的網頁 [localhost:8000/api/account/user/](http://localhost:8000/api/account/user/)，如下圖：

![DRF](/img/in-post/2020-12-06-django-custom-user-with-drf-and-simple-jwt/drf.png)

從結果可以確認我們使用的 Custom User 有新增的 Birthday 欄位，superuser 也是建立在 Custom User Model 中。

### Simple JWT

1. 更新 ```website/settings.py```，調整預設認證 class
2. 更新 ```website/urls.py```，增加 Token 相關 API

設定 ```REST_FRAMEWORK``` 的 ```DEFAULT_AUTHENTICATION_CLASSES``` 為 Simple JWT。

```py
# website/settings.py
REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": (
        "rest_framework_simplejwt.authentication.JWTAuthentication",
    )
}
```

增加取得 Token 與更新 Token 的兩個 API。

```py
# website/urls.py
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    ...
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    ...
]
```

完成後可以使用先前建立的 superuser 取得 Token。

```bash
$ curl \
  -X POST \
  -H "Content-Type: application/json" \
  -d '{"username": "admin", "password": "admin"}' \
  http://localhost:8000/api/token/

{"refresh":"eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTYwNzQ0MzQ3NiwianRpIjoiYzQzYjM2Zjg2ODA0NDU1MzliYzUwNTlmN2YzN2NkMTEiLCJ1c2VyX2lkIjoxfQ.ZC0fAj7HR99v_po4BI-uVVeS9c7ZoN4B35_pYzosE_o","access":"eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjA3MzU3Mzc2LCJqdGkiOiIyYjY5NzkxMmZhNjE0NzY3YmJkNDA2NjExMzE1YzkxMCIsInVzZXJfaWQiOjF9.92m-V9vjRxUWGLlcJRFBdLqSHp0UII3SLPTt_yPynqY"}
```

將取得的 Token 加入 Header 中，再次測試 User 清單的 API。

```bash
$ curl -H 'Accept: application/json; indent=4' -H "Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjA3MzU3Mzc2LCJqdGkiOiIyYjY5NzkxMmZhNjE0NzY3YmJkNDA2NjExMzE1YzkxMCIsInVzZXJfaWQiOjF9.92m-V9vjRxUWGLlcJRFBdLqSHp0UII3SLPTt_yPynqY" http://127.0.0.1:8000/api/account/user/
[
    {
        "id": 1,
        "password": "pbkdf2_sha256$216000$fHERFJ7toIcI$3QOXbA4or+srGXn+60aW+z4rslvJkQcW2wS0oWWzYHI=",
        "last_login": "2020-12-07T16:02:06.847562Z",
        "is_superuser": true,
        "username": "admin",
        "first_name": "",
        "last_name": "",
        "email": "admin@sample.com",
        "is_staff": true,
        "is_active": true,
        "date_joined": "2020-12-07T13:54:21.479125Z",
        "birthday": null,
        "groups": [],
        "user_permissions": []
    }
]
```

Reference:

1. [Django Custom User Model](https://learndjango.com/tutorials/django-custom-user-model)
2. [自訂 Django User Model 的三種方式](https://codinganimal.info/%E8%87%AA%E8%A8%82-django-user-model-%E7%9A%84%E4%B8%89%E7%A8%AE%E6%96%B9%E5%BC%8F-becd8affc0df)
3. [Django REST framework](https://www.django-rest-framework.org/)
4. [SimpleJWT Document](https://django-rest-framework-simplejwt.readthedocs.io/)