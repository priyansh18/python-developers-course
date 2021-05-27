from django.urls import path
from . import views

# as_view convert class based views into function based view
urlpatterns = [
    path('',views.Index.as_view(),name='index'),
    path('college/<int:pk>',views.CollegeDetail.as_view(),name='college_detail'),
    path('college',views.CollegeList.as_view(),name='college_list'),
    path('create_college',views.CollegeCreate.as_view(),name='create_college'),
    path('update_college/<int:pk>',views.CollegeUpdate.as_view(),name='update_college'),
    path('delete_college/<int:pk>',views.CollegeDelete.as_view(),name='delete_college'),
    path('create_student',views.StudentCreate.as_view(),name='create_student'),
]