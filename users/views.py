from django.shortcuts import render, redirect
from .forms import *
from django.contrib.auth import login, logout


def register(request):
    user_form = UserCreationForm(request.POST)
    profile_form = ProfileForm(request.POST or None, request.FILES or None)
    if request.method == 'POST':
        if user_form.is_valid():
            user = user_form.save()
            if profile_form.is_valid():
                Profile.objects.create(user=user, **profile_form.cleaned_data)
                return redirect('auth:login')
    return render(request, 'register.html', {'user_form': user_form, 'profile_form': profile_form})


def sign_in(request):
    form = LoginForm(data=request.POST or None)
    if request.method == 'POST' and form.is_valid():
        user = form.get_user()
        login(request, user)
        return redirect('house:home')
    errors = form.errors.as_data()
    return render(request, 'login.html', {'form': form, 'errors':errors})


def profile(request):
    profile = Profile.objects.get(user=request.user)
    return render(request, 'profile.html', {'profile': profile})


def out(request):
    logout(request)
    return redirect('house:home')
