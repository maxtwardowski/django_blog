from django import forms


class CommentForm(forms.Form):
    # author = forms.CharField(max_length=30)
    text = forms.CharField(max_length=10000)


class PostForm(forms.Form):
    title = forms.CharField(max_length=30)
    text = forms.CharField(max_length=10000)


'''
class LoginForm(forms.Form):
    username = forms.CharField(max_length=30)
    password = forms.CharField(widget=forms.PasswordInput)
'''
