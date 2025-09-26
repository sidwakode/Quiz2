import random
from faker import Faker
from datetime import datetime, timedelta
import os, sys, django

# Add project root to path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "employee_project.settings")
django.setup()

from employees.models import Department, Employee, Attendance  # <-- corrected

fake = Faker()

def create_departments():
    departments = ['HR', 'Finance', 'Engineering', 'Marketing', 'Sales']
    locations = ['Mumbai', 'Pune', 'Bangalore', 'Delhi', 'Hyderabad']
    for name, location in zip(departments, locations):
        Department.objects.get_or_create(name=name, location=location)

def create_employees(num=5):
    departments = list(Department.objects.all())
    positions = ['Manager', 'Developer', 'Analyst', 'Designer', 'Tester']
    for _ in range(num):
        Employee.objects.create(
            first_name=fake.first_name(),
            last_name=fake.last_name(),
            email=fake.unique.email(),
            phone_number=fake.phone_number(),
            date_of_birth=fake.date_of_birth(minimum_age=22, maximum_age=60),
            department=random.choice(departments),
            position=random.choice(positions),
            date_joined=fake.date_between(start_date='-5y', end_date='today'),
        )

def create_attendance(num_days=7):
    employees = Employee.objects.all()
    statuses = ['P', 'A', 'L']
    today = datetime.now().date()
    for emp in employees:
        for i in range(num_days):
            date = today - timedelta(days=i)
            status = random.choices(statuses, weights=[0.8, 0.1, 0.1])[0]
            Attendance.objects.get_or_create(employee=emp, date=date, status=status)

if __name__ == '__main__':
    create_departments()
    create_employees(5)
    create_attendance(7)
    print("Fake data created successfully.")
