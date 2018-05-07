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
    Phone_Number = models.CharField(max_length=12)
    county = models.CharField(max_length=50, null=True, blank=True)
    constituency = models.CharField(max_length=50, null=True, blank=True)
    town = models.CharField(max_length=50, null=True, blank=True)
    Id_No = models.CharField(max_length=8, null=True, blank=True)
    Transporter_Request = models.BooleanField(default=False)
    Transporter_Accepted = models.BooleanField(default=False)
    photo = models.ImageField(upload_to=get_file_path, null=True, blank=True)
    # code = models.CharField(max_length=6)

    def __str__(self):
        return self.Phone_Number

class Verification(models.Model):
    code = models.CharField(max_length=6)

    def __str__(self):
        return self.code