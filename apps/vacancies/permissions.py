from rest_framework.permissions import BasePermission


class VacanciesPermissions(BasePermission):
    def has_permission(self, request, view):
        # if view.action == 'list':
        #     return bool(request.user.is_authenticated and request.user.is_superuser)
        # elif view.action == 'create' or view.action == 'destroy':
        #     return bool(request.user.is_authenticated)
        return True


class VacancySkillPermission(BasePermission):
    def has_permission(self, request, view):
        # if view.action == 'list':
        #     return bool(request.user.is_authenticated and request.user.is_superuser)
        # elif view.action == 'create' or view.action == 'destroy' or view.action == 'retrieve':
        #     return bool(request.user.is_authenticated)
        return True
