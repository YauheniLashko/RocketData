from rest_framework import permissions
from rest_framework.permissions import BasePermission
from rest_framework_api_key.permissions import BaseHasAPIKey
from .models import EmployeeAPIKey


class HasEmployeeAPIKey(BaseHasAPIKey):
    model = EmployeeAPIKey


class Himself(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.employe == request.user

