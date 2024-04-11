from rest_framework import serializers
from hashtags.models import Hashtag
from posts.serializers import PostSerializer


class LikeSerializer(serializers.ModelSerializer):
    post = PostSerializer()

    class Meta:
        model = Hashtag
        fields = '__all__'
