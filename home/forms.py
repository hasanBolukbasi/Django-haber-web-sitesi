from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):
    username = forms.CharField(max_length=30, label='Kullanıcı adı')
    email = forms.EmailField(max_length=200)
    first_name = forms.CharField(max_length=100, label='Ad :')
    last_name = forms.CharField(max_length=100, label='Soyad :')

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'password1', 'password2')
