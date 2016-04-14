web: python Roughlog/manage.py runserver 0.0.0.0:8000 --settings=Roughlog.settings.production
celery: celery --workdir=Roughlog/ --app=Roughlog.celery:app worker
flower: celery --workdir=Roughlog/ --app=Roughlog.celery:app flower
