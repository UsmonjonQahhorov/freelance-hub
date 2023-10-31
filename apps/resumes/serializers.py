from rest_framework import serializers

from apps.resumes.models import Resumes


class ResumesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Resumes
        fields = "__all__"


from rest_framework import serializers


class ResumesCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Resumes
        exclude = ['owner']

    def save(self, **kwargs):
        owner = self.context['request'].user
        instance = Resumes(owner=owner, **self.validated_data)
        instance.save()
        return instance


class ResumesDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Resumes
        fields = '__all__'


class ResumesListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Resumes
        # exclude = ['created_at', 'updated_at', 'skills', 'vacancies']
        exclude = ['created_at', 'updated_at']

