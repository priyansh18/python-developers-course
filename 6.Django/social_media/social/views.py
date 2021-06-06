from django.forms import fields
from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from django.views.generic import ListView
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Like, Post
from django.db.models import Q
from .forms import CreatePostForm,PostCommentForm
# Create your views here.


class Wall(LoginRequiredMixin, ListView):
    context_object_name = 'posts'
    template_name = 'social/wall.html'
    login_url = 'auth/login'
    

    def get_queryset(self):
        return Post.objects.filter(
            # search if either person1 is friend of current user or person2 is.and filter post by friend and remove own posts
            (Q(user__person1=self.request.user.pk) | Q(
                user__person2=self.request.user.pk)) & ~Q(user=self.request.user)
        ).order_by('-created_at')


class Home(LoginRequiredMixin, ListView):
    context_object_name = 'posts'
    template_name = 'social/home.html'
    login_url = 'auth/login'

    def get_queryset(self):
        return Post.objects.filter(Q(user=self.request.user)).order_by('-created_at')

    def get_context_data(self, *args, **kwargs):
        # It uses parent class as context data
        data = super().get_context_data(*args, **kwargs)
        # Passing posts data with addition to post_form
        data['post_form'] = CreatePostForm()
        return data


class AllPost(View):
    def post(self, request):
        form = CreatePostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            return redirect('/home/')


class LikePost(View):
    model = Post
    def post(self, request, pk):
        post = self.model.objects.get(pk=pk)
        Like.objects.create(post=post, user=request.user)
        return HttpResponse(code=204)

class CommentPost(View):
    model = Post
    form = PostCommentForm

    def post(self, request, pk):
        post = self.model.objects.get(pk=pk)
        form = self.form(request.POST)

        if form.is_valid():
            comment =form.save(commit=False)
            comment.post = post
            comment.user = request.user
            comment.save()
            return HttpResponse(code=204)
        return HttpResponse(code=400)


