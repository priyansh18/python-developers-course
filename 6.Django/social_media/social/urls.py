from django.urls import path
from . import views

urlpatterns = [
    path('home/',views.Home.as_view(),name='home'),
    path('post/',views.AllPost.as_view(),name='post'),
    path('',views.Wall.as_view(),name='wall'),
]