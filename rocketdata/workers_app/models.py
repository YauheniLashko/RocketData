from django.db import models
from rest_framework_api_key.models import AbstractAPIKey


class Employee(models.Model):
    choice_lvl = [("0", "0"), ("1", "1"), ("2", "2"), ("3", "3"), ("4", "4")]

    full_name = models.CharField(max_length=100, verbose_name='ФИО')
    position = models.CharField(max_length=50, verbose_name="Должность")
    date_of_employment = models.DateField(verbose_name="Дата приема на работу")
    salary = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Размер заработной платы")
    salary_paid = models.DecimalField(max_digits=10, null=True, decimal_places=2,
                                      verbose_name="Информация о выплаченной зарплате")
    chief = models.ForeignKey("self", null=True, blank=True, on_delete=models.SET_NULL, verbose_name="Начальник")
    level = models.CharField(max_length=1, choices=choice_lvl, default="4", verbose_name="Уровень иерархии")

    def __str__(self):
        return self.full_name

class EmployeeAPIKey(AbstractAPIKey):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name="api_keys")