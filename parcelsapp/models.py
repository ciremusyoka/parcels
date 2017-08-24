from __future__ import unicode_literals

from django.db import models

class Parcels(models.Model):
    status = (('ontransit', 'ontransit'), ('delivered', 'delivered'))
    name = models.CharField(max_length=50)
    origin = models.CharField(max_length=50)
    destination = models.CharField(max_length=50)
    SendingCost = models.IntegerField()
    ParcelCost = models.IntegerField()
    parcelstatus = models.CharField(max_length=20, choices=(status))


    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Parcels'
