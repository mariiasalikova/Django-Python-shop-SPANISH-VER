from django.shortcuts import render
from django.http import HttpResponse

from goods.models import Categories

def index(request):
    context = {
        'title':'Home - main page',
        'content':'HOME Furniture Shop'
    }
    return render(request, 'main/index.html', context)


def about(request):
    context = {
        'title':'Home - about use',
        'content':'Home furniture shop',
        'text_on_page': "Textotext"
    }
    return render(request, 'main/about.html', context)