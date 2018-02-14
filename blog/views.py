from django.views.generic import ListView, DetailView
from django.utils import timezone
from .models import Post, Comment


class FeedView(ListView):
    template_name = 'blog/feed.html'

    def get_queryset(self):
        "Return the last ten published posts"
        return Post.objects.filter(
            publication_date__lte=timezone.now()
        ).order_by('-publication_date')[:5]


class PostView(DetailView):
    queryset = Post.objects.all()
    # model = Post
    template_name = 'blog/post.html'

    def get_context_data(self, *args, **kwargs):
        context = super(PostView, self).get_context_data(*args, **kwargs)
        context['comments_list'] = Comment.objects.all()
        return context
