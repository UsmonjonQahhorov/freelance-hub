from rest_framework.permissions import BasePermission


class ProfessionPermission(BasePermission):
    def has_permission(self, request, view):
        if view.action == 'create' or view.action == 'destroy' or view.action == 'list':
            return bool(request.user.is_authenticated and request.user.is_superuser)
        return True
