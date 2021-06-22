from news.models import Author, Category, Post, PostCategory, Comment
from django.contrib.auth.models import User
from django.db import models


user11 = User.objects.create_user(username='User11', email='user11@user11', password='user11password')
user22 = User.objects.create_user(username='User22', email='user22@user22', password='user22password')

author11 = Author.objects.create(user=user11)
author22 = Author.objects.create(user=user22)

category11 = Category.objects.create(name='Мотоциклы')
category22 = Category.objects.create(name='Скутеры')
category33 = Category.objects.create(name='Велосипеды')
category44 = Category.objects.create(name='Скейты')

article11 = Post.objects.create(author=author11,post_type=Post.article,post_title='Заголовок статьи 1',post_text='Текст статьи 1')
article22 = Post.objects.create(author=author22,post_type=Post.article,post_title='Заголовок статьи 2',post_text='Текст статьи 2')
news11 = Post.objects.create(author=author22,post_type=Post.news,post_title='Заголовок новости 11',post_text='Текст новости 11')

article11.post_category.add(category11)
article11.post_category.add(category22)
article22.post_category.add(category33)
news11.post_category.add(category44)

comment11 = Comment.objects.create(post_info=article11,comment_user=user11,comment_text='Текст комментария 1')
comment22 = Comment.objects.create(post_info=article11,comment_user=user22,comment_text='Текст комментария 2')
comment33 = Comment.objects.create(post_info=article22,comment_user=user11,comment_text='Текст комментария 3')
comment44 = Comment.objects.create(post_info=news11,comment_user=user22,comment_text='Текст комментария 4')

comment11.like()
comment22.like()
comment33.like()
comment44.like()
comment11.like()
comment22.like()
comment33.like()
comment33.like()
comment33.like()
comment11.like()
comment44.like()
comment33.dislike()
comment11.like()
comment22.dislike()
comment44.dislike()
comment33.dislike()
article11.like()
article11.like()
article11.like()
article11.like()
article22.like()
article22.like()
article22.like()
article22.like()
article22.like()
article22.like()
article22.like()

author11.updateRating()
author22.updateRating()

Post.objects.all().values('author', 'post_title')
Post.objects.filter(author=author22)
Post.objects.filter(post_title='Заголовок статьи 1').values('author')
Comment.objects.filter(post_info=article11).values('comment_text')
Comment.objects.filter(comment_text='Текст комментария 2').values('comment_rating')
Author.objects.filter(user_id=1)
Author.objects.all().values('user', 'user_id')
Comment.objects.all().values('post_info', 'comment_user')