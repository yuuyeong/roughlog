from celery import Task

from articles.utils import JsonDataParser


class ArticlesCreateTask(Task):
    def run(self, user, url):
        parser = JsonDataParser(user, url)
        parser.run()
