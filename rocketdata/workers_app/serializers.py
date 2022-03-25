from rest_framework import serializers
from .models import Employee

class EmployeeSerializer(serializers.Serializer):
    full_name = serializers.CharField(max_length=100)
    position = serializers.CharField(max_length=50)
    date_of_employment = serializers.DateField()
    salary = serializers.DecimalField(max_digits=10, decimal_places=2)
    salary_paid = serializers.DecimalField(max_digits=10, decimal_places=2)
    level = serializers.CharField(max_length=1)

    class Meta:
        model = Employee
        fields = '__all__'