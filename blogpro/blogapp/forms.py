from django import forms
from django.contrib.auth.models import User
from blogapp.models import NewPost, Comment


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta():
        model = User
        fields = ('username', 'email', 'password')


class NewPostForm(forms.ModelForm):
    class Meta:
        model = NewPost
        fields = ('Author', 'Title', 'Text')


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('author', 'text',)
