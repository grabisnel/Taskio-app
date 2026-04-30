from rest_framework import serializers
from taskio.models import Task
from user.serializers import UserSerializer

class TasksSerializer(serializers.ModelSerializer):
    owner = UserSerializer(read_only=True)

    class Meta:
        model =  Task
        fields = '__all__'
        read_only_fields = ['owner']
    
    