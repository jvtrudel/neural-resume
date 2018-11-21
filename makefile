# Development shortcuts

up:
	./bin/up.dev &

down:
	docker-compose down

reset-migration:
	./bin/reset-migration.dev

shell:
	export UID=${UID};export UID=${UID}; docker-compose run web sh

dumpdata:
	./bin/dumpdata.dev
loaddata:
	./bin/loaddata.dev


wipe-docker:
	./bin/wipe-docker.dev
