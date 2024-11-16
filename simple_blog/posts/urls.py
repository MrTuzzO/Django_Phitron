from django.urls import path, include
from . import views

urlpatterns = [
    path('add/', views.AddPost.as_view(), name='add_post'),
    path('edit/<int:id>', views.EditPost.as_view(), name='edit_post'),
    path('delete/<int:id>', views.DeletePost.as_view(), name='delete_post'),
    path('details/<int:pk>', views.PostDetailView.as_view(), name='post_detail'),
]