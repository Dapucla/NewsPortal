from django_filters import FilterSet
from django.forms import ModelForm
from .models import Post


class NewsFilter(FilterSet):
    class Meta:
        model = Post
        fields = ['name', 'post_type', 'author']