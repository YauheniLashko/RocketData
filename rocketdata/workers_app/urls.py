from rest_framework.routers import DefaultRouter
from .views import EmployeeViewSet, EmployeeLevelViewSet, EmployeeAPIView, HimselfView
from django.urls import path

router = DefaultRouter()
router.register("employees", EmployeeViewSet, basename="worker")
router.register("level", EmployeeLevelViewSet, basename="level")




urlpatterns = [
    path('himself/', HimselfView.as_view(), name='himself'),
    path('emp-api/', EmployeeAPIView.as_view(), name='employeesapi'),
]

urlpatterns += router.urls
