from django.http.request import HttpRequest
from django.http.response import HttpResponse
from django.shortcuts import render
from django.views import View

# Create your views here.
class Index(View):
    def get(request,self):
        return HttpResponse("GET Request")
    
    def post(request,self):
        return HttpResponse("POST Request") 