from django.shortcuts import render
from django.http import HttpResponse

from goods.models import Categories

def index(request):
    categories = Categories.objects.all()
    context = {
        'title':'Home - main page',
        'content':'Home furniture shop',
        'categories':categories
    }
    return render(request, 'main/index.html', context)


def about(request):
    context = {
        'title':'Home - about use',
        'content':'Home furniture shop',
        'text_on_page': "Textotext"
    }
    return render(request, 'main/about.html', context)