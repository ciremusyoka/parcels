from rest_framework import serializers
from .models import Parcels

class ParcelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Parcels
        fields = ('id', 'name', 'origin', 'destination', 'SendingCost', 'ParcelCost', 'parcelstatus')
