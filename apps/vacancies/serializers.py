from rest_framework import serializers

from apps.vacancies.models import Vacancies, VacancySkills


class VacanciesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vacancies
        fields = "__all__"


class VacanciesCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vacancies
        exclude = ['owner', 'created_at', 'updated_at']

    def save(self, **kwargs):
        owner = self.context['request'].user
        instance = Vacancies(owner=owner, **self.validated_data)
        instance.save()
        return instance


class VacanciesDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vacancies
        fields = '__all__'


class SearchVacancySerializer(serializers.ModelSerializer):
    class Meta:
        model = Vacancies
        exclude = ['requests', 'updated_at']


class VacancySkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vacancies
        fields = "__all__"


class VacancySkillCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = VacancySkills
        exclude = ['created_at', 'updated_at']


class VacancySkillDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = VacancySkills
        fields = '__all__'
