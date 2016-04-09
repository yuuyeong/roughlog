from django.db import models


class ArticleTag(models.Model):
    article = models.ForeignKey(
        "Article",
    )

    name = models.CharField(
        max_length=15,
    )
