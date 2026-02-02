from django.contrib.auth import authenticate, logout, password_validation
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.permissions import AllowAny
from rest_framework import status 
from django.contrib.auth.models import User
from rest_framework.authtoken.views import ObtainAuthToken



class LoginView(ObtainAuthToken):
    permission_classes = [AllowAny]

    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")
        
        if not username or not password:
            return Response({"detail": "Username and password required"}, status=status.HTTP_400_BAD_REQUEST)

        user = authenticate(request, username=username, password=password)
        print(user)
        if user is None:
            return Response({"detail": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)        

        response = super().post(request)
        
        print(response.data)
        
        return Response({"detail": "Logged in successfully", "token": response.data.get("token")}, status=status.HTTP_200_OK)


class LogoutView(APIView):
    permission_classes = [IsAuthenticated] 

    def post(self, request):
        
        request.user.auth_token.delete()
        
        return Response({"detail": "Logged out successfully."}, status=200)
    
    
class UserDetailView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        user_data = {
            "username": user.username,
            "email": user.email,
            "first_name": user.first_name,
            "last_name": user.last_name,
        }
        return Response(user_data, status=status.HTTP_200_OK)
    
    
class UserRegisterView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")
        email = request.data.get("email")
        first_name = request.data.get("first_name")
        last_name = request.data.get("last_name")

        if not username or not password or not email:
            return Response({"detail": "Username, password, and email are required."}, status=status.HTTP_400_BAD_REQUEST)

        if not first_name or not last_name:
            return Response({"detail": "First name and last name are required."}, status=status.HTTP_400_BAD_REQUEST)

        if User.objects.filter(username=username).exists():
            return Response({"detail": "Username already taken."}, status=status.HTTP_400_BAD_REQUEST)
        
        try:
            password_validation.validate_password(password)
            
        except password_validation.ValidationError as e:
            return Response({"detail": e.messages}, status=status.HTTP_400_BAD_REQUEST)

        user = User.objects.create_user(username=username, password=password, email=email, first_name=first_name, last_name=last_name)
        user.save()

        return Response({"detail": "User registered successfully."}, status=status.HTTP_201_CREATED)