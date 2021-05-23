from django.db import models

# Create your models here.

# Every table in database is represented as a class.
# Every row in database is created by an object of this class.


class Student(models.Model):
    GENDERS = (
        ('f', 'Female'),
        ('m', 'Male'),
        ('u', 'Undisclosed')
    )
    name = models.CharField(max_length=100)
    roll_number = models.IntegerField(unique=True)
    address = models.TextField(null=True)
    # Can be null in database
    # Cannot be null in ORM
    phone_number = models.CharField(max_length=15,null=True,blank=True)
    email = models.EmailField(null=True)
    gender = models.CharField(max_length=1,choices=GENDERS,null=True)

    def __str__(self):
        return self.name