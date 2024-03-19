from django.db import models


class Product(models.Model):
    objects = None
    name = models.CharField(null=False, primary_key=True, max_length=80)
    description = models.CharField(null=False)
    price = models.IntegerField()
