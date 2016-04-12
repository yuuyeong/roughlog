from django.apps import AppConfig


class UserAppConfig(AppConfig):
    name = "users"

    def ready(self):
        from users.signals import get_user_articles
