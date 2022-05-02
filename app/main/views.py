from django.shortcuts import render
from main.models import Landing
from django.http import HttpResponseNotFound


def main_page(request):
    return render(request, "main/main.html", context={'page': 'main'})


def contacts(request):
    return render(request, "main/contacts.html", context={'page': 'contacts'})


def humanitarian(request):
    return render(request, "main/humanitarian.html", context={'page': 'humanitarian'})


def medical(request):
    return render(request, "main/medical.html", context={'page': 'medical'})


def migration(request):
    return render(request, "main/migration.html", context={'page': 'migration'})


def peremoga(request):
    return render(request, "main/peremoga.html", context={'page': 'peremoga'})


def gallery(request):
    return render(request, "main/gallery.html", context={'page': 'gallery'})


def page_detail(request, pk):
    try:
        page = Landing.objects.get(id=pk)
    except:
        return HttpResponseNotFound("Not found")   
    return render(request, 'main/detail.html', {'page': page, 'current': 'page'})
