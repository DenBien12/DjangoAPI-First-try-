from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .models import Data
from .serializers import DataSerializer
# Create your views here.

@api_view(['GET'])
def getData(request):
    app=Data.objects.all()
    serializer = DataSerializer(app, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['POST'])
def postData(request):
    data={
        'name': request.data.get('name'),
        'description': request.data.get('description')
    }
    serializer = DataSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


