from django.contrib.auth.models import AbstractUser
from django.db import models


class Profile(AbstractUser):
    is_author = models.BooleanField(default=False)
    date_of_birth = models.DateField(null=True, blank=True)
    school = models.CharField(max_length=255, null=True, blank=True)
