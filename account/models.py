from django.contrib.auth.models import AbstractUser
from django.db import models


class Profile(AbstractUser):
    is_author = models.BooleanField(default=False)
