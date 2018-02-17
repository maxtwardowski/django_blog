from django.views.generic import ListView, DetailView
from django.utils import timezone
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect
from .models import Post, Comment
from .forms import CommentForm


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


class NewPostView(DetailView):
    queryset = Post.objects.all()
    template_name = 'blog/newpost.html'
