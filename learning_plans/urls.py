"""定义 learning_plans 的 URL 模式"""

from django.urls import path

from . import views

app_name = 'learning_plans'
urlpatterns = [
    # 主页
    path('', views.index, name = "index"),
]
