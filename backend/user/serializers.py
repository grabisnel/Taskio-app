from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):

    email = serializers.EmailField(required=True)

    class Meta:
        model =  User
        exclude = ['password']
        read_only_fields = ['id']


class UserProfileUpdateSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name', 'username', 'email']
        read_only_fields = ['id', 'email']
    