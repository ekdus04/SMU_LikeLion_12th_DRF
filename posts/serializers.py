from rest_framework import serializers
from posts.models import Post, Comment, Like
from users.serializers import UserSerializer

class PostSerializer(serializers.ModelSerializer):
    user = UserSerializer(required=False)

    class Meta:
        model = Post
        fields = '__all__'
    
class CommentSerializer(serializers.ModelSerializer):
    user = UserSerializer(required=False)
    post = PostSerializer(required=False)

    class Meta:
        model = Comment
        fields = '__all__'

class LikeSerializer(serializers.ModelSerializer):
    user = UserSerializer(required=False)
    post = PostSerializer(required=False)

    class Meta:
        model = Like
        fields = '__all__'