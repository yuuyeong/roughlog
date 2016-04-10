from django.db import models
from django.conf import settings


class Article(models.Model):
    origin_url = models.URLField(
        max_length=250,
    )

    title = models.CharField(
        max_length=128,
    )

    excerpt = models.TextField()

    status = models.BooleanField()

    favorite = models.BooleanField()

    created_at = models.DateTimeField(
        auto_now_add=True,
    )

    updated_at = models.DateTimeField(
        auto_now=True,
    )
