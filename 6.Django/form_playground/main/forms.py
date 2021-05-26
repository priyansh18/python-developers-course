from django import forms
from django.db.models import fields
from django.forms import widgets
from .models import Student

class ExampleForm(forms.Form):
    name = forms.CharField(max_length=50)
    about_me = forms.CharField()
    active = forms.BooleanField()


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = "__all__"

