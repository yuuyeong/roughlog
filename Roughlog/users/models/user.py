from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    nickname = models.CharField(
        max_length=12,
        unique=True,
        blank=True,
        null=True,
    )

    description = models.TextField()

    def __str__(self):
        return "{name}".format(name=self.username)
