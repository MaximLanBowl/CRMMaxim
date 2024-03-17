from django.contrib.auth import get_user_model
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import User
from django.db import models


class Service(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    cost = models.DecimalField(max_digits=10, decimal_places=2)


class Client(models.Model):
    objects = None
    username = models.CharField(default=True, null=True)
    user_id = models.CharField(null=True)
    email = models.EmailField(default='Почта', unique=True, null=True)
    status = models.BooleanField(default=True, null=True)

