from django.db.models import fields
from rest_framework import serializers
from .models import Student,Institute

class InstituteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Institute
        fields = '__all__'

class StudentSerializer(serializers.ModelSerializer):
    institute = InstituteSerializer(read_only=True)
    class Meta:
        model = Student
        fields = '__all__'
