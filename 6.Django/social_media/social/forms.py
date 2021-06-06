from django import forms
from django.forms import fields
from .models import Post,Comment

class CreatePostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['content','image']

class PostCommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']