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


class UserUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            "first_name",
            "last_name",
            "phone_number",
            "email",
            "password"
        ]

    def update(self, instance, validated_data):
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.phone_number = validated_data.get('phone_number', instance.phone_number)
        instance.email = validated_data.get('email', instance.email)

        password = validated_data.get('password')
        if password:
            instance.password = make_password(password)

        instance.save()
        return instance


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


class UserRetrieveSerializer(serializers.ModelSerializer):
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
            "id",
            "first_name",
            "last_name",
            "phone_number",
            "email",
            "password"
        ]
