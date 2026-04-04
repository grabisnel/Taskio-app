from django.contrib.auth import authenticate
from django.middleware.csrf import get_token
from django.conf import settings
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
            return Response({"detail": "Username and password required"}, 
                status=status.HTTP_400_BAD_REQUEST)

        user = authenticate(request, username=username, password=password)
        
        if user is None:
            return Response({"detail": "Invalid credentials"}, 
                status=status.HTTP_401_UNAUTHORIZED)        

        response = super().post(request)
        token = response.data.get("token")
        response = Response(
            {"detail": "Logged in successfully", "token": token},
            status=status.HTTP_200_OK,
        )

        response.set_cookie(
            key=settings.AUTH_TOKEN_COOKIE_NAME,
            value=token,
            httponly=True,
            secure=settings.AUTH_TOKEN_COOKIE_SECURE,
            samesite=settings.AUTH_TOKEN_COOKIE_SAMESITE,
            max_age=settings.AUTH_TOKEN_COOKIE_MAX_AGE,
            path='/',
        )

        get_token(request)

        return response


class LogoutView(APIView):
    permission_classes = [IsAuthenticated] 

    def post(self, request):
        if hasattr(request.user, "auth_token"):
            request.user.auth_token.delete()

        response = Response({"detail": "Logged out successfully."}, status=200)
        response.delete_cookie(
            settings.AUTH_TOKEN_COOKIE_NAME,
            path='/',
            samesite=settings.AUTH_TOKEN_COOKIE_SAMESITE,
        )

        return response
    
    
