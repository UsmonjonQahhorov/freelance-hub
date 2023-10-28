from rest_framework import serializers

from apps.resumes.models import Resumes


class ResumesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Resumes
        fields = "__all__"


class ResumesCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Resumes
        exclude = ['owner']


class ResumesDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Resumes
        fields = '__all__'


class ResumesListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Resumes
        exclude = ['created_at', 'updated_at', 'skills', 'vacancies']
