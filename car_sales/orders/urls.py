from django.urls import path
from . import views


urlpatterns = [
    path('buy/<int:pk>', views.place_order, name='place_order'),
]