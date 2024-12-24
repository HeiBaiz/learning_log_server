from django.db import models

# 在这里创建模型
class Topic(models.Model):
    """用户学习的主题"""
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        """返回模型的字符串表示"""
        return self.text
    
class Entry(models.Model):
    """学到的某个有关某个主题的具体知识"""
    # 让 Django 在删除主题的同时删除所有与之相关联的条目，这称为级联删除
    topic = models.ForeignKey(Topic, on_delete = models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add = True)
    
    # Meta 存储用于管理模型的额外信息
    class Meta:
        verbose_name_plural = 'entries'
        
    def __str__(self):
            """返回一个表示条目的简单字符串"""
            textLen = len(self.text)
            if textLen > 50:
                return f"{self.text[:50]}..."
            else:
                return f"{self.text[:50]}" 