from django.db import models

# Create your models here.

class Institute(models.Model):
    TYPES = (
        ('c','College'),
        ('h','High School'),
    )
    name = models.CharField(max_length=100)
    type_of_institute = models.CharField(max_length=1,choices=TYPES)

    def __str__(self):
        return self.name

class Student(models.Model):
    GENDERS = (
        ('m', 'Male'),
        ('f', 'Female'),
        ('u', 'Undisclosed'),
    )
    name = models.CharField(max_length=260)
    roll_no = models.IntegerField(unique=True)
    email = models.EmailField(max_length=100)
    gender = models.CharField(max_length=1, choices=GENDERS)
    percentage = models.FloatField()
    institute = models.ForeignKey('Institute',on_delete=models.CASCADE,blank=True,null=True)

    def __str__(self):
        return self.name

