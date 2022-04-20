from django.shortcuts import render
from .models import News


def blog(request):
    blogs = News.objects.all()
    return render(request, 'news/blog-list.html', {'blogs': blogs})
