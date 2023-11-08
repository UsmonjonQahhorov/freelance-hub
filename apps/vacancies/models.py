from django.db import models
from apps.vacancies.choices import VacancyStatusChoice


class Vacancies(models.Model):
    owner = models.OneToOneField(to='users.User', on_delete=models.PROTECT)
    title = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    salary_from = models.FloatField(null=True)
    salary_to = models.FloatField(null=True)
    working_time_from = models.IntegerField()
    working_time_to = models.IntegerField()
    experience_year = models.FloatField(null=True)
    description = models.TextField()
    longitude = models.IntegerField()
    latitude = models.IntegerField()
    requirements = models.ManyToManyField(to='skills.Skills', through="VacancySkills")
    deadline = models.DateField(null=True)
    status = models.CharField(choices=VacancyStatusChoice.choices)
    requests = models.ManyToManyField(to='resumes.Resumes', through="resumes.VacancyResume",
                                      related_name='vacancy_resumes')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Vacancy"
        verbose_name_plural = "Vacancies"

    def __str__(self):
        return f"{self.title}"


class VacancySkills(models.Model):
    vacancy = models.ForeignKey(Vacancies, on_delete=models.PROTECT)
    skill = models.ForeignKey("skills.Skills", on_delete=models.PROTECT)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
