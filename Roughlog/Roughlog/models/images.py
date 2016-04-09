from django.db import models

from articles.models import Article


class Image(models.Model):
    article = models.ForeignKey(
        Article,
    )

    name = models.ImageField()
