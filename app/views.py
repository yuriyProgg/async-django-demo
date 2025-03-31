from django.http import HttpRequest
from django.shortcuts import render, redirect
from rest_framework.response import Response

from api_post import views


async def main_view(request: HttpRequest):
    return render(request, "main.html")


async def posts_view(request: HttpRequest):
    posts: Response = await views.PostAPIView.as_view()(request)
    if request.method == "GET":
        return render(request, "list.html", {"posts": posts.data})
    return redirect("posts")
