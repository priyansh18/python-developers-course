from os import error
from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from .forms import LoginForm
from django.http import HttpResponse
from django.contrib.auth import authenticate,login
# Create your views here.
def auth_login(request):
    form = LoginForm()
    error = None
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username = username,password = password)
            if user:
                login(request,user)
                return HttpResponseRedirect('/')
            else:
                error = "Invalid Username or Password"
    context = {
        'form':form,
        'error':error
    }

    return render(request,'auth/login.html',context)