from django.contrib import admin
from django.urls import path
from article import views

urlpatterns = [
	path(r'Article/<int:id>', views.Blog_Article, name='blog_article'),
	
	]