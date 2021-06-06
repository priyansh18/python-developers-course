from django.shortcuts import render
from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Post
from django.db.models import Q
# Create your views here.
class Wall(LoginRequiredMixin,ListView):
    context_object_name = 'posts'
    template_name = 'social/wall.html'
    login_url = 'auth/login'

    def get_queryset(self):
        return Post.objects.filter(
            # search if either person1 is friend of current user or person2 is.and filter post by friend and remove own posts 
            (Q(user__person1 = self.request.user.pk) | Q(user__person2 = self.request.user.pk))& ~Q(user = self.request.user)
        )

class Home(LoginRequiredMixin,ListView):
    context_object_name = 'posts'
    template_name = 'social/home.html'
    login_url = 'auth/login'

    def get_queryset(self):
        return Post.objects.filter(
            Q(user = self.request.user)
        )