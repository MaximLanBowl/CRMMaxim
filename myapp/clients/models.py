from django.db import models


class Service(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    cost = models.DecimalField(max_digits=10, decimal_places=2)


class Client(models.Model):
    objects = None
    name = models.CharField(max_length=50, default=True)
    email = models.EmailField()
    phone = models.CharField(max_length=15, default=True)