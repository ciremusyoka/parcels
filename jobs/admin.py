# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import JobsModel

class JobsAdmin(admin.ModelAdmin):
    list_display = ['id', 'sender', 'transporter', 'date', 'accepted', 'completed']

admin.site.register(JobsModel,JobsAdmin)


