from django.test import TestCase
from ..models import Author, Post, Comment
from django.contrib.auth.models import User

class TestBlogModels(TestCase):
    def setUp(self):
        self.author = Author.objects.create(name='Yousef')
        self.post = Post.objects.create(title ='Post', author=self.author, body = r'body.txt', image=r'cat.jpg', status = 'archived')
        self.user = User.objects.create(username = 'test', password = '1234')

    def test_post_author(self):
        self.assertEqual(self.author, self.post.author)

    def test_comments_in_one_post(self):
        comments = []
        for i in range(3):
            comments.append(Comment.objects.create(user = self.user, body = 'something', post = self.post))

        for comment in comments:
            self.assertEqual(comment.post, self.post)

    def test_comment_user(self):
        comment = Comment.objects.create(user = self.user, body = 'something', post = self.post)    
        self.assertEqual(comment.user , self.user)    