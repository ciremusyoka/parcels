# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from .serializers import CreateUserSerializer, LoginUserSerializer, UsersSerializer, ChangePasswordSerializer
from rest_framework import generics,permissions
from django.contrib.auth import get_user_model
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.status import HTTP_200_OK,HTTP_400_BAD_REQUEST
from django.contrib.auth.models import Group, User

class CreateUserView(generics.CreateAPIView):
    model = get_user_model()
    #permission_classes = (AllowAny)
    serializer_class = CreateUserSerializer


class LoginUserView(APIView):
    serializer_class = LoginUserSerializer

    def post(self, request,*args,**kwargs):
        data=request.data
        serializer = LoginUserSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            new_data= serializer.data
            return Response(new_data,  HTTP_200_OK)
        return Response(serializer.error, HTTP_400_BAD_REQUEST)

# list of users for admins only
class UsersListView(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAdminUser]
    queryset = User.objects.all()
    serializer_class = UsersSerializer

# edit user details
class RetrieveUpdateUsers(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UsersSerializer

# change users password
class ChangePasswordView(generics.UpdateAPIView):
    """
    An endpoint for changing password.
    """
    serializer_class = ChangePasswordSerializer
    model = get_user_model()
    permission_classes = (permissions.IsAuthenticated,)

    def get_object(self, queryset=None):
        obj = self.request.user
        return obj

    def update(self, request, *args, **kwargs):
        self.object = self.get_object()
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            # Check old password
            if not self.object.check_password(serializer.data.get("old_password")):
                return Response({"old_password": ["Wrong password."]}, status=HTTP_400_BAD_REQUEST)
            # set_password also hashes the password that the user will get
            self.object.set_password(serializer.data.get("new_password"))
            self.object.save()
            return Response("Success.", status=HTTP_200_OK)

        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)
