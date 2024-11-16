from django.contrib.auth import logout, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import PasswordChangeForm
from django.shortcuts import render, redirect
from django.contrib import messages
from django.urls import reverse_lazy

from . import forms


# def porfile(request):
def register(request):
    if request.method == 'POST':
        register_form = forms.RegisterUserForm(request.POST)
        if register_form.is_valid():
            user = register_form.save()
            messages.success(request, f'Account created for {user.username}')
            return redirect('profile')
    else:
        register_form = forms.RegisterUserForm()

    return render(request, 'register.html', {'form': register_form})


class UserLogin(LoginView):
    template_name = 'register.html'

    def get_success_url(self):
        return reverse_lazy('profile')

    def form_valid(self, form):
        messages.success(self.request, 'Login successful!')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, 'Invalid credentials')
        return super().form_invalid(form)

    def get_context_data(self, **kwargs):
        contex = super().get_context_data(**kwargs)
        contex['title'] = 'Login'
        return contex


@login_required
def profile(request):
    data = request.user
    return render(request, 'profile.html', {'data': data})


@login_required
def edit_profile(request):
    if request.method == 'POST':
        form = forms.UserUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('profile')
    else:
        form = forms.UserUpdateForm(instance=request.user)

    return render(request, 'edit_profile.html', {'form': form})


@login_required
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


@login_required
def user_logout(request):
    logout(request)
    messages.success(request, f'You have been logged out')
    return redirect('home')
