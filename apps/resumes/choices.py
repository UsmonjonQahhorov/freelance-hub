from django.db import models


class ResumeStatusChoice(models.TextChoices):
    ACTIVE = ('active', "Active")
    INACTIVE = ('inactive', "Inactive")
