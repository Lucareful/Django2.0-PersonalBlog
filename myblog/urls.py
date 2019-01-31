from django.urls import path
from . import views

urlpatterns = [
	path(r'index.html', views.blog_index, name='blog_index'),
	path(r'time.html', views.blog_time, name='blog_time'),
	path(r'weichat.html',views.blog_weichat, name='blog_weichat'),

]
