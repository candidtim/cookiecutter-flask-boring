#!/bin/bash
{%- if cookiecutter.db == 'mysql' %}

mkdir -p ./instance/mysqldata
docker run --name {{cookiecutter.package_name}}-mysql -d \
  -v ./instance/mysqldata:/var/lib/mysql \
  -e MYSQL_ROOT_PASSWORD=dev -e MYSQL_DATABASE=dev \
  -p 3306:3306 -it \
  docker.io/mysql:latest
{%- endif %}
{%- if cookiecutter.db == 'postgres' %}

mkdir -p ./instance/pgdata
docker run --name {{cookiecutter.package_name}}-postgres -d \
  -v ./instance/pgdata:/var/lib/postgresql/data \
  -e POSTGRES_USER=dev -e POSTGRES_PASSWORD=dev \
  -p 5432:5432 \
  docker.io/postgres:latest
{%- endif %}
