from django.db import models

from articles.models import Article


class Image(models.Model):
    article = models.ForeignKey(
        Article,
    )

    img_url = models.URLField()

    caption = models.CharField(
        max_length=255,
        blank=True,
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
    )

    updated_at = models.DateTimeField(
        auto_now=True,
    )
