from django.urls import path
from . import views

app_name= 'news'

urlpatterns = [
    path('', views.blog, name='news'),
    path('<int:pk>/', views.blog_detail, name='blog-detail')
]
