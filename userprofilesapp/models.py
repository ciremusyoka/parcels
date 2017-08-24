# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
import uuid
import os

def get_file_path(instance, filename):
    ext = filename.split('.')[-1]
    filename = "%s.%s" % (uuid.uuid4(), ext)
    return os.path.join('media', filename)

class ProfileModel(models.Model):
    user= models.ForeignKey('auth.User')
    phonenumber = models.CharField(max_length=12)
    location = models.CharField(max_length=50)
    photo = models.ImageField(upload_to=get_file_path, null=True, blank=True)

    def __str__(self):
        return self.phonenumber

