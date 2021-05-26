from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('students', views.student, name='student'),
    path('addstudent', views.addStudent, name='addstudent'),
]
