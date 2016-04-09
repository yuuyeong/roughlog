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

    follower_set = models.ManyToManyField(
        "self",
        symmetrical=False,
        related_name="followee_set",
        through="Follow",
        through_fields=("followee", "follower")
    )

    def __str__(self):
        return "{name}".format(name=self.username)
