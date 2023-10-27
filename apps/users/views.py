from rest_framework import viewsets, status
from apps.users.models import User
from apps.users.permissions import UserPermission
from apps.users.serializers import UserCreateSerializer, UserLoginSerializer
from rest_framework.response import Response
import jwt
import datetime
from rest_framework.decorators import action
from rest_framework.mixins import CreateModelMixin
from rest_framework.viewsets import GenericViewSet


class UserRegView(CreateModelMixin, GenericViewSet):
    queryset = User.objects.all()
    serializer_class = UserCreateSerializer
    permission_classes = [UserPermission]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            instance = self.perform_create(serializer)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserLogViewSet(CreateModelMixin, GenericViewSet):
    queryset = User.objects.all()
    serializer_class = UserLoginSerializer

    def login(self, request):
        email = request.data.get('email')  # Use get to avoid KeyError
        password = request.data.get('password')

        user = User.objects.filter(email=email).first()
        if user is None:
            return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)

        if not user.check_password(password):
            return Response({'error': 'Incorrect password'}, status=status.HTTP_401_UNAUTHORIZED)

        payload = {
            'id': user.id,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=60),
            'iat': datetime.datetime.utcnow()
        }

        token = jwt.encode(payload, 'secret', algorithm='HS256').decode('utf-8')

        return Response({'jwt': token}, status=status.HTTP_200_OK)
