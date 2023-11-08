from django.contrib.auth.base_user import AbstractBaseUser
# from django.contrib.auth.models import UserManager
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.db import models
from django.contrib.auth.models import PermissionsMixin
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django.core.cache import cache
from apps.users.manager import UserManager
from apps.users.validators import CustomEmailValidator


# employee
# employeer
# user


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(validators=[CustomEmailValidator()])

    first_name = models.CharField(
        _("first_name"),
        max_length=150,
        help_text=_(
            "Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only."
        ),
    )
    last_name = models.CharField(max_length=150)
    username = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=13)
    email = models.EmailField(_("email address"), blank=True, unique=True)
    password = models.CharField(max_length=250)
    employer = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    is_verified = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    EMAIL_FIELD = "email"
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

    class Meta:
        verbose_name = _("user")
        verbose_name_plural = _("users")

    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"


def getKey(key):
    return cache.get(key)


def setKey(key, value, timeout):
    cache.set(key, value, timeout)


class Employer(models.Model):
    company = models.CharField(max_length=150, unique=True)
    location = models.CharField(max_length=150)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="user_employer")


