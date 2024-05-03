from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from likes.models import Like
from likes.serializers import LikeSerializer

@api_view(['POST'])
def like_list_api_view(request):
    if request.method == 'POST':
        serializer = LikeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET', 'DELETE'])
def like_retrieve_api_view(request, users_id):
    try:
        like = Like.objects.get(pk=users_id)
    except Like.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = LikeSerializer(like)
        return Response(serializer.data)

    elif request.method == 'DELETE':
        like.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)