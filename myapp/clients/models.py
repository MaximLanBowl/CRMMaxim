from django.contrib.auth import get_user_model
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import User
from django.db import models


class Service(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    cost = models.DecimalField(max_digits=10, decimal_places=2)


User = get_user_model()


class Client(models.Model):
    objects = None
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    email = models.EmailField(default='Почта', unique=True, null=False)
    status = models.BooleanField(default=True, null=False)
