from django.shortcuts import render
from django.views.generic import ListView
from .models import Post
# Create your views here.
class Wall(ListView):
    queryset = Post.objects.all()
    context_object_name = 'posts'
    template_name = 'social/wall.html'

