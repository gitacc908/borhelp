from django.urls import path
from . import views

app_name= 'news'

urlpatterns = [
    path('', views.blog, name='news'),
    path('<slug>/', views.blog_detail, name='blog-detail')
]
