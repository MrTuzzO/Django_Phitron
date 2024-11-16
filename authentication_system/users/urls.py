from django.contrib import admin
from django.urls import path, include
from . import views
urlpatterns = [
    path('signup/', views.register, name='signup'),
    path('profile/', views.profile, name='profile'),
    path('login/', views.UserLogin.as_view(), name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('edit/', views.edit_profile, name='edit_profile'),
    path('change_password/', views.change_password, name='change_password'),
]
