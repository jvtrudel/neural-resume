# Development shortcuts

up:
	./bin/up.dev &

down:
	docker-compose down

reset-migration:
	./bin/reset-migration.dev

migrate:
	./bin/migrate.dev

shell:
	./bin/shell.dev

dumpdata:
	./bin/dumpdata.dev
loaddata:
	./bin/loaddata.dev


wipe-docker:
	./bin/wipe-docker.dev
