import json
import requests

from django.conf import settings

from social.apps.django_app.default.models import UserSocialAuth
from articles.models import Article, Pocket


class JsonDataParser(object):
    def __init__(self, user, url):
        self.url = url
        self.user = user

    def run(self):
        self._get_json_data()
        if self.user.since:
            self._retrieve_modify_articles()
        else:
            self._retrieve_all_articles()
        self._save_since()

    def _retrieve_modify_articles(self):
        data = self.json_data['list']
        if len(data):
            for article in [val for key, val in data.items()]:
                status = article.get('status')
                # from IPython import embed; embed()
                if status is '0':
                    # article 추가
                    new_article = self._save_article_data(article)
                    if new_article:
                        pocket = self._save_pocket_data(
                            new_article,
                            article.get('item_id'),
                            article.get('time_added'),
                            article.get('time_updated'),
                        )

                elif status is '2':
                    # article 삭제
                    item_id = article.get('item_id')

                    if item_id:
                        pocket = Pocket.objects.get(item_id=item_id)
                        pocket_num = pocket.article.pocket_set.count()
                        if pocket_num < 2:
                            # 삭제
                            pocket.article.delete()
                            pocket.delete()

    def _retrieve_all_articles(self):
        data = self.json_data['list']
        if len(data):
            for article in [val for key, val in data.items()]:
                new_article = self._save_article_data(article)
                if new_article:
                    pocket = self._save_pocket_data(
                        new_article,
                        article.get('item_id'),
                        article.get('time_added'),
                        article.get('time_updated'),
                    )

    def _get_json_data(self):
        # socail auth의 유저정보 받아오기
        user = UserSocialAuth.objects.get(uid=self.user.username)
        extra_data = json.loads(user.extra_data)
        # from IPython import embed;embed()
        data = {
            "consumer_key": settings.SOCIAL_AUTH_POCKET_KEY,
            "access_token": extra_data.get('access_token'),
            "detailType": "complete",
        }

        if self.user.since:
            data["since"] = str(self.user.since)

        response = requests.post(
            self.url,
            data,
            headers={"X-Accept": "application/json"}
        )
        self.json_data = json.loads(response.text)

    def _save_article_data(self, article):
        if article.get('is_article') is '0':
            return

        img_url = self._get_img_url(article.get('image'))
        new_article, is_created = Article.objects.get_or_create(
            origin_url=article.get('resolved_url'),
        )
        if is_created:
            new_article.title = article.get('resolved_title')
            new_article.excerpt = article.get('excerpt')
            new_article.img = img_url
            new_article.status = bool(int(article.get('status')))
            new_article.favorite = bool(int(article.get('favorite')))
            new_article.save()
        return new_article

    def _get_img_url(self, img_data):
        img_url = ""
        if img_data:
            for key, val in img_data.items():
                if key == "src":
                    img_url = val
                    break
        return img_url

    def _save_pocket_data(self, article, item_id, time_added, time_updated):
        pocket = Pocket.objects.create(
            user=self.user,
            article=article,
            item_id=item_id,
            time_added=time_added,
            time_updated=time_updated,
        )
        return pocket

    def _save_since(self):
        self.user.since = self.json_data.get('since')
        self.user.save()
