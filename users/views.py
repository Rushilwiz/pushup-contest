from django.shortcuts import render, redirect

from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

from .forms import UserRegisterForm
from .models import Profile

from django.contrib import messages

# Create your views here.
def login(request):
    return render(request, 'users/login.html')

def signup(request):
    if request.POST:
        print(request.POST)
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            key = form.cleaned_data.get('key')
            if Profile.objects.filter(key=key).count() == 1:
                profile = Profile.objects.get(key=key)
                if profile.isEnabled == False:
                    instance = form.save(commit=False)
                    instance.save()
                    instance.first_name = profile.first_name
                    instance.last_name = profile.last_name
                    instance.save()
                    profile.user = instance
                    profile.isEnabled = True
                    profile.save()
                    messages.success(request, f'Your account has been created! You are now able to log in')
                    return redirect('login')
                else:
                    messages.error(request, 'This account is alr activation', extra_tags='danger')
            else:
                messages.error(request, 'Looks like your key was invalid!', extra_tags='danger')
        else:
            messages.error(request, 'Looks like there were some problems with your form!', extra_tags='danger')
    
    form = UserRegisterForm()

    return render(request, 'users/signup.html', {'form': form})


@login_required
def logout(request):
    auth_logout(request)
    return redirect('/')

    