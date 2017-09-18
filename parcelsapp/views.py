from django.shortcuts import render

from rest_framework import generics, permissions
from .serializers import (ParcelSerializer, CourierSerializer, AcceptJobSerializer,
                            ReceivedSerializer, DeliveredSerializer )
from .models import Parcels
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK,HTTP_400_BAD_REQUEST,HTTP_201_CREATED
from .permissions import IsSender

class ParcelsList(generics.ListCreateAPIView):
    # permission_classes = (permissions.IsAuthenticated,)
    serializer_class = ParcelSerializer
    queryset = Parcels.objects.all()

    def get_queryset(self):
        return Parcels.objects.all()

class RetrieveUpdateParcel(generics.RetrieveUpdateAPIView):
    serializer_class = ParcelSerializer
    queryset = Parcels.objects.all()

class AcceptJobView(generics.RetrieveUpdateAPIView):
    serializer_class = AcceptJobSerializer
    queryset = Parcels.objects.all()

    # def update(self, request, *args, **kwargs):
    #     data = request.data
    #     serializer = AcceptJobSerializer(data=data)
    #     if serializer.is_valid(raise_exception=True):
    #         new_data = serializer.data
    #         return Response(new_data, HTTP_200_OK)
    #     return Response(serializer.error, HTTP_400_BAD_REQUEST)

class CourierView(generics.RetrieveUpdateAPIView):
    serializer_class = CourierSerializer
    queryset = Parcels.objects.all()

class ReceivedView(generics.RetrieveUpdateAPIView):
    serializer_class = ReceivedSerializer
    queryset = Parcels.objects.all()

class DeliveredView(generics.RetrieveUpdateAPIView):
    serializer_class = DeliveredSerializer
    queryset = Parcels.objects.all()

