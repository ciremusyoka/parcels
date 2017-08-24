from django.shortcuts import render

from rest_framework import generics
from .serializers import ParcelSerializer
from .models import Parcels

class ParcelsList(generics.ListCreateAPIView):
    serializer_class = ParcelSerializer
    queryset = Parcels.objects.all()

class RetriveUpdateParcel(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ParcelSerializer
    queryset = Parcels.objects.all()