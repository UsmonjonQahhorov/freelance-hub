from django.db import models


class VacancyStatusChoice(models.TextChoices):
    ACTIVE = ('active', "Active")
    INACTIVE = ('inactive', "Inactive")
