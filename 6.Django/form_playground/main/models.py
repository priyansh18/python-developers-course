from os import name
from django.db import models

# Create your models here.
class Student(models.Model):
    GENDERS = (
        ('M','Male'),
        ('F','Female'),
        ('U','Undisclosed')
    )
    name = models.CharField(max_length=255)
    roll_number= models.IntegerField( )
    gender = models.CharField(max_length=1,choices=GENDERS)

    def __str__(self):
        return self.name