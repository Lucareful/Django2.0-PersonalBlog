from django.db import models
# 导入内建的User模型
from django.contrib.auth.models import User
# timezone用于处理时间相关事务
from django.utils import timezone
from django.urls import reverse
# Create your models here.


class BlogArticle(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()
    content = models.TextField(null=True, blank=True)
    # 该字段为增加的字段，类型为FileField,且上传的图片会保存到media文件夹中
    cover = models.FileField(upload_to='media', null=True) 
    timestamp = models.DateTimeField()

    def __str__(self):
        return self.title


class ArticlePost(models.Model):
    """
    # 添加下面这个函数
    # 获取文章地址
    """
    def get_absolute_url(self):
        return reverse('article:article_detail', args=[self.id])
