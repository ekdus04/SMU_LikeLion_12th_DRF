from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from hashtags.models import Hashtag
from hashtags.serializers import HashtagSerializer

@api_view(['POST'])
def hashtag_list_api_view(request):
    if request.method == 'POST':
        serializer = HashtagSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET', 'DELETE'])
def hashtag_retrieve_api_view(request, hashtags_id):
    try:
        hashtag = Hashtag.objects.get(pk=hashtags_id)
    except Hashtag.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = HashtagSerializer(hashtag)
        return Response(serializer.data)