# from rest_framework import viewsets, status
# from apps.users.models import User
# from apps.users.permissions import UserPermission
# from apps.users.serializers import UserCreateSerializer, UserListSerializer
# from rest_framework.response import Response
# from rest_framework.mixins import (
#     ListModelMixin,
#     CreateModelMixin,
#     UpdateModelMixin,
#     DestroyModelMixin,
#     RetrieveModelMixin
# )
# from rest_framework.viewsets import GenericViewSet
# from rest_framework.views import APIView
# from rest_framework.permissions import IsAuthenticated
# from rest_framework.permissions import AllowAny
#
#
# class UserRegView(ListModelMixin,
#                   CreateModelMixin,
#                   UpdateModelMixin,
#                   DestroyModelMixin,
#                   GenericViewSet):
#     queryset = User.objects.all()
#     serializer_class = UserCreateSerializer
#     permission_classes = [UserPermission, IsAuthenticated]
#
#     def get_queryset(self):
#         if self.request.user.is_authenticated:
#             return User.objects.filter(id=self.request.user.id)
#         else:
#             return User.objects.none()
#
#     def list(self, request, *args, **kwargs):
#         queryset = self.get_queryset()
#         serializer = self.get_serializer(queryset, many=True)
#         return Response(serializer.data)
#
#     def create(self, request, *args, **kwargs):
#         serializer = self.get_serializer(data=request.data)
#         if serializer.is_valid():
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#

#

from rest_framework.mixins import (
    ListModelMixin,
    CreateModelMixin,
    UpdateModelMixin,
    DestroyModelMixin,
)
from rest_framework import status
from rest_framework.viewsets import GenericViewSet
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response

from apps.users.models import User
from apps.users.permissions import UserPermission
from apps.users.serializers import UserListSerializer, UserCreateSerializer, UserRetrieveSerializer, \
    UserUpdateSerializer


class UserRegView(ListModelMixin, CreateModelMixin, UpdateModelMixin, DestroyModelMixin, GenericViewSet):
    queryset = User.objects.all

    permission_classes = [UserPermission, AllowAny]

    def get_queryset(self):
        if self.request.user.is_authenticated:
            if self.request.user.is_superuser:
                return User.objects.all()
            else:
                return User.objects.filter(id=self.request.user.id)

    def get_serializer_class(self):
        if self.action == 'list':
            return UserListSerializer
        elif self.action == 'create':
            return UserCreateSerializer
        elif self.action == 'retrieve':
            return UserRetrieveSerializer
        elif self.action == 'update':
            return UserUpdateSerializer
        elif self.action == 'partial_update':
            return UserUpdateSerializer
        elif self.action == 'destroy':
            return UserListSerializer
        else:
            return UserCreateSerializer

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer_class = self.get_serializer_class()
        serializer = serializer_class(queryset, many=True)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        serializer_class = self.get_serializer_class()
        serializer = serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#set password endpoint alohida
#get-me alohida endpoint
#django signals
