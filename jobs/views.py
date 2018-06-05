# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from rest_framework import generics,permissions
from .models import JobsModel
from serializers import JobsSerializer
from .permissions import IsTransporter, IsSender

class JobsView(generics.ListCreateAPIView):
    # permission_classes = (permissions.IsAuthenticated,)
    serializer_class = JobsSerializer
    queryset = JobsModel.objects.all()

class EditJobsView(generics.RetrieveUpdateAPIView):
    # permission_classes = (IsSender, IsTransporter,)
    serializer_class = JobsSerializer
    queryset = JobsModel.objects.all()

class MyJobsView(generics.ListAPIView):
    # permission_classes = (permissions.IsAuthenticated,)
    serializer_class = JobsSerializer

    def get_queryset(self):
        user = self.request.user
        return JobsModel.objects.filter(transporter=user)
