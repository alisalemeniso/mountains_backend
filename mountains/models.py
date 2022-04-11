# from django.db import models
from django.contrib.gis.db import models


class Mountain(models.Model):
    name = models.CharField(max_length=200)
    altitude = models.IntegerField()
    lat = models.FloatField()
    long = models.FloatField()
    location = models.PointField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['id']
