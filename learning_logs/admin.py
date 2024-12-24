from django.contrib import admin

# 在这里注册你的模型
from .models import Topic, Entry

admin.site.register(Topic)
admin.site.register(Entry)
