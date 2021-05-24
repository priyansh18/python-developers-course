from django.core import validators
from django.db import models
from .validators import validate_even_number
# Default validation can only occurs on ORM level not on Database level.So Django have its own validators
from django.core.validators import(
    EmailValidator, MaxValueValidator, MinValueValidator, MinLengthValidator, URLValidator, validate_slug)
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
    phone_number = models.CharField(max_length=15, null=True, blank=True)
    email = models.CharField(max_length=100, null=True, validators=[
                             EmailValidator(message='Email address is not valid')])
    age = models.IntegerField(null=True, validators=[
                              MaxValueValidator(150), MinValueValidator(0),
                              validate_even_number])
    gender = models.CharField(max_length=1, choices=GENDERS, null=True)

    slug = models.CharField(max_length=100, validators=[
                            validate_slug], null=True)

    def __str__(self):
        return self.name
