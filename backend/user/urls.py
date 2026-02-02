from django.urls import path
from .views import UserDetailView, UserRegisterView



urlpatterns = [
    path('info/', UserDetailView.as_view()),
    path('register/', UserRegisterView.as_view()),
]
