from django.urls import path
from .views import (
    TaskListCreateView,
    UserRegistrationView,
    TaskRetriveUpdateDestroyView,
)

urlpatterns = [
    path("tasks/", TaskListCreateView.as_view(), name="task-list-create"),
    path("tasks/<int:pk>/", TaskRetriveUpdateDestroyView.as_view(), name="task-detail"),
    path("register/", UserRegistrationView.as_view(), name="user-register"),
]
