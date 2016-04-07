import json
import requests

from django.http import HttpResponse
from django.core.urlresolvers import reverse
from django.shortcuts import render, redirect
from django.conf import settings
from django.http import HttpResponse
from django.views.generic import View

from social.apps.django_app.default.models import UserSocialAuth


class ArticleListView(View):

    def get(self, request):
        dict_file = self.get_json_file(request.user)
        lists = [
            # [ value.get('excerpt'), value.get('resolved_title'), value.get('resolved_url')]
            value
            for key, value
            in dict_file['list'].items()
        ]
        # from IPython import embed; embed()
        return render(
            request,
            "articles/list.html",
            context={
                'lists': lists,
            },
        )

    def get_json_file(self, user_object):
        user = UserSocialAuth.objects.get(uid=user_object.username)
        url = "https://getpocket.com/v3/get"

        if user:
            response = requests.post(
                url,
                data={
                    "consumer_key": settings.SOCIAL_AUTH_POCKET_KEY,
                    "access_token": user.extra_data['access_token'],
                    "state": "unread",
                },
                headers={"X-Accept": "application/json"}
            )

            return json.loads(
                response.text
            )
        return {}
