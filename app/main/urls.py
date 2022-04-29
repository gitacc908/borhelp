from django.urls import path

from main.views import main_page, contacts, humanitarian, medical, migration, peremoga, page_detail, gallery

app_name = 'main'

urlpatterns = [
    path('', main_page, name='main'),
    path('contacts/', contacts, name='contacts'),
    path('humanitarian/', humanitarian, name='humanitarian'),
    path('medical/', medical, name='medical'),
    path('migration/', migration, name='migration'),
    path('peremoga/', peremoga, name='peremoga'),
    path('gallery/', gallery, name='gallery'),
    path('page_detail/<int:pk>/', page_detail, name='detail'),
]
