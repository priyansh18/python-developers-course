from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from . import forms, models

# Create your views here.


def index(request):
    context = {
        'forms': forms.ExampleForm
    }
    return render(request, 'main/index.html', context)


def student(request):
    students = models.Student.objects.all()
    context = {
        'students': students
    }
    return render(request, 'main/students.html', context)


def addStudent(request):

    studentForm = forms.StudentForm()
    if request.method == "POST":
        studentForm = forms.StudentForm(request.POST)
        if studentForm.is_valid():
            studentForm.save()
            return HttpResponseRedirect('/')

    context = {
        "student_form": studentForm
    }
    return render(request, 'main/addstudents.html', context)
