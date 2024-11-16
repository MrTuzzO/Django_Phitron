from django.contrib.auth.context_processors import auth
from django.shortcuts import render, redirect
from . import forms
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from posts.models import Post

def register(request):
    if request.method == 'POST':
        register_form = forms.RegistrationForm(request.POST)
        if register_form.is_valid():
            register_form.save()
            messages.success(request, 'Account created')
            return redirect('register')

    else:
        register_form = forms.RegistrationForm()

    return render(request, 'register.html', {'form': register_form, 'title': 'Register'})

def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                messages.success(request, 'You are now logged in')
                login(request, user)
                return redirect('profile')
            else:
                messages.error(request, 'Invalid username or password')
                return redirect('register')
    else:
        form = AuthenticationForm()

    return render(request, 'register.html', {"form": form, 'title': 'Login'})


@login_required
def profile(request):
    data = Post.objects.filter(author=request.user)
    return render(request, 'profile.html', {'data': data})

@login_required
def edit_profile(request):
    if request.method == 'POST':
        form = forms.updateUserData(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated')
            return redirect('profile')
    else:
        form = forms.updateUserData(instance=request.user)

    return render(request, 'edit_profile.html', {'form': form})

def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your password was successfully updated!')
            update_session_auth_hash(request, form.user)
            return redirect('profile')
    else:
        form = PasswordChangeForm(user=request.user)

    return render(request, 'change_password.html', {'form': form})

def user_logout(request):
    logout(request)
    return redirect('user_login')