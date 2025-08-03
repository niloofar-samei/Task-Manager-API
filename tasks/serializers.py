from rest_framework import serializers
from .models import Task
from django.contrib.auth.models import User


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = "__all__"
        read_only_fields = ["owner", "created_at"]


class UserRegistrationSerializer(serializers.ModelSerializer):
    # This line protects the password by hiding it from being accidentally returned.
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ["username", "password"]

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validate_data["username"],
            password=validate_data["password"],
        )
        return user
