from __future__ import unicode_literals

from django.db import models

class Parcels(models.Model):
    status = (('searching', 'searching transporter'),('waiting',' waiting courier'),('ontransit', 'on transit'),
              ('received','received'),('delivered','delivered'))
    sender = models.ForeignKey('auth.User',related_name='parcels_sender')
    name = models.CharField(max_length=50)
    origin = models.CharField(max_length=50)
    destination = models.CharField(max_length=50)
    SendingCost = models.IntegerField(null=True, blank=True)
    TransporterResponse = models.BooleanField(default=False)
    CourierNumber = models.IntegerField(null=True, blank=True)
    ParcelCost = models.IntegerField()
    ParcelStatus = models.CharField(max_length=20, choices=(status))
    transporter = models.ForeignKey('auth.User', null=True, blank=True, related_name='parcels_transporter')
    DeliveredSender = models.BooleanField(default=False)
    DeliveredTransporter = models.BooleanField(default=False)



    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Parcels'
