.EXPORT_ALL_VARIABLES:

UID=$(shell id -u)
GID=$(shell id -u)

django-shell:
	docker-compose run web python manage.py shell

shell:
	docker-compose run web sh



