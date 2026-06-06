from rest_framework import serializers
from . import models

class DepartmentsSerializer(serializers.ModelSerializer):
    class Meta:
        models = models.Departments
        fields = ["id", "name"]

class RolesSerializer(serializers.ModelSerializer):
    class Meta:
        models = models.Roles
        fields = ["id", "role"]

class CustomUserSerializer(serializers.ModelSerializer):
    