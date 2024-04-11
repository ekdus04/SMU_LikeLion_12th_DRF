from rest_framework import serializers
from likes.models import Like
from users.serializers import UserSerializer
from posts.serializers import PostSerializer


class LikeSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    post = PostSerializer()

    class Meta:
        model = Like
        fields = '__all__'
