from rest_framework import serializers
from users.models import User
from posts.models import Post

class UserSerializer(serializers.ModelSerializer):
    posts_num = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ['id', 'username', 'password', 'email', 'posts_num']
        extra_kwargs = {'password': {'write_only': True}}

    def get_posts_num(self, obj):
        return Post.objects.filter(user=obj).count()