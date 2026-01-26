from django.contrib import admin
from django.urls import path
from auth.views import LoginView, LogoutView, UserDetailView, UserRegisterView

urlpatterns = [
    path('login/', LoginView.as_view(), name="login"),
    path('logout/', LogoutView.as_view(), name="logout"),
    path('me/', UserDetailView.as_view(), name="user-detail"),
    path('register/', UserRegisterView.as_view(), name="user-register"),
]