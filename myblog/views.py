from django.shortcuts import render
from .models import BlogPost, BlogTime
# Create your views here.

# Create your views here.
def blog_index(request):
    blog_list = BlogPost.objects.all()  # 获取所有博客数据
    return render(request, 'index.html', {'blog_list': blog_list})   # 返回index.html页面

def blog_time(request):
    blog_Time = BlogTime.objects.all()  # 获取所有时间轴的信息
    return render(request, 'time.html', {'blog_time': blog_Time}) # 返回time.html 页面

def blog_weichat(request):
    return render(request, 'weichat.html') # 返回time.html 页面
