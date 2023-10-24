from apps.users.models import TimeStampedModel
from django.db import models


class Resumes(TimeStampedModel):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    second_name = models.CharField(max_length=100)
    profession = models.ForeignKey(to="Professions.id", on_delete=models.PROTECT)
    gender = models.CharField(choices=)
