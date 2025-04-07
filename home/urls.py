from django.urls import path
from .views import (
    EmployeeListCreateView, EmployeeDetailView,
    DepartmentListCreateView, DepartmentDetailView,
)

urlpatterns = [
    # Employee CRUD
    path('employees/', EmployeeListCreateView.as_view(), name='employee-list-create'),
    path('employees/<int:pk>/', EmployeeDetailView.as_view(), name='employee-detail'),

    # Department CRUD
    path('departments/', DepartmentListCreateView.as_view(), name='department-list-create'),
    path('departments/<int:pk>/', DepartmentDetailView.as_view(), name='department-detail'),
]
