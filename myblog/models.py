from django.db import models

# Create your models here.
class BlogPost(models.Model):
    title = models.CharField(max_length=150)
    body = models.TextField()
    timestamp = models.DateTimeField()

    def __str__(self):
        return self.title

class BlogTime(models.Model):
    time = models.DateTimeField()
    time_title = models.CharField(max_length=150)
    things = models.TextField()

    def __str__(self):
        return self.time_title

