from django.utils import timezone
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from blog.models import Post


class PostListView(ListView):

    model = Post
    paginate_by = 100
    template_name = 'blog/post_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context


class PostDetailView(DetailView):

    model = Post
    template_name = 'blog/post_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context
