from django.contrib.auth.models import AbstractUser
from django.db import models


class Profile(AbstractUser):
    is_author = models.BooleanField(default=False)
    date_of_birth = models.DateField(null=True, blank=True)
    school = models.CharField(max_length=255, null=True, blank=True)
    profile_pic = models.ImageField(upload_to='profiles/', null=True, blank=True)

    @property
    def full_name(self):
        return self.first_name + ' ' + self.last_name if self.last_name else self.first_name
