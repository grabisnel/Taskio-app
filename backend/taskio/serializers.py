from rest_framework import serializers
from taskio.models import Task
from user.serializers import UserSerializer

class TasksSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    class Meta:
        model =  Task
        fields = '__all__'
    
    