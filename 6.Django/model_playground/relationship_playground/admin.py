from django.contrib import admin
from .models import Author,Article,Pizza,Topping,Society,Membership,Person
# Register your models here.
admin.site.register([Article,Author,Pizza,Topping,Society,Membership,Person])
