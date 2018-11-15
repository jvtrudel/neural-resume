#!/bin/sh
# wait-for-postgres.sh
# simple script inspired from https://docs.docker.com/compose/startup-order/
#

set -e



if [ "$1" == "debug" ]; then
   shift
   echo "command: $@"
   echo "POSTGRES_PASSWORD:$POSTGRES_PASSWORD"
   echo "POSTGRES_DB:$POSTGRES_DB"
   echo "POSTGRES_USER:$POSTGRES_USER"
fi



cmd="$@"
until PGPASSWORD=$POSTGRES_PASSWORD psql -h "$POSTGRES_DB" -U "$POSTGRES_USER" -c '\q'; do
    >&2 echo "Postgres is unavailable - sleeping"
    sleep 1
done

>&2 echo "Postgres is up - executing command"
exec $cmd

