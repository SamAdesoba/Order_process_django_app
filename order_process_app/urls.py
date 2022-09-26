import routers as routers
from django.urls import path
from . import views


app_name = 'app_html'
routers = routers.DefaultRouter()
routers.register('employee', views.EmployeesViewSet)

urlpatterns = [
    path('employees-list/', views.EmployeesViewSet, name='employees-list'),
    path('employee-detail/<int:pk>/', views.EmployeesViewSet, name='employees-details'),
]
