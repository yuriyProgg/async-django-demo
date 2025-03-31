from adrf.generics import ListCreateAPIView, DestroyAPIView
from api_post.models import Post
from api_post.serializers import PostSerializer


class PostAPIView(ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostDestroyAPIView(DestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
