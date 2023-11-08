from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView

from apps.users.views import ResetPasswordConfirmView, UserInfoListAPIView, EmployerRegisterAPIView
from apps.users.views import (UserRegisterCreateAPIView, CheckActivationCodeGenericAPIView, ResetPasswordView)


urlpatterns = [

    path('user/api/register', UserRegisterCreateAPIView.as_view()),
    path('user/api/activate-code', CheckActivationCodeGenericAPIView.as_view()),
    path('user/api/reset-password', ResetPasswordView.as_view()),
    path('user/api/reset-password-confirm', ResetPasswordConfirmView.as_view()),
    path('user/api/login', TokenObtainPairView.as_view()),
    path('user/api/get-me', UserInfoListAPIView.as_view()),
    path('employer/api/register', EmployerRegisterAPIView.as_view()),

]
