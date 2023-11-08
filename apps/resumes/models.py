from apps.resumes.choices import ResumeStatusChoice, ResumeGenderChoices, ResumeEducationChoices
from django.db import models


class Resumes(models.Model):
    owner = models.OneToOneField('users.User', on_delete=models.PROTECT)
    surname = models.CharField(max_length=100, null=True)
    gender = models.CharField(choices=ResumeGenderChoices.choices)
    location = models.CharField(max_length=255)
    birthday = models.DateTimeField
    citizenship = models.CharField(max_length=30)
    level_education = models.CharField(choices=ResumeEducationChoices.choices)
    experience_year = models.FloatField()
    status = models.CharField(choices=ResumeStatusChoice.choices)
    profession = models.ForeignKey('professions.Professions', on_delete=models.PROTECT)
    skills = models.ManyToManyField('skills.Skills', through='ResumeSkills')
    vacancies = models.ManyToManyField('vacancies.Vacancies', through='VacancyResume')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Resume"
        verbose_name_plural = "Resumes"

    def __str__(self):
        return f"{self.location}"


class ResumeSkills(models.Model):
    resume = models.ForeignKey(Resumes, on_delete=models.PROTECT)
    skill = models.ForeignKey('skills.Skills', on_delete=models.PROTECT)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class VacancyResume(models.Model):
    resume = models.ForeignKey(Resumes, on_delete=models.PROTECT)
    vacancy = models.ForeignKey('vacancies.Vacancies', on_delete=models.PROTECT)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
