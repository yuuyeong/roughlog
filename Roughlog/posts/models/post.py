from django.conf import settings
from django.db import models

from tags.models import Tag


class Post(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
    )

    title = models.CharField(
        max_length=30,
    )

    content = models.TextField()

    article = models.URLField(
        max_length=250,
    )

    tag_set = models.ManyToManyField(
        Tag,
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
    )

    updated_at = models.DateTimeField(
        auto_now=True,
    )

    def get_absolute_url(self):
        from django.core.urlresolvers import reverse
        return reverse(
            "post-detail",
            kwargs={
                "pk": self.pk,
            },
        )
