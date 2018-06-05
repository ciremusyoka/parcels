from django.shortcuts import render

from rest_framework import generics, permissions
from .serializers import (ParcelSerializer, CourierSerializer, AcceptJobSerializer,
                            ReceivedSerializer, DeliveredSerializer )
from .models import Parcels
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK,HTTP_400_BAD_REQUEST,HTTP_201_CREATED
from .permissions import IsSender, IsTransporter

class ParcelsList(generics.CreateAPIView):
    # permission_classes = (permissions.IsAuthenticated,)
    serializer_class = ParcelSerializer
    queryset = Parcels.objects.all()

class UserParcelsList(generics.ListAPIView):
    serializer_class = ParcelSerializer

    def get_queryset(self):
        user = self.request.user
        return Parcels.objects.filter(sender=user)

class RetrieveUpdateParcel(generics.RetrieveUpdateAPIView):
    # permission_classes = (IsSender,)
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

