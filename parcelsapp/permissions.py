from rest_framework import permissions
from .models import Parcels

class IsSender(permissions.BasePermission):
    message = 'you are not the sender of this parcel'

    def has_object_permission(self, request, view, obj):
        return obj.sender == request.user

        # the_sender = request.data['sender']
        # print the_sender
        # sender = Parcels.objects.filter(sender=the_sender)
        # return sender

class IsTransporter(permissions.BasePermission):
    message = 'your are not the transporter of this parcel'
    def has_object_permission(self, request, view, obj):
        return obj.transporter == request.transporter