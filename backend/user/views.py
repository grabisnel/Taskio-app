from django.contrib.auth.models import User
from django.contrib.auth import get_user_model, password_validation
from django.db import IntegrityError
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework import status
from user.serializers import UserSerializer, UserProfileUpdateSerializer
from rest_framework.exceptions import ValidationError

User = get_user_model()

class UserDetailView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        serializer = UserSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    
class UserRegisterView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):

        serializer = UserSerializer(data=request.data)

        try:
            username = request.data.get("username")
            password = request.data.get("password")
            email = request.data.get("email")
            first_name = request.data.get("first_name")
            last_name = request.data.get("last_name")

            if not username or not password or not email:
                return Response({"detail": "Username, password, and email are required."}, status=status.HTTP_400_BAD_REQUEST)

            if not first_name or not last_name:
                return Response({"detail": "First name and last name are required."}, status=status.HTTP_400_BAD_REQUEST)

            try:
                password_validation.validate_password(password)

            except password_validation.ValidationError as e:
                return Response({"detail": e.messages}, status=status.HTTP_400_BAD_REQUEST)

            try:
                serializer.is_valid(raise_exception=True)

                try:
                    User.objects.create_user(
                        username=username,
                        password=password,
                        email=email,
                        first_name=first_name,
                        last_name=last_name,
                    )


                except IntegrityError as exc:
                    return Response(
                        {"detail": "A user with this username or email already exists."},
                        status=status.HTTP_400_BAD_REQUEST,
                    )
            
            except ValidationError as exc:
                return Response(
                    {"detail": exc.detail},
                    status=status.HTTP_400_BAD_REQUEST,
                )
            
            return Response({"detail": "User registered successfully."}, status=status.HTTP_201_CREATED)
        
        except Exception as e:
            return Response(
                {"detail": "An unexpected error occurred during registration."},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )


class UserProfileUpdateView(APIView):
    permission_classes = [IsAuthenticated]

    def patch(self, request):
        if 'email' in request.data:
            return Response(
                {"detail": "Email cannot be updated from this endpoint."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        user = request.user
        serializer = UserProfileUpdateSerializer(user, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)