from django import forms


class CommentForm(forms.Form):
    text = forms.CharField(max_length=10000)


class PostForm(forms.Form):
    title = forms.CharField(max_length=30)
    text = forms.CharField(max_length=10000)
    image = forms.FileField(required=False)
