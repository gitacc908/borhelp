from .models import Landing


def header(request):
    pages = Landing.objects.all()
    return {'pages':pages} 
