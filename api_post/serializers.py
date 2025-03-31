from adrf.serializers import ModelSerializer
from api_post import models


class PostSerializer(ModelSerializer):
    class Meta:
        model = models.Post
        fields = "__all__"
