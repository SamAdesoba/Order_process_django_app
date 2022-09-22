from order_process_app.viewset import EmployeesViewSet
from rest_framework import routers

routers = routers.DefaultRouter()
routers.register('employee', EmployeesViewSet)
