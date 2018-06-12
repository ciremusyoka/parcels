# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from .serializers import CreateUserSerializer, LoginUserSerializer, UsersSerializer, ProfileSerializer,\
    ChangePasswordSerializer, UpdateUserSerializer, ResetPasswordSerializer, TransportersSerializer, \
    UserInfoSerializer
from rest_framework import generics,permissions
from django.contrib.auth import get_user_model
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.status import HTTP_200_OK,HTTP_400_BAD_REQUEST,HTTP_201_CREATED
from django.contrib.auth.models import Group, User
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from .permissions import IsOwner
from .models import Profile

# end point for creating user
class CreateUserView(generics.CreateAPIView):
    model = get_user_model()
    # permission_classes = (permissions.IsAllowany)
    serializer_class = CreateUserSerializer

    def post(self, request, *args, **kwargs):
        serializer = CreateUserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=HTTP_201_CREATED)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

#end point for creating user profile
class CreateProfileView(generics.CreateAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer


class LoginUserView(APIView):
    serializer_class = LoginUserSerializer
    model = User.objects.all()

    def post(self, request,*args,**kwargs):
        data=request.data
        serializer = LoginUserSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            new_data= serializer.data
            return Response("user details confirmed",  HTTP_200_OK)
        return Response(serializer.error, HTTP_400_BAD_REQUEST)

# list of users for admins only
class UsersListView(generics.ListCreateAPIView):
    # permission_classes = [permissions.IsAdminUser]
    queryset = User.objects.all()
    serializer_class = UsersSerializer

#end point of getting user id easily
class RetrieveUserIDView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = CreateUserSerializer
    lookup_field = 'username'



# end point for editing user details
class RetrieveUpdateUsers(generics.RetrieveUpdateAPIView):
    # permission_classes = (permissions.IsAuthenticated, IsOwner,)
    queryset = User.objects.all()
    lookup_field = 'username'

    def get_serializer_class(self):
        if self.request.method == 'GET':
            serializer_class = UserInfoSerializer
            return serializer_class
        else:
            serializer_class = UpdateUserSerializer
            return serializer_class



    # def get_object(self):
    #     obj = self.request.user
    #     id = obj.profile.IdNo
    #     # print(id +'hello')
    #     return obj
    # def update(self, request, *args, **kwargs):
    #     self.id = self.get_object()
    #     serializer = self.get_serializer(data=request.data)
    #     print ('hello')
    #     self.id.save()

#filter to get trnsporters
class FilterTransporters(generics.ListAPIView):
    serializer_class = TransportersSerializer
    queryset = Profile.objects.all()


    def filter_queryset(self, queryset):
        county = self.request.query_params.get('county', None)
        accepted = self.request.query_params.get('Transporter_Accepted', None)
        if county is not None:
            queryset = queryset.filter(county=county)
        if accepted is not None:
            queryset = queryset.filter(Transporter_Accepted=accepted)
        return queryset

# change users password
class ChangePasswordView(generics.UpdateAPIView):
    """
    An endpoint for changing password.
    """
    serializer_class = ChangePasswordSerializer
    model = get_user_model()
    # permission_classes = (permissions.IsAuthenticated,)

    def get_object(self, queryset=None):
        obj = self.request.user
        print(obj)
        return obj

    def update(self, request, *args, **kwargs):
        self.object = self.get_object()
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            # Check old password
            if not self.object.check_password(serializer.data.get("old_password")):
                return Response({"old_password": ["Your current password didn't match. please try again"]}, status=HTTP_400_BAD_REQUEST)
            # set_password also hashes the password that the user will get
            self.object.set_password(serializer.data.get("new_password"))
            self.object.save()
            return Response("Your password has been successfully changed.", status=HTTP_200_OK)

        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

class ResetPasswordView(APIView):
    serializer_class = ResetPasswordSerializer


    model = get_user_model()
    def post(self, request, *args, **kwargs):

        data = request.data
        serializer = ResetPasswordSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            new_data = serializer.data
            return Response(new_data, HTTP_200_OK)
        return Response(serializer.error, HTTP_400_BAD_REQUEST)

# class CustomObtainAuthToken(ObtainAuthToken):
#     def post(self, request, *args, **kwargs):
#         response = super(CustomObtainAuthToken, self).post(request, *args, **kwargs)
#         token = Token.objects.get(key=response.data['token'])
#         return Response({'token': token.key, 'id': token.id})