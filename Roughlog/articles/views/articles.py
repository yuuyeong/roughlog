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
        return render(
            request,
            "articles/list.html",
            context={},
        )
