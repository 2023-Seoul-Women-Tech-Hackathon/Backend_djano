from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .serializers import userSerializer
from .models import Shelter

@api_view(['GET'])
def getShelter(request):
    queryset = Shelter.objects.all()
    serializer = userSerializer(queryset,many=True)
    return Response(serializer.data)

# Create your views here.
