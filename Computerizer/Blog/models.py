from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=64, default=None)

    def __str__(self):
        return f'{self.name}'

class Post(models.Model):
    status_choices = [
        ('Archived', 'archived'),
        ('Published', 'published'),
        ('Unpublished', 'unpublished')
    ]

    title = models.CharField(max_length=258)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    body = models.FilePathField(path=r'Blog\blogs')
    image = models.ImageField(upload_to = r'Computerizer/static/Blog/media')
    
    status = models.CharField(choices = status_choices, max_length=15)
    upload_date  = models.DateTimeField(auto_now_add=True)
    likes = models.PositiveIntegerField(default=0)
    views = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f'{self.title}'

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None)    
    body = models.TextField()
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    upload_date = models.DateTimeField(auto_now_add=True)
    likes = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f'{self.user}({self.post.title}): {self.body}'