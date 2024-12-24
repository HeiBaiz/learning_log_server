"""定义 start 的 URL 模式"""

from django.urls import path

from . import views

# 区分其他应用程序中同名文件
app_name = 'start'
urlpatterns = [
    # 导航
    path('', views.index, name = 'index'),
]