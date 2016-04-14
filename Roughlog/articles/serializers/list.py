from articles.models import Pocket

from rest_framework import serializers


class PocketSerializer(serializers.ModelSerializer):
    article_id = serializers.CharField(source='article.pk')
    article_url = serializers.URLField(source='article.origin_url')
    article_title = serializers.CharField(source='article.title')
    article_excerpt = serializers.CharField(source='article.excerpt')
    article_img = serializers.URLField(source='article.img')

    class Meta:
        model = Pocket
        fields = (
            'item_id',
            'article_id',
            'article_url',
            'article_title',
            'article_excerpt',
            'article_img',
        )
