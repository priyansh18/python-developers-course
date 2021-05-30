from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.decorators import api_view

# Create your views here.
# Using of api_view decorators convert list or object into type-JSON
@api_view()
def usersApi(request):
    # Can also be get through database
    users = [
        {
            'name':'Priyansh Singhal',
            'language' : 'Python'
        },
        {
            'name':'Shaurya Singhal',
            'language' : 'C++'
        }
    ]

    return Response(users)