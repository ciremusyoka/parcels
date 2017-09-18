# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import Profile

from django.contrib import admin

class ProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'PhoneNumber', 'county', 'constituency', 'town',
                  'IdNo', 'TransporterRequest', 'TransporterAccepted', 'photo')
admin.site.register(Profile,ProfileAdmin)

# Register your models here.
