from django.forms import ModelForm
from .models import Post


class NewsForm(ModelForm):
    class Meta:
        model = Post
        fields = ['name', 'post_type', 'post_title', 'post_text', 'post_category', 'author']