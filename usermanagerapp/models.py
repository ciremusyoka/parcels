# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
import uuid
import os

def get_file_path(instance, filename):
    ext = filename.split('.')[-1]
    filename = "%s.%s" % (uuid.uuid4(), ext)
    return os.path.join('media', filename)

class Profile(models.Model):
    user = models.OneToOneField('auth.User')
    PhoneNumber = models.CharField(max_length=12)
    county = models.CharField(max_length=50, null=True, blank=True)
    constituency = models.CharField(max_length=50, null=True, blank=True)
    town = models.CharField(max_length=50, null=True, blank=True)
    IdNo = models.CharField(max_length=8, null=True, blank=True)
    TransporterRequest = models.BooleanField(default=False)
    TransporterAccepted = models.BooleanField(default=False)
    photo = models.ImageField(upload_to=get_file_path, null=True, blank=True)

    def __str__(self):
        return self.PhoneNumber
