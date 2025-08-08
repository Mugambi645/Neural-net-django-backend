from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from rest_framework.permissions import AllowAny
from .serializers import UserSerializer
from django.contrib.auth.models import User

class RegisterView(generics.CreateAPIView):
    """Api view to register a new user"""
    queryset = User.objects.all()
    permission_classes = (AllowAny, )
    serializer_class = UserSerializer