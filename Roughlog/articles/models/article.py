from django.db import models


class Article(models.Model):
    item_id = models.CharField(
        max_length=20,
    )

    origin_url = models.URLField(
        max_length=250,
    )

    title = models.CharField(
        max_length=128,
    )

    content = models.TextField()

    status = models.BooleanField()
    favorite = models.BooleanField()

    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
