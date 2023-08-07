from rest_framework import serializers
from .models import Shelter

# serializer.py
class userSerializer(serializers.ModelSerializer):
    class Meta:
        model=Shelter
        fields='__all__'
        # ("id","name","tel")