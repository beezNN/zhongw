"""guest URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from sign import views
from django.conf.urls import url

urlpatterns = [
    url('admin/', admin.site.urls),
    url(r'^index/$',views.index),  #添加index路径配置
    url(r'^login_action/$',views.login_action),  #添加login_action的路由
    url(r'^event_manage/$',views.event_manage),  #添加event_manage/的路由
    url(r'^acction/login/$',views.index),
    url(r'^search_name/$',views.search_name),   #添加搜索路由
    url(r'^guest_manage/$', views.guest_manage),  # 添加嘉宾路径路由
    url(r'^sign_index/(?P<event_id>[0-9]+)/$',views.sign_index),
    url(r'^sign_index_action/(?P<event_id>[0-9]+)/$', views.sign_index_action),
]
