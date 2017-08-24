from django.contrib import admin

from .models import Parcels

class AdminParcels(admin.ModelAdmin):
    list_display = ['id', 'name', 'origin', 'destination', 'SendingCost', 'ParcelCost', 'parcelstatus']

admin.site.register(Parcels,AdminParcels)
