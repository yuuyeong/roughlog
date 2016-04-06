from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    description = models.TextField()

    def __str__(self):
        return "{name}".format(name=self.username)
