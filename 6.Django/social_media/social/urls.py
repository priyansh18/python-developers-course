from django.urls import path
from . import views

urlpatterns = [
    path('home/',views.Home.as_view(),name='home'),
    path('post/',views.AllPost.as_view(),name='post'),
    path('post/<int:pk>/like/',views.LikePost.as_view(),name='like_post'),
    path('post/<int:pk>/comment/',views.CommentPost.as_view(),name='comment_post'),
    path('',views.Wall.as_view(),name='wall'),
]