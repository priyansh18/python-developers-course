from django.urls import path
from . import views

# as_view convert class based views into function based view
urlpatterns = [
    path('',views.Index.as_view(),name='index')
]