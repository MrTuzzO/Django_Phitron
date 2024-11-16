from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect
from . import forms
from .models import Musician


# Create your views here.
@login_required
def add_musician(request):
    if request.method == 'POST':
        form = forms.MusicianForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = forms.MusicianForm()

    return render(request, 'add_musician.html', {'form': form})

@login_required
def edit_musician(request, id):
    musician = Musician.objects.get(pk=id)
    form = forms.MusicianForm(instance=musician)

    if request.method == 'POST':
        form = forms.MusicianForm(request.POST, instance=musician)
        if form.is_valid():
            form.save()
            return redirect('home')

    return render(request, 'add_musician.html', {'form': form})
