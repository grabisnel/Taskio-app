from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from taskio.serializers import TasksSerializer
from taskio.models import Task
# Create your views here.

class TaskListCreateView(generics.ListCreateAPIView):
    serializer_class = TasksSerializer
    permission_classes = [IsAuthenticated]
    lookup_field = 'id'

    def get_queryset(self):
        return Task.objects.filter(owner=self.request.user)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class TaskRetrieveUpdateView(generics.RetrieveUpdateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = TasksSerializer

    def get_queryset(self):
        return Task.objects.select_related('owner').filter(owner=self.request.user)
    
    
    