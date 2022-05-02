from django.shortcuts import render, get_object_or_404
from .models import News


def blog(request):
    blogs = News.objects.all()
    return render(request, 'news/blog-list.html', {'blogs': blogs, 'page': 'blogs'})


def blog_detail(request, slug):
    blogs = News.objects.all()
    blog = get_object_or_404(News, slug=slug)
    blog.viewed +=1
    blog.save(update_fields=['viewed'])
    return render(request, 'news/blog-detail.html', {'blog': blog, 'blogs': blogs})