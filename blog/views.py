from django.views.generic import ListView, DetailView
from django.utils import timezone
from .models import Post


class FeedView(ListView):
    template_name = 'blog/feed.html'

    def get_queryset(self):
        "Return the last ten published posts"
        return Post.objects.filter(
            publication_date__lte=timezone.now()
        ).order_by('-publication_date')[:5]


class PostView(DetailView):
    model = Post
    template_name = 'blog/post.html'
