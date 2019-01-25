from django.shortcuts import render
from .models import BlogArticle
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.conf import settings
# Create your views here.

def Blog_Article(request, id):
	# 取出相应的文章
	article_page = BlogArticle.objects.get(id=id)
	return render(request, 'Article.html', {'article_page': article_page})

'''def cover_list(request):
	# hava time to up
    articles = BlogArticle.objects.all().order_by('id')
    paginator = Paginator(articles, 1) # Show 25 contacts per page
    page = request.GET.get('page')
    try:
        contacts = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        contacts = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        contacts = paginator.page(paginator.num_pages)
    return render(request, 'list.html', {'articles': articles})
'''
def global_settings(request):
    titles = BlogArticle.objects.all()
    return {"titles": titles}
