.EXPORT_ALL_VARIABLES:

UGID=$(shell id -u):$(shell id -u)


up:
	docker-compose up &

django-shell:
	docker-compose run web python manage.py shell

shell:
	docker-compose run web sh

wipe-dockers:
# Un peu trop violent...
# todo: détruire uniquement le projet courant
	docker stop $(shell docker ps -aq) ;\
	docker rm $(shell docker ps -aq) ;\
	docker rmi $(shell docker images -q)

init-db:
	docker-compose run web ./manage.py makemigrations
	docker-compose run web ./manage.py migrate
	docker-compose run web ./manage.py loaddata resume/migrations/fixtures/dev_data.json


