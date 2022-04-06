from django.db import models
from django.contrib.auth.models import User
from Post.models import Post
# Create your models here.
class Comment(models.Model):
    title = models.CharField(max_length=200)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    content = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    