"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# 从django的核心方法导入管理员方法
from django.contrib import admin
# 从django的路由方法导入 路径、包括方法
from django.urls import path,include

urlpatterns = [
    # 根路径 从apps中的blog中导入urls.py文件，
    # 这里的意思就是包括了apps中的blog中urls.py的内容
    path('',include('apps.blog.urls')),
    # 下面的这个路径是后台管理路径，后面我们写博文都在这个网址写
    # http://127.0.0.1:8000/admin
    path('admin/', admin.site.urls),
]
