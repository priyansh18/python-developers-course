from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Article
from .serializers import StudentSerializer,ArticleSerializer

# Create your views here.
# Using of api_view decorators convert list or object into type-JSON
class Student:
    def __init__(self,name,roll_no,marks):
        self.name = name
        self.roll_no = roll_no
        self.marks = marks


# Decorator for converting view into API view
@api_view()
def articleApi(request):
    articles = Article.objects.all()
    response = ArticleSerializer(articles,many=True)
    return Response(response.data)

@api_view()
def usersApi(request):
    # Can also be get through database
    student1 = Student("Priyansh",1,100)
    student2 = Student("Shaurya",2,90)
    student3 = Student("Aman",3,96)
    response = StudentSerializer([student1,student2,student3],many = True)

    return Response(response.data)