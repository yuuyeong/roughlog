import requests

from django.http import HttpResponse
from django.views.generic import View


class ArticleListView(View):
	template_name_name = "articles/list.html"

	def get(self, request):
		user = request.user.social_auth.filter(
			provider='pocket',
		).first()
		url = "https://getpocket.com/v3/get"

		if user:
			response = requests.post(
				url,
				data = {
					"consumer_key": "",
					"access_token": user.extra_data['access_token'],
				},
				headers = {"X-Accept": "application/json"}
			)

			return HttpResponse(
				response,
				content_type="application/json"
			)
		return HttpResponse(
				json.dumps([]),
				content_type="application/json"
			)
