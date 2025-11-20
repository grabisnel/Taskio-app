from rest_framework import serializers
from taskio.models import Task


class TasksSerializers(serializers.ModelSerializer):
    class Meta:
        model =  Task
        fields = '__all__'
    
    