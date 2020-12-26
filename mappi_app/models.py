from django.db import models


class Store(models.Model):
    store_id = models.IntegerField()
    adress = models.CharField(max_length=100)
    store_name = models.CharField(max_length=100)