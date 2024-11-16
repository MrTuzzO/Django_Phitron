from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms
from django.contrib.auth.models import User


class RegisterUserForm(UserCreationForm):
    first_name = forms.CharField(label='First Name', widget=forms.TextInput(attrs= {'id' : 'required'}))
    last_name = forms.CharField(label='Last Name', widget=forms.TextInput(attrs = {'id' : 'required'}))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')


class UserUpdateForm(UserChangeForm):
    password = None

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')
