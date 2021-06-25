from django.contrib.auth.models import AbstractUser
from django.db import models


class Profile(AbstractUser):
    is_author = models.BooleanField(default=False)
    date_of_birth = models.DateField(null=True, blank=True)
    school = models.CharField(max_length=255, null=True, blank=True)
    profile_pic = models.ImageField(upload_to='profiles/', null=True, blank=True, default='profiles/default.png')

    @property
    def full_name(self):
        full = []
        if self.first_name:
            full.append(self.first_name)
            if self.last_name:
                full.append(self.last_name)
        else:
            full.append(self.username)
        return " ".join(full)
