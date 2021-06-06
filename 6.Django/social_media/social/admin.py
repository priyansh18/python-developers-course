from django.contrib import admin
from . import models
# Register your models here.
admin.site.register([models.Post,models.Friends,models.Like,models.Comment])