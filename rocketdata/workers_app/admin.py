from django.contrib import admin
from .models import Employee


def delete_salary(modeladmin, request, queryset):
    queryset.update(salary_paid=0)
    delete_salary.short_description = "Удалить информацию о выплаченной заработной плате"

class ListEmployes(admin.ModelAdmin):
    list_display =["full_name", "position", "chief", "salary", "salary_paid"]
    list_filter = ["position", "level"]
    actions = [delete_salary]




admin.site.register(Employee, ListEmployes)