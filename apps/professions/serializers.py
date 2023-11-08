from rest_framework import serializers

from apps.professions.models import Professions


class ProfessionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Professions
        fields = "__all__"


class ProfessionsCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Professions
        exclude = ['created_at', 'updated_at']


class ProfessionsDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Professions
        fields = '__all__'


class ProfessionsListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Professions
        exclude = ['created_at', 'updated_at']
