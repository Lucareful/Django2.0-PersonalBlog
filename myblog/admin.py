from django.contrib import admin
from .models import BlogPost, BlogTime

# Register your models here.
class BlogsPostAdmin(admin.ModelAdmin):
    list_display = ['title', 'body', 'timestamp','id']

class BlogTimeLine(admin.ModelAdmin):
    list_display  = ['time', 'time_title', 'things', 'id']

admin.site.register(BlogPost,BlogsPostAdmin)

admin.site.register(BlogTime, BlogTimeLine)