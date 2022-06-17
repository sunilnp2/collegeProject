# from rest_framework import sera
from rest_framework import serializers
from .models import Review, Stud

class ReviewSerializers(serializers.Serializer):
    class Meta:
        model = Review
        fields = ['name', 'subject','review']
        
class StudSerializers(serializers.ModelSerializer):
    class Meta:
        model = Stud
        fields = ['name', 'age']
    
    # def create(self,validated_data):
    #     return Stud.objects.create(**validated_data)

