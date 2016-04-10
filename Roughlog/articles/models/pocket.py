from django.conf import settings
from django.db import models


class Pocket(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
    )

    article = models.ForeignKey(
        "Article",
    )

    item_id = models.CharField(
        max_length=20,
    )

    tag_set = models.ManyToManyField(
        "PocketTag",
        related_name="pocket_set"
    )

    def __str__(self):
        return "{user} saved {title}".format(
            user=user.nickname,
            title=article.title,
        )
