import django_filters.rest_framework
from django.shortcuts import get_object_or_404
from rest_framework import viewsets, generics, filters
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework_api_key.permissions import HasAPIKey
from rest_framework.views import APIView
from rest_framework_api_key.models import APIKey
from .serializers import EmployeeSerializer


from .models import Employee, EmployeeAPIKey
from .serializers import EmployeeSerializer
from .permissions import HasEmployeeAPIKey, Himself


class EmployeeViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer



class EmployeeLevelViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.filter(level='4')
    serializer_class = EmployeeSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class EmployeeAPIView(generics.RetrieveAPIView):
    permission_classes = [HasEmployeeAPIKey]

    def get(self, request, *args, **kwargs):
        """Retrieve a project based on the request API key."""
        key = request.META["HTTP_AUTHORIZATION"].split()[1]
        api_key = EmployeeAPIKey.objects.get_from_key(key)
        employee = EmployeeAPIKey.objects.get(key=api_key.employee_id)
        serializer = EmployeeSerializer(employee, many=True)
        return Response(serializer.data)


class HimselfView(generics.RetrieveAPIView):
    serializer_class = EmployeeSerializer
    permission_classes = (Himself, )
    queryset = Employee.objects.all()
    def get_object(self):
        queryset = self.filter_queryset(self.get_queryset())
        obj = queryset.get(id=1)
        self.check_object_permissions(self.request, obj)
        return obj
