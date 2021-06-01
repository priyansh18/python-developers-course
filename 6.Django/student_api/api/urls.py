from django.urls import path
from . import views

urlpatterns = [
    path('students/',views.StudentListView.as_view(),name='students_list'),
    path('student/<int:pk>',views.StudentDetailView.as_view(),name='student'),
    path('deletestudent/<int:pk>',views.StudentDeleteView.as_view(),name='student_delete'),
]