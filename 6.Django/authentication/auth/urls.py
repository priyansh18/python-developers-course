from django.urls import path
from . import views

urlpatterns = [
    path('login',views.AuthLogin.as_view(),name = 'login'),
    path('logout',views.AuthLogout.as_view(),name = 'logout'),
    # path('login',views.auth_login,name = 'login')
]