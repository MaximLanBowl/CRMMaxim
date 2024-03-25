from django.db import models


class Service(models.Model):
    objects = None
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.IntegerField(default=0)
