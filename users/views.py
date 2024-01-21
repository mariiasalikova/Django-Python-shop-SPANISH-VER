
# Create your views here.
from django.contrib import auth
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from users.forms import UserLoginForm

def login(request):
    if request.method == "POST":
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user:
                auth.login(request, user)
                return HttpResponseRedirect(reverse('main:index'))
    else:
        #si no había enviado methodo POST ya - если еще не отправился пост-метод
        form = UserLoginForm()
    context = {
        'title':'Home - main page',
        'content':'HOME Furniture Shop',
        'form': form
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