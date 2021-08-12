from django.urls import path
from .views import NewsList, NewsDetail, NewsCreateView, NewsUpdateView, NewsDeleteView
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    # path('', NewsList.as_view()),
    path('<int:pk>', NewsDetail.as_view(), name='article'),
    path('login/',
         LoginView.as_view(template_name='login.html'),
         name='login'),
    path('search/', NewsList.as_view(), name='article_list'),
    path('create/', NewsCreateView.as_view(), name='article_create'),
    path('create/<int:pk>', NewsUpdateView.as_view(), name='article_update'),
    path('delete/<int:pk>', NewsDeleteView.as_view(), name='article_delete'),
]