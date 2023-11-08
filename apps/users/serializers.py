import random
import re
from django.core.validators import EmailValidator
from django.contrib.auth.hashers import make_password
from django.core.mail import send_mail
from rest_framework import serializers

from config.settings import EMAIL_HOST_USER

from apps.users.models import User, getKey, setKey, Employer


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            "first_name",
            "last_name",
            "phone_number",
            "email",
            "password",
        ]


class UserRegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=150, write_only=True)

    class Meta:
        model = User
        fields = (
            "first_name",
            "last_name",
            "phone_number",
            "email",
            "password",
        )

    def validate_email(self, value):
        if not value:
            raise serializers.ValidationError("Email manzilni kiritishingiz kerak.")
        if not re.match(r'^[a-zA-Z0-9._%+-]+@gmail\.com$', value):
            raise serializers.ValidationError("Email manzilni @gmail.com bilan tugatish kerak.")
        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError("Ushbu email manzil allaqachon ro'yxatdan o'tgan.")
        return value

    def validate(self, attrs):
        activate_code = random.randint(100000, 999999)
        user = User(
            first_name=attrs['first_name'],
            email=attrs['email'],
            last_name=attrs['last_name'],
            phone_number=attrs['phone_number'],
            password=make_password(attrs['password']),
            is_active=True,
        )
        setKey(
            key=attrs['email'],
            value={
                "user": user,
                "activate_code": activate_code
            },
            timeout=300
        )
        print(getKey(key=attrs['email']))
        send_mail(
            subject="Subject here",
            message=f"Your activation code.\n{activate_code}",
            from_email=EMAIL_HOST_USER,
            recipient_list=[attrs['email']],
            fail_silently=False,
        )
        return super().validate(attrs)


class CheckActivationCodeSerializer(serializers.Serializer):
    email = serializers.EmailField()
    activate_code = serializers.IntegerField(write_only=True)

    def validate(self, attrs):
        data = getKey(key=attrs['email'])
        print(data)
        if data and data['activate_code'] == attrs['activate_code']:
            return attrs
        raise serializers.ValidationError(
            {"error": "Error activate code or email"}
        )


class ResetPasswordSerializer(serializers.Serializer):
    email = serializers.EmailField()


class ResetPasswordConfirmSerializer(serializers.Serializer):
    email = serializers.EmailField()
    activation_code = serializers.CharField()
    new_password = serializers.CharField()
    confirm_password = serializers.CharField()


class UserRetrieveSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            "first_name",
            "last_name",
            "phone_number",
            "email",
        ]


class EmployerRegisterSerializer(serializers.Serializer):
    first_name = serializers.CharField(max_length=30, write_only=True)
    last_name = serializers.CharField(max_length=30, write_only=True)
    phone_number = serializers.CharField(max_length=15, write_only=True)
    email = serializers.EmailField(write_only=True)
    password = serializers.CharField(max_length=150, write_only=True)
    company = serializers.CharField(max_length=255, write_only=True)
    location = serializers.CharField(max_length=255, write_only=True)

    def validate_email(self, value):
        if not value:
            raise serializers.ValidationError("Email manzilni kiritishingiz kerak.")
        if not re.match(r'^[a-zA-Z0-9._%+-]+@gmail\.com$', value):
            raise serializers.ValidationError("Email manzilni @gmail.com bilan tugatish kerak.")
        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError("Ushbu email manzil allaqachon ro'yxatdan o'tgan.")
        return value

    def create(self, validated_data):
        activate_code = random.randint(1000, 9999)
        user = User.objects.create_user(
            username=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            phone_number=validated_data['phone_number'],
            email=validated_data['email'],
            password=make_password(validated_data['password']),
            is_active=False,
            employer=True
        )

        Employer.objects.create(
            user=user,
            company=validated_data['company'],
            location=validated_data['location'],
        )

        send_mail(
            subject="Subject here",
            message=f"Your activation code.\n{activate_code}",
            from_email=EMAIL_HOST_USER,
            recipient_list=[validated_data['email']],
            fail_silently=False,
        )
        return user
