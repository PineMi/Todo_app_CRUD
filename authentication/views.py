from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .serializer import RegisterSerializer
from rest_framework.authtoken.models import Token
from .models import User
from django.contrib.auth import authenticate


@api_view(["POST"])
def register(request):
    serializer = RegisterSerializer(data=request.data)
    if serializer.is_valid():
        user = serializer.save()
        token = Token.objects.create(user=user)
        return Response({"token": token.key}, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["POST"])
def login(request):
    user = authenticate(username=request.data.get("username"), password=request.data.get("password"))
    if user:
        token, _ = Token.objects.get_or_create(user=user)
        return Response({"token": token.key}, status=status.HTTP_202_ACCEPTED)
    return Response({"Error message": "Invalid credentials."}, status=status.HTTP_400_BAD_REQUEST)
