from django.shortcuts import render
from django.views.generic import ListView,DetailView
from .models import Question,Choice

# Create your views here.


class Index(ListView):
    model = Question
    template_name = 'main/index.html'
    # Default context object name is smallm model name _ list i.e. question_list 
    
class Question(DetailView):
    model = Question
    template_name = 'main/question.html'