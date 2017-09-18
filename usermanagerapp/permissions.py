from rest_framework import permissions
from .models import Profile

class IsOwner(permissions.BasePermission):
    message = 'you are not the owner of this object'
    def has_object_permission(self, request, view, obj):
        return obj.profile.user == request.user