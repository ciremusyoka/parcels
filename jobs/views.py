# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from rest_framework import generics,permissions
from .models import JobsModel
from serializers import JobsSerializer

class JobsView(generics.ListCreateAPIView):
    serializer_class = JobsSerializer
    queryset = JobsModel.objects.all()

class MyJobsView(generics.ListAPIView):
    serializer_class = JobsSerializer

    def get_queryset(self):
        user = self.request.user
        return JobsModel.objects.filter(transporter=user)
