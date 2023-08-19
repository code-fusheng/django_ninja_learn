from django.db import models

# Create your models here.


class Department(models.Model):
    """"部门表"""
    title = models.CharField(max_length=100)

class Employee(models.Model):
    """员工表"""
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    department = models.BigIntegerField(null=True, blank=True)
    birthdate = models.DateField(null=True, blank=True)
    cv = models.FileField(null=True, blank=True)
