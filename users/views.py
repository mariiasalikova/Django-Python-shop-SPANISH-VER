
# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse

from goods.models import Categories

def login(request):
    context = {
        'title':'Home - main page',
        'content':'HOME Furniture Shop'
    }
    return render(request, 'users/login.html', context)


def registration(request):
    context = {
        'title':'Home - re'
    }
    return render(request, 'users/registration.html', context)


def profile(request):
    context = {
        'title':'Home - about use',
    }
    return render(request, 'users/profile.html', context)


def logout(request):
    ...