from django.shortcuts import render
from django.contrib.auth.hashers import check_password
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import status
from rest_framework.response import Response
from rest_framework.generics import RetrieveUpdateDestroyAPIView
from rest_framework.decorators import api_view, action
from users.models import User
from users.serializers import UserSerializer

# 비밀번호 변경 시 보안장치 추가
# user 정보 받아오기(user_id -> request.user로 변경)

@api_view(['POST'])
def user_list_api_view(request):
    if request.method == 'POST':
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET', 'PATCH', 'DELETE'])
def user_retrieve_api_view(request, user_id):
    try:
        user = User.objects.get(pk=user_id)
    except User.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = UserSerializer(user)
        return Response(serializer.data)
    
    elif request.method == 'PATCH':
        serializer = UserSerializer(user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
@api_view(['POST'])
def jwt_api_view(request):
    username = request.data.get('username')
    password = request.data.get('password')

    print(username)

    user = User.objects.get(username=username)

    if not check_password(password, user.password):
        return Response(status=status.HTTP_401_UNAUTHORIZED)
    
    token = RefreshToken.for_user(user)
    serializer = UserSerializer(user)
    return Response(
        status=status.HTTP_200_OK,
        data = {
            'token': str(token.access_token), #token(객체->str)
            'user': serializer.data,
        }
    )

@api_view(['PATCH'])
def patch_password_api_view(request, user_id):
    try:
        user = User.objects.get(pk=user_id)
        new_pwd = request.data["password"]
    except User.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    user.set_password(new_pwd)
    user.save()
    return Response(status=status.HTTP_200_OK)

class UserAPIView(RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    lookup_field = 'pk'
    lookup_url_kwarg = 'user_id'