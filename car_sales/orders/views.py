from django.shortcuts import render, redirect
from cars.models import Car
from . models import Order
from django.contrib import messages
from django.contrib.auth.decorators import login_required


@login_required
def place_order(request, pk):
    car = Car.objects.get(pk=pk)
    if car.quantity>0:
        Order.objects.create(user = request.user, car = car)
        car.quantity -= 1
        car.save()
        messages.success(request, 'Your order has been placed.')
    else:
        messages.error(request, 'Out of Stock')

    return redirect('car_details', pk=car.pk)

