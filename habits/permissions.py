from rest_framework import permissions


class IsOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.user == request.user


class CannotEditOrDeletePublicHabit(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.method not in ('PUT', 'PATCH', 'DELETE')