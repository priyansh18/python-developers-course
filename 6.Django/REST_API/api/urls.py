from django.urls import path
from . import views

urlpatterns = [
    path('users/',views.usersApi,name="userapi")
]