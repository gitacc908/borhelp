from django.shortcuts import render, get_object_or_404
from .models import News


def blog(request):
    blogs = News.objects.all()
    return render(request, 'news/blog-list.html', {'blogs': blogs})


def blog_detail(request, pk):
    blogs = News.objects.all()
    blog = get_object_or_404(News, id=pk)
    return render(request, 'news/blog-detail.html', {'blog': blog, 'blogs': blogs})
