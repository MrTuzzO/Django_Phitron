from django.contrib.auth import logout, update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.contrib import messages
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from . import forms
from orders.models import Order


def signup(request):
    if request.method == 'POST':
        signup_form = forms.RegistrationForm(request.POST)
        if signup_form.is_valid():
            signup_form.save()
            messages.success(request, 'Your account has been created!')
            return redirect('profile')
    else:
        signup_form = forms.RegistrationForm()

    return render(request, 'signup.html', {'form': signup_form, 'title': 'Sign Up'})


class UserLogin(LoginView):
    template_name = 'signup.html'

    def get_success_url(self):
        return reverse_lazy('profile')

    def form_valid(self, form):
        messages.success(self.request, 'You have successfully logged in!')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, 'Please try again.')
        return super().form_invalid(form)

    def get_context_data(self, **kwargs):
        contex = super().get_context_data(**kwargs)
        contex['title'] = 'Sign In'
        return contex


@login_required
def profile(request):
    data = request.user
    user_orders = Order.objects.filter(user=request.user)
    return render(request, 'profile.html', {'data': data, 'user_orders': user_orders})


@login_required
def edit_profile(request):
    if request.method == 'POST':
        form = forms.EditProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been updated!')
            return redirect('profile')
    else:
        form = forms.EditProfileForm(instance=request.user)
    return render(request, 'edit_profile.html', {'form': form})


@login_required
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your password has been updated!')
            update_session_auth_hash(request, form.user)
            return redirect('profile')
    else:
        form = PasswordChangeForm(user=request.user)

    return render(request, 'change_password.html', {'form': form})


@login_required
def user_logout(request):
    logout(request)
    messages.success(request, 'You have been logged out!')
    return redirect('home')