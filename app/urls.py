from django.urls import path
from app import views

urlpatterns = [
    path("", views.main_view, name="main"),
    path("posts", views.posts_view, name="posts"),
]
