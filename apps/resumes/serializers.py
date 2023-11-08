from rest_framework import serializers

from apps.resumes.models import Resumes, ResumeSkills, VacancyResume


class ResumesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Resumes
        fields = "__all__"


class ResumesCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Resumes
        exclude = ['owner', 'created_at', 'updated_at']

    def save(self, **kwargs):
        citizenship = self.data.get('citizenship').lower
        self.validated_data.pop('citizenship')
        owner = self.context['request'].user
        instance = Resumes(owner=owner, citizenship=citizenship, **self.validated_data)
        instance.save()
        return instance


class ResumesDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Resumes
        fields = '__all__'


class SearchResumeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Resumes
        exclude = ['status', 'vacancies', 'updated_at']


class ResumeSkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = ResumeSkills
        fields = "__all__"


class ResumeSkillCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = ResumeSkills
        exclude = ['created_at', 'updated_at']


class ResumeSkillDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = ResumeSkills
        fields = '__all__'


class VacancyResumeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Resumes
        fields = "__all__"


class VacancyResumeCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = VacancyResume
        exclude = ['created_at', 'updated_at']


class VacancyResumeDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = VacancyResume
        fields = '__all__'
