from django.db import models


class TimeStampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class User(TimeStampedModel):
    name = models.CharField(max_length=250)
    surename = models.CharField(max_length=200)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=50, blank=True)

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"

    def __str__(self):
        return f"{self.name, self.surename}"
