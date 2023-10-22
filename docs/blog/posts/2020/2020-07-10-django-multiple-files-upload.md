---
categories:
- Share
date: 2020-07-10
tags:
- Django
---

# Django Multiple Files Upload

Django 的 [Filefield](https://docs.djangoproject.com/en/3.0/ref/models/fields/#django.db.models.FileField) 用於儲存上傳檔案的路徑，一般的範例大多是上傳單一個檔案，但在實務中批次上傳多個檔案是更常見的需求，有時可能還會搭配更新檔案的功能。

以下範例為透過 Django REST framework 做 API，上傳時將檔案存至當天日期的資料夾。如果資料夾內已有同樣檔名的檔案則進行覆蓋，並更新上傳時間。

完整程式碼可以參考 [django-multiple-files-upload](https://github.com/Blueswen/django-multiple-files-upload)。

### HTML

一個簡單的上傳頁面 HTML 如下

```html
<!-- templates/index.html -->

<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <h1>Upload Files</h1>
    <form enctype="multipart/form-data" action="/api/files/multiple_files_upload/" method="post">
        <input type="file" name="files" multiple>
        <button type="submit">Upload</button>
    </form>
</body>
</html>
```

### settings.py

1. 設定 ```MEDIA_ROOT```、```MEDIA_URL``` 指定上傳檔案的根目錄與 URL
2. 增加 ```TEMPLATES``` 的 ```DIRS``` 讀取上傳頁面的 HTML
3. ```INSTALLED_APPS``` 增加 rest_framework 與 upload app

```python
# main/settings.py

# 上傳檔案的根目錄
MEDIA_ROOT = os.path.join(BASE_DIR, "upload_files/")
# 上傳檔案目錄的 URL
MEDIA_URL = "/upload_files/"

...

TEMPLATES = [
    {
        ...
        "DIRS": [os.path.join(BASE_DIR, "templates").replace("\\", "/")], # 設定上傳頁面的 templates 位置
        ...
    },
]

...

# 增加 rest_framework 與 upload app
INSTALLED_APPS = [
    ...
    "rest_framework",
    "upload.apps.UploadConfig",
]

...
```

### models.py

在 upload app 中定義儲存上傳檔案的 model

```FileField``` 的參數設定 ```upload_to``` 設定上傳檔案的位置，```storage``` 處理重複檔案的問題

```python
# upload/models.py

import os
from django.conf import settings
from django.db import models
from django.core.files.storage import FileSystemStorage
import datetime

def file_directory_path_instance(instance, filename, *args, **kwargs):
    return file_directory_path(filename)


def file_directory_path(filename, *args, **kwargs):
    return "/".join([datetime.datetime.today().strftime("%Y-%m-%d"), filename])


# https://docs.djangoproject.com/en/3.0/topics/files/#file-storage
class OverwriteStorage(FileSystemStorage):
    def get_available_name(self, name, max_length=None):
        # 如果已經存在則先刪除
        if self.exists(name):
            os.remove(os.path.join(settings.MEDIA_ROOT, name))
        return name


class File(models.Model):
    file_id = models.AutoField(primary_key=True, verbose_name="檔案編號")
    upload_file = models.FileField(
        null=True,
        blank=True,
        upload_to=file_directory_path_instance, # 指定上傳的位置
        storage=OverwriteStorage(), # 處理重複檔案的問題
        verbose_name="檔案",
    )
    # auto_now = True => instance 更新時自動更新時間
    upload_time = models.DateTimeField(verbose_name="上傳時間", auto_now=True)
```

### views.py

在 ```upload``` app 的 view 設定 ```FileViewSet``` 並新增 ```multiple_files_upload``` action

```multiple_files_upload``` 處理邏輯同 [update_or_create](https://docs.djangoproject.com/en/3.0/ref/models/querysets/#update-or-create)，但須調整 ```upload_file``` 為實際上傳的檔案路徑。若直接使用 update_or_create ```upload_file``` 的值只會有檔案名稱而已，導致查詢結果的判斷錯誤。

```python
# upload/views.py

from django.shortcuts import render
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import (
    File,
    file_directory_path,
)
from .serializers import FileSerializer
from rest_framework import viewsets


# 上傳頁面
def upload(request):
    return render(request, "index.html")


class FileViewSet(viewsets.ModelViewSet):
    queryset = File.objects.all()
    serializer_class = FileSerializer

    @action(detail=False, methods=["post"])
    def multiple_files_upload(self, request, *args, **kwargs):
        # 取得 file list
        files = request.FILES.getlist("files")
        for upload_file in files:
            try:
                # 查詢指定路徑是否有檔案
                obj = File.objects.get(
                    # upload_file 必須更改為上傳後的位置，因此使用 file_directory_path
                    upload_file=file_directory_path(upload_file.name) 
                )
                obj.upload_file = upload_file
                obj.save()
            except File.DoesNotExist:
                # 查無時新增
                new_values = {"upload_file": upload_file}
                obj = File(**new_values)
                obj.save()
        return Response({"msg": "ok"})
```

### urls.py

設定 API 與頁面的 URL

```python
# main/urls.py

from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from upload.views import upload
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),
    path("upload/", upload),
    path("api/", include("upload.urls")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
```

```python
# upload/urls.py

from django.urls import include, path
from rest_framework import routers

from . import views

router = routers.DefaultRouter()
router.register(r"files", views.FileViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
```

### Run server

程式碼完成後 migrate DB，再啟動 Server

``` bash
python manage.py makemigrations
python manage.py migrate
python manage.py run server 6001
```

[localhost:6001/upload/](localhost:6001/upload/) 可以開啟上傳檔案的頁面。完成上傳後 [localhost:6001/api/files/](localhost:6001/api/files/) 能夠檢視 Files 的資料，upload_file 欄位的 URL 也可以直接點擊開啟該檔案。

Reference:

1. [Github - python-django-upload-multiple-files](https://github.com/kdchang/python-django-upload-multiple-files)
