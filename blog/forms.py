from django import forms
from .models import Post, Comment


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('author', 'text',)
    # comment_author = forms.CharField(max_length=100)
    # comment_text = forms.CharField(max_length=10000)


class PostForm(forms.Form):
    post_title = forms.CharField(max_length=30)
    post_text = forms.CharField(max_length=10000)
