web: python Roughlog/manage.py runserver
celery: celery --workdir=Roughlog/ --app=Roughlog.celery:app worker
flower: celery --workdir=Roughlog/ --app=Roughlog.celery:app flower
