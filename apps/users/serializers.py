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
    class Meta:
        model = User
        fields = [
            "first_name",
            "last_name",
            "phone_number",
            "email",
            "password"
        ]

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
            last_name=attrs['last_name'],
            email=attrs['email'],
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
            subject="Activation code for you account",
            message=f"Your activate code.\n{activate_code}",
            from_email=EMAIL_HOST_USER,
            recipient_list=[attrs['email']],
            fail_silently=False,
        )
        return super().validate(attrs)


class UserCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            "first_name",
            "last_name",
            "phone_number",
            "email",
            "password"
        ]

    def create(self, validated_data):
        password = validated_data.pop('password')
        validated_data['password'] = make_password(password)
        user = User(**validated_data)
        user.save()
        return user

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
            user = data['user']
            user.is_verified = True
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
    # user = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = [
            "first_name",
            "last_name",
            "phone_number",
            "email",
        ]

    # def get_user(self, obj):
    #     user_data = {
    #         "first_name": obj.user.first_name,
    #         "last_name": obj.user.last_name,
    #         "email": obj.user.email,
    #         "phone_number": obj.user.phone_number,
    #     }
    #     return user_data


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

    def validate(self, attrs):
        activate_code = random.randint(1000, 9999)

        user = User(
            first_name=attrs['first_name'],
            email=attrs['email'],
            last_name=attrs['last_name'],
            phone_number=attrs['phone_number'],
            password=make_password(attrs['password']),
            is_active=True,
            is_employer=True
        )
        user.save()

        employer = Employer(
            company=attrs["company"],
            location=attrs["location"],
            user=user
        )

        employer.save()
        setKey(
            key=attrs['email'],
            value={
                "user": user,
                "employer": employer,
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
