# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from parcelsapp.models import Parcels

class JobsModel(models.Model):
    sender = models.ForeignKey('auth.User', related_name='sender_of_parcel')
    transporter = models.ForeignKey('auth.User', related_name='transporter_of_parcel')
    parcel = models.ForeignKey('parcelsapp.Parcels')
    date = models.DateField()
    accepted = models.BooleanField(default=False)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return str(self.date)

    class Meta:
        verbose_name_plural = 'Jobs'
