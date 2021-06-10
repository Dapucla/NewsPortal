from django.db import models
from django.contrib.auth.models import User
from django.db.models import Sum


class Author(models.Model):
    author_rating = models.FloatField(default=0.0)

    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)

    def updateRating(self):
        postRat = self.post_set.agregate(postRating=Sum('post_rating'))
        pRat = 0
        pRat += postRat.get('postRating')
        commentRat = self.user.comment_set.agregate(commentRating=Sum('comment_rating'))
        cRat = 0
        cRat += commentRat.get('commentRating')
        self.authors_rating = pRat * 3 + cRat
        self.save()


class Category(models.Model):
    name = models.CharField(max_length=255, unique=True)


class Post(models.Model):

    article = 'AR'
    news = 'NE'

    POST = [
        (article, 'Статья'),
        (news, 'Новость'),
    ]

    name = models.CharField(max_length=255, unique=True)
    post_type = models.CharField(max_length=2, choices=POST, default=None)
    post_datetime = models.DateTimeField(auto_now_add=True)
    post_title = models.CharField(max_length=255)
    post_text = models.TextField(default="")
    post_rating = models.FloatField(default=0.0)

    post_category = models.ManyToManyField(Category, through='PostCategory')
    author = models.ForeignKey(Author, on_delete=models.CASCADE, null=True, default=0)

    def like(self):
        self.post_rating += 1

    def dislike(self):
        self.post_rating -= 1

    def preview(self):
        return self.post_text[0:123] + "..."

    def __str__(self):
        return f'{self.name.title()}: {self.post_text[:20]}'


class PostCategory(models.Model):
    post_info = models.ForeignKey(Post, on_delete=models.CASCADE)
    post_category = models.ForeignKey(Category, on_delete=models.CASCADE)


class Comment(models.Model):
    post_info = models.ForeignKey(Post, on_delete=models.CASCADE)
    comment_user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment_text = models.TextField(default="")
    comment_datetime = models.DateTimeField(auto_now_add=True)
    comment_rating = models.FloatField(default=0.0)

    def like(self):
        self.comment_rating += 1

    def dislike(self):
        self.comment_rating -= 1