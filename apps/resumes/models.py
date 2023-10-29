from apps.resumes.choices import ResumeStatusChoice
from django.db import models

from apps.users.models import User


class Resumes(models.Model):
    owner = models.OneToOneField(to=User, on_delete=models.PROTECT)
    location = models.CharField(max_length=255)
    education = models.JSONField
    status = models.CharField(choices=ResumeStatusChoice.choices)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # profession = models.OneToOneField(to=Professions, on_delete=models.PROTECT)
    # skills = models.ManyToManyField(Skills, through="ResumeSkills")
    # vacancies = models.ManyToManyField(Vacancies, through="VacancyResume")

    class Meta:
        verbose_name = "Resume"
        verbose_name_plural = "Resumes"

    def __str__(self):
        return f"{self.location}"
