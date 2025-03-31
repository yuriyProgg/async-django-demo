from django.urls import path
from api_post import views

urlpatterns = [
    path("list", views.PostAPIView.as_view(), name="api posts"),
    path("<pk>", views.PostDestroyAPIView.as_view(), name="api post destroy"),
]
