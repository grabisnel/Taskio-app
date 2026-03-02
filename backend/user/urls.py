from django.urls import path
from .views import UserDetailView, UserRegisterView, UserProfileUpdateView



urlpatterns = [
    path('info/', UserDetailView.as_view()),
    path('register/', UserRegisterView.as_view()),
    path('profile/', UserProfileUpdateView.as_view()),
]
