from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.modelsForm, name='modelsForm'),
]