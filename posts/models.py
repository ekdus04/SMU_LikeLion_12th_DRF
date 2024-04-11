from django.db import models
from users.models import User

# Model이 id 자동 생성
class Post(models.Model):
    title = models.CharField(max_length=50, null=True)
    content = models.CharField(max_length=500, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(null=True, blank=True)
    view = models.IntegerField(default=0)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts', null=True)
