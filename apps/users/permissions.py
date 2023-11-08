from rest_framework import permissions


class UserPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user and request.user.is_authenticated


# 1: email
# 2: first_name, last_name
# 3: komp_name
# 4: kompany_location: one_to_many_field
