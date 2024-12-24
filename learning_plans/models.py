from django.db import models

# Create your models here.
class Plan(models.Model):
    """用户学习计划"""
    text = models.CharField(max_length = 200)
    data_added = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.text
