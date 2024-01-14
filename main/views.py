from django.shortcuts import render
from django.http import HttpResponse



def index(request):
    context = {
        'title':'Home - main page',
        'content':'Home furniture shop',

    }
    return render(request, 'main/index.html', context)


def about(request):
    context = {
        'title':'Home - about use',
        'content':'Home furniture shop',
        'text_on_page': "Textotext"
    }
    return render(request, 'main/about.html', context)