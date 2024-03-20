from rest_framework.serializers import ModelSerializer, ValidationError, DateTimeField
from .models import Task
from django.utils import timezone

class TaskReadSerializer(ModelSerializer):
    deadline = DateTimeField(format='%d/%m/%Y', required=False, allow_null=True)
    class Meta:
        model = Task
        exclude = ("created_at", "modified_at")


class TaskWriteSerializer(ModelSerializer):
    class Meta:
        model = Task
        fields = "__all__"

    def validate_name(self, name):
        if any(char.isdigit() for char in name):
            raise ValidationError("Name can't be a number")
        return name
    
    def validate_deadline(self, deadline):
        if deadline <= timezone.now():
            raise ValidationError("You can't have a deadline in the past")
        return deadline