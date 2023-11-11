import random
from django.core.mail import send_mail
from rest_framework import status
from rest_framework.generics import GenericAPIView, CreateAPIView, ListAPIView, RetrieveAPIView
from rest_framework.response import Response
from apps.users.models import User, getKey
from apps.users.permissions import UserPermission
from rest_framework.permissions import AllowAny
from apps.users.serializers import (UserRegisterSerializer, CheckActivationCodeSerializer, ResetPasswordSerializer,
                                    ResetPasswordConfirmSerializer, UserRetrieveSerializer, EmployerRegisterSerializer)
from rest_framework.views import APIView


class UserInfoListAPIView(ListAPIView):
    queryset = User.objects.all
    permission_classes = [UserPermission, AllowAny]
    serializer_class = UserRetrieveSerializer

    def get_queryset(self):
        if self.request.user.is_authenticated:
            if self.request.user.is_superuser:
                return User.objects.all()
            else:
                return User.objects.filter(id=self.request.user.id)

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer_class = UserRetrieveSerializer
        serializer = serializer_class(queryset, many=True)
        return Response(serializer.data)


class UserRegisterCreateAPIView(CreateAPIView):
    serializer_class = UserRegisterSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class CheckActivationCodeGenericAPIView(GenericAPIView):
    serializer_class = CheckActivationCodeSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.data
        print(data)
        if 'email' not in data:
            user_data = getKey(key=data['email'])

            if 'user' not in user_data:
                user = user_data['user']
                user.is_active = True
                user.is_verified = True
                user.save()
                return Response({"message": "Your email has been confirmed"}, status=status.HTTP_200_OK)

        return Response({"error": "Invalid data"}, status=status.HTTP_400_BAD_REQUEST)


class ResetPasswordView(CreateAPIView):
    serializer_class = ResetPasswordSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            email = serializer.validated_data['email']
            try:
                user = User.objects.get(email=email)
            except User.DoesNotExist:
                return Response({"detail": "User not found with this email."}, status=status.HTTP_400_BAD_REQUEST)

            activation_code = str(random.randint(100000, 999999))
            user.set_password(activation_code)
            user.save()

            send_mail(
                'Password Reset Confirmation',
                f'Your password reset code is: {activation_code}',
                'admin@example.com',
                [email],
                fail_silently=False,
            )

            return Response({"detail": "Password reset code sent to your email."}, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ResetPasswordConfirmView(CreateAPIView):
    serializer_class = ResetPasswordConfirmSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            email = serializer.validated_data['email']
            activation_code = serializer.validated_data['activation_code']
            new_password = serializer.validated_data['new_password']
            confirm_password = serializer.validated_data['confirm_password']

            try:
                user = User.objects.get(email=email)
            except User.DoesNotExist:
                return Response({"detail": "User not found with this email."}, status=status.HTTP_400_BAD_REQUEST)

            if user.check_password(activation_code):
                if new_password == confirm_password:
                    user.set_password(new_password)
                    user.save()
                    return Response({"detail": "Password reset successfully."}, status=status.HTTP_200_OK)
                else:
                    return Response({"detail": "New password and confirm password do not match."},
                                    status=status.HTTP_400_BAD_REQUEST)
            else:
                return Response({"detail": "Invalid activation code."}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class EmployerRegisterAPIView(CreateAPIView):
    serializer_class = EmployerRegisterSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

#
# class UserRetrieveAPIView(APIView):
#     def get(self, request):
#         user_instance = request.user
#         if not user_instance:
#             return Response({"error": "User not found"}, status=status.HTTP_404_NOT_FOUND)
#
#         serializer = UserRetrieveSerializer(user_instance)
#         return Response(serializer.data, status=status.HTTP_200_OK)
