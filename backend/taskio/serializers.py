from rest_framework import serializers
from taskio.models import Task
from user.serializers import UserSerializer


class TaskSerializer(serializers.ModelSerializer):
    owner = UserSerializer(read_only=True)

    class Meta:
        model = Task
        fields = ['id', 'title', 'description', 'status', 'created_at', 'updated_at', 'owner']
        read_only_fields = ['id', 'created_at', 'updated_at']

    def validate_status(self, value):
        valid_choices = [choice[0] for choice in Task.Status.choices]
        if value not in valid_choices:
            raise serializers.ValidationError(
                f"Invalid status. Must be one of: {', '.join(valid_choices)}."
            )
        return value
    