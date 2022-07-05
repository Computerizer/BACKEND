from django.db import models

# Create your models here.
from distutils.command.upload import upload
from operator import mod
from django import views
from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Author(AbstractUser):
    pass

class Post(models.Model):
    title = models.CharField(max_length=258)
    #author = models.ForeignKey(Author, on_delete=models.CASCADE)
    body = models.TextField()
    image = models.ImageField(upload_to = r'Computerizer/static/Blog/media')
    upload_date  = models.DateTimeField(auto_now_add=True)
    likes = models.PositiveIntegerField(default=0)
    views = models.PositiveIntegerField(default=0)

class Comment(models.Model):
    #user = models.ForeignKey(Author, on_delete=models.CASCADE)    
    body = models.TextField()
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    upload_date = models.DateTimeField(auto_now_add=True)
    likes = models.PositiveIntegerField(default=0)