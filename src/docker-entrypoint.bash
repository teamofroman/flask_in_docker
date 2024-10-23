#!/bin/bash

set -e

while ! nc -z ${POSTGRES_SERVER} ${POSTGRES_PORT}; do
  echo "Waiting for postgres to start..."
  sleep 3
done
echo "Postgres started"

flask db upgrade

gunicorn main:app -b 0.0.0.0:5000
