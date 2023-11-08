from django.db import models


class ResumeStatusChoice(models.TextChoices):
    ACTIVE = ('active', "Active")
    INACTIVE = ('inactive', "Inactive")


class ResumeGenderChoices(models.TextChoices):
    MALE = ('male', "Male")
    FEMALE = ('female', "Female")


class ResumeEducationChoices(models.TextChoices):
    AVERAGE = ("average", "Average")
    SPECIALIZED = ("specialized secondary", "Specialized secondary")
    SECONDARY = ("incomplete higher education", "Incomplete higher education")
    HIGHER = ("higher", "Higher")
    EDUCATION = ("bachelor", "Bachelor")
    MASTER = ("master", "Master")
    PHD = ("phd", "PhD")
    PHD2 = ("ph.d", "Ph.D")
