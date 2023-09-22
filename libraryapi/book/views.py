from django.shortcuts import render
from book.models import Book
from django.contrib.auth.models import User
from book.serializers import BookSerializer,UserSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated,AllowAny
from rest_framework import status
from rest_framework.views import APIView
from django.http import Http404
from rest_framework import mixins,generics,viewsets

class UserViewset(viewsets.ModelViewSet):
    permission_classes=[AllowAny,]
    queryset=User.objects.all()
    serializer_class=UserSerializer

class BookViewset(viewsets.ModelViewSet):
    queryset=Book.objects.all()
    serializer_class=BookSerializer

