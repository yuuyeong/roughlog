from django.contrib.auth.signals import user_logged_in
from django.dispatch import receiver

from articles.tasks import ArticlesCreateTask


@receiver(user_logged_in)
def get_user_articles(sender, user, request, **kwargs):
    url = "https://getpocket.com/v3/get"
    init_article = ArticlesCreateTask()
    init_article.delay(user, url)
