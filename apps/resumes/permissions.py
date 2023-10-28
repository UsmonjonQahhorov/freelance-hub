from rest_framework.permissions import BasePermission


class ResumePermission(BasePermission):
    def has_permission(self, request, view):
        if view.action == 'retrieve':
            return True
        return bool(request.user.is_authenticated and request.user.is_superuser)
