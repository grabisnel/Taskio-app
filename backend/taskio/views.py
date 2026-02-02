from django.shortcuts import render
from rest_framework import generics
from rest_framework.authentication import BasicAuthentication, SessionAuthentication
from taskio.serializers import TasksSerializer
from taskio.models import Task
from rest_framework.permissions import IsAuthenticated
# Create your views here.

class TaskListCreateView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Task.objects.all()
    serializer_class = TasksSerializer
    lookup_field = Task.id



class TaskRetrieveUpdateView(generics.RetrieveUpdateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Task.objects.select_related('user')
    serializer_class = TasksSerializer
    
    
    