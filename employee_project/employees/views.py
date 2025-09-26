from rest_framework import viewsets, filters
from .models import Department, Employee, Attendance
from .serializers import DepartmentSerializer, EmployeeSerializer, AttendanceSerializer

class DepartmentViewSet(viewsets.ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer

class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()

    serializer_class = EmployeeSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['first_name', 'last_name', 'email', 'position', 'department__name']
    ordering_fields = ['date_joined', 'first_name']

class AttendanceViewSet(viewsets.ModelViewSet):
    queryset = Attendance.objects.all()
    serializer_class = AttendanceSerializer
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['date', 'employee__first_name']