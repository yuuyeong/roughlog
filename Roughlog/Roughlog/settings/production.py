import os
import raven

from .partial import *


DEBUG = False

ALLOWED_HOSTS = [
    "*",
]

INSTALLED_APPS += [
    'raven.contrib.django.raven_compat',
]

STATICFILES_STORAGE = 'Roughlog.storage.S3PipelineCachedStorage'
DEFAULT_FILE_STORAGE = 'storages.backends.s3boto.S3BotoStorage'

AWS_ACCESS_KEY_ID = os.environ.get("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY = os.environ.get("AWS_SECRET_ACCESS_KEY")
AWS_STORAGE_BUCKET_NAME = os.environ.get("AWS_STORAGE_BUCKET_NAME")

AWS_S3_CUSTOM_DOMAIN = 'd1ozx5abd8asoc.cloudfront.net'
AWS_S3_URL_PROTOCOL = 'https'
AWS_S3_HOST = "s3-ap-northeast-1.amazonaws.com"

STATIC_URL = "https://d1ozx5abd8asoc.cloudfront.net/"

RAVEN_CONFIG = {
    'dsn': 'https://d0c257bd6f814935aa305e8c6054a058:ae34253937ba44348e249756c01c7c84@app.getsentry.com/74131',
}
