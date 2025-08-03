from django.shortcuts import render
from rest_framework import generics
from .models import Task
from .serializers import TaskSerializer, UserRegistrationSerializer
from rest_framework.permissions import IsAuthenticated
from django.contrib.aut.models import User


class TaskListCreateView(generics.ListCreateAPIView):
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Task.objects.filter(owner=self.rquest.user)

    def preform_create(self, serializer):
        serializer.save(owner=self.request.user)


class UserRegistrationSerializer(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserRegistrationSerializer
