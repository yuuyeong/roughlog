from django.db import models
from django.conf import settings


class Article(models.Model):
    origin_url = models.URLField(
        max_length=250,
    )

    title = models.CharField(
        max_length=128,
        blank=True,
    )

    excerpt = models.TextField()

    img = models.URLField(
        max_length=250,
        blank=True,
    )

    status = models.BooleanField(
        default=False,
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
    )

    updated_at = models.DateTimeField(
        auto_now=True,
    )
