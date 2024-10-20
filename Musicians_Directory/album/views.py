from django.shortcuts import render, redirect
from album.forms import AlbumForm
from album.models import Album


# Create your views here.
def add_album(request):
    if request.method == 'POST':
        form = AlbumForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = AlbumForm()

    return render(request, 'add_album.html', {'form': form})

def edit_album(request, id):
    album = Album.objects.get(pk=id)
    album_form = AlbumForm(instance=album)

    if request.method == 'POST':
        form = AlbumForm(request.POST, instance=album)
        if form.is_valid():
            form.save()
            return redirect('home')

    return render(request, 'add_album.html', {'form': album_form})

def delete_album(request, id):
    album = Album.objects.get(pk=id)
    album.delete()
    return redirect('home')
