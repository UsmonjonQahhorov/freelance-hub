from rest_framework import serializers

from apps.skills.models import Skills


class SkillsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skills
        fields = "__all__"


class SkillsCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skills
        exclude = ['created_at', 'updated_at']


class SkillsDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skills
        fields = '__all__'


class SkillsListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skills
        exclude = ['created_at', 'updated_at']
