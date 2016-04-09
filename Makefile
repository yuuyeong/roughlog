migrate:
	python Roughlog/manage.py makemigrations users posts tags django_summernote
	python Roughlog/manage.py migrate
