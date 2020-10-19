from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile

class UserRegisterForm(UserCreationForm):
    key = forms.CharField(max_length=10, help_text="Enter the one word key that Rushil gave you. If you need a key, just DM rushil or sahishnu")

    class Meta:
        model = User
        fields = ['username', 'key', 'password1', 'password2']