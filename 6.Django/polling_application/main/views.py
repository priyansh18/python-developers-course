from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import ListView,DetailView,FormView
from .models import Answer, Question,Choice
from django.views.generic.detail import SingleObjectMixin
from .forms import AnswerForm

# Create your views here.

class Index(ListView):
    model = Question
    template_name = 'main/index.html'
    # Default context object name is smallm model name _ list i.e. question_list 
    
class Question(FormView,SingleObjectMixin):
    model = Question
    template_name = 'main/question.html'
    form_class = AnswerForm

    def form_valid(self, form):
        # Save in memory but not commit in database
        obj = form.save(commit = False)
        # Adding particular field in memory
        obj.question = self.get_object()
        obj.user = self.request.user
        # Commit in database
        obj.save()
        return HttpResponseRedirect('/')

    # Overriding Context data
    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        try:
            data['answer'] = Answer.objects.get(
                question = self.get_object(),
                user = self.request.user
            )
        except:
            data['answer'] = None
        return data


    def post(self, request, *args, **kwargs):
        self.object =self.get_object()
        return super().post(self,request,*args,**kwargs)
    
    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        context = self.get_context_data(object = self.object)
        return self.render_to_response(context)