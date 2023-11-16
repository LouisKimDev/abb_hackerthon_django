from django.db import models


class Location(models.Model):
    latitude = models.FloatField()
    longtitude = models.FloatField()
    name = models.CharField(max_length=255)
    type = models.CharField(max_length=50)
    perce = models.IntegerField()
