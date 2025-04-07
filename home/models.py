from django.db import models

# Create your models here.
# models.py
from django.db import models

class Department(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        db_table = 'app_departments'

    def __str__(self):
        return self.name

class Employee(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name='employees')

    class Meta:
        db_table = 'app_employees'

    def __str__(self):
        return self.name
