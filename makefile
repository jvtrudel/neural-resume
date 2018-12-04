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
	docker network rm $(docker network ls -q)
	docker rm $(shell docker ps -aq) ;\
	docker rmi $(shell docker images -q)

reset-db:
	rm -f resume/migrations/00*.py
	rm -rf resume/migrations/__pycache__
	docker-compose run web ./manage.py makemigrations
	docker-compose run web ./manage.py migrate
	docker-compose run web python manage.py shell -c "from django.contrib.auth.models import User; User.objects.create_superuser('admin', 'admin@example.com', '1234')"
# docker-compose run web ./manage.py loaddata resume/migrations/fixtures/dev_data.json

reset:
	docker-compose down
	docker-compose up --force-recreate &
	sleep 10
	rm -f resume/migrations/00*.py
	rm -rf resume/migrations/__pycache__
	docker-compose run web ./manage.py makemigrations
	docker-compose run web ./manage.py migrate
	docker-compose run web python manage.py shell -c "from django.contrib.auth.models import User; User.objects.create_superuser('admin', 'admin@example.com', '1234')"
	docker-compose run web ./manage.py loaddata fixtures/db.json
