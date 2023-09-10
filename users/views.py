from django.shortcuts import render

# Create your views here.
from django.views import View
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import User
from .serializer import UserSerializer

from django.http import JsonResponse

from django.shortcuts import render, redirect
from rest_framework import viewsets

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


# Create your views here.
class User(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class BulkUserUpload(APIView):
    def post(self, request, format=None):
        serializer = UserSerializer(data=request.data, many=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
