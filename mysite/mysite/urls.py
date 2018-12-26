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
from django.contrib import admin
from django.urls import path
from django.shortcuts import HttpResponse,render
# 保存了路径和函数的对应关系
def yimi(request):
    # request参数保存了所有和用户浏览器请求相关的数据
    #　自己找html文件
    # with open('./templates/yimi.html','r',encoding='utf-8') as f:
    #     data = f.read()
    # return HttpResponse(data)
    # Django找
    return render(request,'yimi.html')
def login(request):
    # request参数保存了所有和用户浏览器请求相关的数据
    #　自己找html文件
    # with open('./templates/yimi.html','r',encoding='utf-8') as f:
    #     data = f.read()
    # return HttpResponse(data)
    # Django找
    return render(request,'login.html')

def xiaohei(request):
    # request参数保存了所有和用户浏览器请求相关的数据
    return HttpResponse(b'hello,xiaohei!')
urlpatterns = [
    path('yimi/', yimi),
    path('xiaohei/', xiaohei),
    path('login/', login),
    # path('admin/', admin.site.urls),
]
