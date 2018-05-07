# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import Profile, Verification

from django.contrib import admin

class ProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'Phone_Number', 'county', 'constituency', 'town',
                  'Id_No', 'Transporter_Request', 'Transporter_Accepted', 'photo',)

# class VerificationAdmin(admin.ModelAdmin):
#     list_display = ('id', 'code')

admin.site.register(Profile,ProfileAdmin)
# admin.site.register(Verification, VerificationAdmin)

# Register your models here.
