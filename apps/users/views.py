from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from apps.users.models import User
from apps.users.permissions import UserPermission
from apps.users.serializers import (
    UserSerializer,
    UserCreateSerializer,
    UserDetailSerializer,
    UserListSerializer
)


# Create your views here.


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [UserPermission]

    def get_serializer_class(self):
        if self.action == "create":
            return UserCreateSerializer
        elif self.action in ("update", "partial_update"):
            return UserDetailSerializer
        elif self.action == "list":
            return UserListSerializer
        elif self.action == "retrieve":
            return UserDetailSerializer
        return self.serializer_class
