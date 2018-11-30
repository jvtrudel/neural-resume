.EXPORT_ALL_VARIABLES:

UGID=$(shell id -u):$(shell id -u)


up:
	docker-compose up &

django-shell:
	docker-compose run web python manage.py shell

shell:
	docker-compose run web sh

wipe-docker:
	docker stop $(docker ps -aq) ;\
	docker rm $(docker ps -aq) ;\
	docker rmi $(docker images -q)

