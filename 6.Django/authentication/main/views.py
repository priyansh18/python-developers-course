from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
# Create your views here.
def index(request):
    return render(request,'main/index.html',context={})

@login_required(login_url='/auth/login')
def secure(request):
    return  HttpResponse('This is Authenticated View')