from django.contrib import admin

from articles.models import Pocket


@admin.register(Pocket)
class PocketModelAdmin(admin.ModelAdmin):
    list_display = (
        'item_id',
        'user',
        'article',
    )
