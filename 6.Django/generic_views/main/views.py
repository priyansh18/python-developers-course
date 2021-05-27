from django.http.request import HttpRequest
from django.http.response import HttpResponse
from django.shortcuts import render
from django.views import View
from django.views.generic import (DetailView,ListView,CreateView,UpdateView,DeleteView)
from .models import Student,College

# Create your views here.
class Index(View):
    def get(request,self):
        return HttpResponse("GET Request")
    
    def post(request,self):
        return HttpResponse("POST Request") 

# Detail View
class CollegeDetail(DetailView):
    model = College
    template_name = 'main/college_detail.html'

# List View
class CollegeList(ListView):
    model = College
    template_name = 'main/college_list.html'
    # Instead of Object we can change its name to anything we want
    context_object_name = 'colleges'

# Create View

class CollegeCreate(CreateView):
    model = College
    template_name = 'main/college_create.html'
    fields = "__all__"
    success_url = '/college'

class StudentCreate(CreateView):
    model = Student
    template_name = 'main/student_create.html'
    fields = "__all__"
    success_url = '/college'

# Update View

class CollegeUpdate(UpdateView):
    model = College
    template_name = 'main/college_create.html'
    fields = "__all__"
    success_url = '/college'

class CollegeDelete(DeleteView):
    model = College
    template_name = 'main/confirm.html'
    fields = "__all__"
    success_url = '/college'



# Delete View