from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, User
import datetime


STATUS_CHOICE = [
        ('W', 'Installation Requested'),
        ('Y', 'Installation in Progress'),
        ('G', 'Installation Complete'),
        ('R', 'Installation Rejected')
    ]
ROLE_CHOICES = [('M', 'MANAGER'), ('I', "INSTALLER")]


class Customer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    date_created = models.DateTimeField(auto_now=True)
    address = models.CharField(max_length=1000)
    postal_code = models.CharField(max_length=4)

    class Mata:
        unique_together = ['user.username', 'user.email']

    def __str__(self):
        return self.first_name + ' ' + self.last_name


class Employee(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    date_joined = models.DateTimeField(auto_now=True)
    role = models.CharField(max_length=2, choices=ROLE_CHOICES, default="I")
    postal_code = models.CharField(max_length=4)

    class Mata:
        unique_together = ['user.username', 'user.email']

    def __str__(self):
        return self.first_name + ' ' + self.first_name + ', ' + self.role


class Status(models.Model):
    status = models.CharField(max_length=100)
    notes = models.CharField(max_length=200)
    date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.status + ', ' + self.notes


class InstallationRequest(models.Model):
    customer_name = models.CharField(max_length=200)
    address = models.CharField(max_length=2000)
    appointment_date = models.DateField(auto_now=True)
    date_created = models.DateField(auto_now=True)
    date_modified = models.DateTimeField(auto_now=True)

    status = models.CharField(max_length=2, choices=STATUS_CHOICE, default='W')

    class Meta:
        ordering = ['date_modified']

    def __str__(self):
        return self.customer_name + ', ' + self.status + ', ' \
               + str(self.appointment_date) + ', ' + str(self.date_modified)
