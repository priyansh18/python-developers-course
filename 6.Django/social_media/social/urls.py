from django.urls import path
from . import views

urlpatterns = [
    path('',views.Wall.as_view(),name='wall'),
]