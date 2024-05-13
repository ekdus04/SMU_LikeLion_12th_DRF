from rest_framework import serializers
from posts.models import Post
from users.serializers import UserSerializer

class PostSerializer(serializers.ModelSerializer):
    user = UserSerializer(required=False)

    class Meta:
        model = Post
        fields = '__all__'