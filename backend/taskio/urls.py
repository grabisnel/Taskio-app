from django.urls import path
from taskio.views import TaskListCreateView, TaskRetrieveUpdateView

urlpatterns = [
    
    path('tasks/get-or-create', TaskListCreateView.as_view()),
    path('tasks/update/<int:pk>', TaskRetrieveUpdateView.as_view())
    
]