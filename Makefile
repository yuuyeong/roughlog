migrate:
	python Roughlog/manage.py makemigrations users posts django_summernote
	python Roughlog/manage.py migrate
