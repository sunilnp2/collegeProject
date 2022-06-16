# from rest_framework import sera
from rest_framework import serializers
from .models import Review

class StudentSerializers(serializers.Serializer):
    class Meta:
        model = Review
        fields = ['__all__']
