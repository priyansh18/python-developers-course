from django.urls import path
from . import views

urlpatterns = [
    # path('users/',views.usersApi,name="userapi"),
    path('articles/',views.ArticleListView.as_view(),name="articleapi"),
    path('articles/<int:pk>',views.ArticleDetailView.as_view(),name="articledetailapi"),
    # path('create-article/',views.createArticleApi,name="create_articleapi"),
]