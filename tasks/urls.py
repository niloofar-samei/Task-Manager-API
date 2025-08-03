from django.urls import path
from .views import TaskListCreateView, UserRegistrationView

urlpatterns = [
    path("tasks/", TaskListCreateView.as_view(), name="task-list-create"),
    path("register/", UserRegistrationView.as_view(), name="user-register"),
]
