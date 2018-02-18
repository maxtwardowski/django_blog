from django.views.generic import ListView, DetailView
from django.utils import timezone
from django.http import HttpResponseRedirect, HttpResponse
from .models import Post, Comment
from .forms import CommentForm, PostForm
from django.template import loader


class FeedView(ListView):
    template_name = 'blog/feed.html'

    def get_queryset(self):
        "Return the last ten published posts"
        return Post.objects.filter(
            date__lte=timezone.now()
        ).order_by('-date')[:5]


class PostView(DetailView):
    queryset = Post.objects.all()
    # model = Post
    template_name = 'blog/post.html'


def AddComment(request, pk):
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            newcomment = Comment()
            newcomment.post = Post.objects.get(pk=pk)
            newcomment.author = form.cleaned_data['author']
            newcomment.text = form.cleaned_data['text']
            newcomment.date = timezone.now()
            newcomment.save()
            return HttpResponseRedirect('/' + str(pk))
    else:
        form = CommentForm()

    return HttpResponseRedirect('/' + str(pk))


def AddPostView(request):
    template = loader.get_template("blog/newpost.html")
    return HttpResponse(template.render())


def AddPost(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            newpost = Post()
            newpost.title = form.cleaned_data['title']
            newpost.text = form.cleaned_data['text']
            newpost.date = timezone.now()
            newpost.save()
            return HttpResponseRedirect('/')
    else:
        form = PostForm()

    return HttpResponseRedirect('/')
