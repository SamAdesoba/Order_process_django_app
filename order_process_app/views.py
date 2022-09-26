from rest_framework import viewsets
from . import serializer

from order_process_app import models


class EmployeesViewSet(viewsets.ModelViewSet):
    queryset = models.Employees.objects.all()
    serializer_class = serializer.EmployeesSerializer
