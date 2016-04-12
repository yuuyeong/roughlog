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

    time_added = models.IntegerField()

    time_updated = models.IntegerField()

    def __str__(self):
        return "{name} saved {title}".format(
            name=self.user.nickname,
            title=self.article.title,
        )
