from django import forms
from django.contrib.auth.forms import AuthenticationForm

from users.models import User


class UserLoginForm(AuthenticationForm):
    username = forms.CharField()
    password = forms.CharField()
    
    
    '''username = forms.CharField(label="Login",
        widget=forms.TextInput(attrs={"autofocus": True, "class": "form-control"})
    )
    password = forms.CharField(
        label=("Contraseña"),
        strip=False,
        widget=forms.PasswordInput(attrs={"autocomplete": "current-password", "class": "form-control"}),
    )'''

    class Meta:
        model = User
        fields = ['username', 'password']
