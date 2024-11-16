from django.shortcuts import render
from categories.models import Category
from posts.models import Post
from categories.models import Category


def home(request, category_slug=None):
    data = Post.objects.all()
    category_obj = None
    if category_slug:
        category_obj = Category.objects.get(slug=category_slug)
        data = Post.objects.filter(category=category_obj)

    categories = Category.objects.all()
    return render(request, 'home.html', {'data': data, 'categories': categories, 'selected_category': category_obj})
