from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from .forms import SignUpForm, UpdateProfileForm


def index(request):
    form = SignUpForm()
    return render(request, 'index.html', {'form':form})


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()    
            return redirect('index')
    else:
        form = SignUpForm()
    return render(request, 'registration/signup.html', {'form': form})


def update_profile(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = UpdateProfileForm(request.POST, instance = request.user)
            if form.is_valid():
                form.save()
                return redirect('index')   
        else:
            form = UpdateProfileForm(instance = request.user)
        return render(request, 'profile_update.html', {'form':form})
    
    