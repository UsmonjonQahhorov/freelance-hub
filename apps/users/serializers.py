import re

from apps.users.models import User
from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from django.contrib.auth.hashers import make_password


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            "first_name",
            "last_name",
            "phone_number",
            "email",
            "password"
        ]


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


class UserDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            "first_name",
            "last_name",
            "phone_number",
            "email",
        ]


class UserLoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            "email",
            "password",
        ]


class UserListSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            "first_name",
            "last_name",
            "phone_number",
            "email",
        ]
