from django.shortcuts import render
from rest_framework import generics
from taskio.serializers import TasksSerializers
from taskio.models import Task
# Create your views here.


class TaskListCreateView(generics.ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TasksSerializers
    lookup_field = Task.id

class TaskRetrieveUpdateView(generics.RetrieveUpdateAPIView):
    queryset = Task.objects.all()
    serializer_class = TasksSerializers
    
    