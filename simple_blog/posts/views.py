from django.shortcuts import redirect
from django.urls import reverse_lazy
from . import forms
from . import models
from django.views.generic import CreateView, UpdateView, DeleteView, DetailView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

@method_decorator(login_required, name='dispatch')
class AddPost(CreateView):
    model = models.Post
    form_class = forms.PostForm
    template_name = 'add_post.html'
    success_url = reverse_lazy('profile')
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


@method_decorator(login_required, name='dispatch')
class EditPost(UpdateView):
    model = models.Post
    form_class = forms.PostForm
    template_name = 'add_post.html'
    pk_url_kwarg = 'id'
    success_url = reverse_lazy('profile')

@method_decorator(login_required, name='dispatch')
class DeletePost(DeleteView):
    model = models.Post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('profile')
    pk_url_kwarg = 'id'
    
class PostDetailView(DetailView):
    model = models.Post
    pk_url_kwarg = 'pk'
    template_name = 'post_details.html'

    def post(self, request, *args, **kwargs):
        comment_form = forms.CommentForm(data= self.request.POST)
        post = self.get_object()
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.post = post
            new_comment.save()
        return self.get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        contex = super().get_context_data(**kwargs)
        post = self.object
        comments = post.comments.all()
        comment_form = forms.CommentForm()
        contex['comments'] = comments
        contex['comment_form'] = comment_form
        return contex