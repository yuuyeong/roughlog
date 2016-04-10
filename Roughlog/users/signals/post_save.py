import json
import requests

from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver

from users.models import User
from articles.models import Article, PocketTag, Pocket
from Roughlog.models import Image
from social.apps.django_app.default.models import UserSocialAuth


@receiver(post_save, sender=User)
def get_user_articles(sender, instance, created, **kwargs):
    if not instance.nickname:
        return
    # pocket api를 이용해 json으로 정보를 받아온다
    user = UserSocialAuth.objects.get(uid=instance.username)
    url = "https://getpocket.com/v3/get"

    if user:
        response = requests.post(
            url,
            data={
                "consumer_key": settings.SOCIAL_AUTH_POCKET_KEY,
                "access_token": user.extra_data['access_token'],
                # "state": "archive",
                "detailType": "complete",
            },
            headers={"X-Accept": "application/json"}
        )
        dict_file = json.loads(response.text)

    # json 파싱해서 article 모델로 저장
    if dict_file:
        for article in [val for key, val in dict_file['list'].items()]:
            new_article = Article.objects.create(
                origin_url=article.get('resolved_url'),
                title=article.get('resolved_title'),
                excerpt=article.get('excerpt'),
                status=bool(article.get('status')),
                favorite=bool(article.get('favorite')),
            )

            pocket = Pocket.objects.create(
                user=instance,
                article=new_article,
                item_id=article.get('item_id'),
            )

            if article.get('images'):
                # from IPython import embed; embed()
                for img_info in [
                    {'src': val.get('src'), 'caption': val.get('caption')}
                    for key, val
                    in article.get('images').items()
                ]:
                    Image.objects.create(
                        article=new_article,
                        img_url=img_info.get('src'),
                        caption=img_info.get('caption'),
                    )

            if article.get('tags'):
                # from IPython import embed; embed()
                for tag_name in [key for key in article.get('tags')]:
                    tag, is_created = PocketTag.objects.get_or_create(
                        name=tag_name,
                    )
                    pocket.tag_set.add(tag)
