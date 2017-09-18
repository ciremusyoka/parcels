from rest_framework import permissions

class IsSender(permissions.BasePermission):
    message = 'you are not the sender of this parcel'
    def has_object_permission(self, request, view, obj):
        return obj.sender == request.sender

class IsTransporter(permissions.BasePermission):
    message = 'your are not the transporter of this parcel'
    def has_object_permission(self, request, view, obj):
        return obj.transporter == request.transporter