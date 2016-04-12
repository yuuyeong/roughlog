migrate:
	python Roughlog/manage.py makemigrations users posts tags articles Roughlog django_summernote
	python Roughlog/manage.py migrate
