from apps.resumes.choices import ResumeStatusChoice
from apps.users.models import TimeStampedModel
from django.db import models


class Resumes(TimeStampedModel):
    owner = models.ForeignKey(to="Users.id", on_delete=models.CASCADE)
    profession = models.ForeignKey(to="Professions.id", on_delete=models.PROTECT)
    location = models.CharField(max_length=255)
    education = models.JSONField
    status = models.CharField(choices=ResumeStatusChoice)
    skills = models.ManyToManyField(Skills, through="ResumeSkills")
    vacancies = models.ManyToManyField(Vacancies, through="VacancyResume")

    class Meta:
        verbose_name = "Resume"
        verbose_name_plural = "Resumes"

    def __str__(self):
        return f"{self.profession}"
