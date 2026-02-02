from django.contrib.auth import authenticate
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.permissions import AllowAny
from rest_framework import status 
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
    
    
