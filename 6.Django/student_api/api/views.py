from rest_framework.response import Response
from . import models,serializers
from rest_framework.generics import (ListAPIView, RetrieveAPIView, UpdateAPIView,
                                     RetrieveUpdateAPIView, CreateAPIView, ListCreateAPIView, DestroyAPIView)
# Create your views here.

# class StudentListView(ListAPIView):
#     queryset = models.Student.objects.all()
#     serializer_class = serializers.StudentSerializer

# Instead of using ListAPIView we use ListCreateAPIView If Get request is sent it shows data and if post request is sent then create data
class StudentListView(ListCreateAPIView):
    queryset = models.Student.objects.all()
    serializer_class = serializers.StudentSerializer

# Instead of using RetrieveAPIView we use RetrieveUpdateAPIView  If Get request is sent it shows data and if patch request is sent with updated data it changes the data of particular id 
class StudentDetailView(RetrieveUpdateAPIView):
    queryset = models.Student.objects.all()
    serializer_class = serializers.StudentSerializer

class StudentDeleteView(DestroyAPIView):
    queryset = models.Student.objects.all()
    serializer_class = serializers.StudentSerializer
