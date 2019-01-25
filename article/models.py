from django.db import models

# Create your models here.
class BlogArticle(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()
    content = models.TextField(null=True, blank=True)
    #该字段为增加的字段，类型为FileField,且上传的图片会保存到media文件夹中
    cover = models.FileField(upload_to='media', null=True) 
    timestamp = models.DateTimeField()

    def __str__(self):
        return self.title

