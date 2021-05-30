from rest_framework import fields, serializers
from .models import Article,Tag

class StudentSerializer(serializers.Serializer):
    name = serializers.CharField(max_length = 100)
    roll_no =  serializers.IntegerField()
    marks = serializers.IntegerField()

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag 
        fields = '__all__'

class ArticleSerializer(serializers.ModelSerializer):
    tags = TagSerializer(many=True,read_only = True)
    class Meta:
        model = Article 
        fields = '__all__'
