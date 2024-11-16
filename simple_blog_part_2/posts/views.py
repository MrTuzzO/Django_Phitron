from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect
from . import forms
from . import models

@login_required
def add_post(request):
    if request.method == "POST":
        post_form = forms.AddPost(request.POST)
        if post_form.is_valid():
            post_form.instance.author = request.user
            post_form.save()
            return redirect('homepage')
    else:
        post_form = forms.AddPost()
    
    return render(request, 'add_post.html', {'form': post_form})

@login_required
def edit_post(request, id):
    post = models.Post.objects.get(pk=id)
    post_form = forms.AddPost(instance=post)

    if request.method == "POST":
        post_form = forms.AddPost(request.POST, instance=post)
        if post_form.is_valid():
            post_form.instance.author = request.user
            post_form.save()
            return redirect('homepage')
    
    return render(request, 'add_post.html', {'form' : post_form})

@login_required
def delete_post(request, id):
    post = models.Post.objects.get(pk=id)
    post.delete()
    return redirect('homepage')