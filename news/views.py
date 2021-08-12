from django.views.generic import ListView
from django.views.generic import DetailView
from django.views.generic import CreateView
from django.views.generic import UpdateView
from django.views.generic import DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin


from .models import Post
from .filters import NewsFilter
from .forms import NewsForm


class NewsList(ListView):
    model = Post
    template_name = 'article_list.html'
    context_object_name = 'news'
    ordering = ['-id']
    paginate_by = 1

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filters'] = NewsFilter(self.request.GET, queryset=self.get_queryset())
        return context


class NewsDetail(DetailView):
    model = Post
    template_name = 'article.html'
    context_object_name = 'article'


class NewsCreateView(LoginRequiredMixin, CreateView):
    template_name = 'templates/article_create.html'
    form_class = NewsForm
    success_url = '/search/'


class NewsUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'article_create.html'
    form_class = NewsForm
    success_url = '/search/'

    def get_object(self, **kwargs):
        id = self.kwargs.get('pk')
        return Post.objects.get(pk=id)


class NewsDeleteView(LoginRequiredMixin, DeleteView):
    template_name = 'article_delete.html'
    model = Post
    context_object_name = 'post'
    success_url = '/search/'

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['post'] = Post.objects.all()
    #
    #     return context