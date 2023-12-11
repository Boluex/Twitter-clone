from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.db.models import Q
# Create your models here.
class posts(models.Model):
    author=models.ForeignKey(User,on_delete=models.CASCADE)
    title=models.CharField(max_length=200)
    image=models.ImageField(upload_to='post_images')
    content=models.TextField()
    date_posted=models.DateTimeField(default=timezone.now)

class comment(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    post=models.ForeignKey(posts,on_delete=models.CASCADE)
    image=models.ImageField(upload_to='comment_images')
    content=models.CharField(max_length=300)
    date_posted=models.DateTimeField(auto_now_add=True)


class follow_button(models.Model):
    follower=models.ForeignKey(User,on_delete=models.CASCADE,related_name='follower')
    following=models.ForeignKey(User,on_delete=models.CASCADE,related_name='following')


class like_button(models.Model):
    post=models.ForeignKey(posts,on_delete=models.CASCADE,related_name='post')
    user=models.ForeignKey(User,on_delete=models.CASCADE,related_name='user')


