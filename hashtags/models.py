from django.db import models
from posts.models import Post

class Comment(models.Model):
    category = models.CharField(max_length=20, null=True, blank=True)
    post = models.ManyToManyField(Post, related_name='hashtags')