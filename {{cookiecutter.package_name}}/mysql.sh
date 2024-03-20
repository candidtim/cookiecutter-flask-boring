#!/bin/bash

mkdir ./instance/mysql
docker run --name {{cookiecutter.package_name}}-mysql --rm \
  -v ./instance/mysql:/var/lib/mysql \
  -e MYSQL_ROOT_PASSWORD=dev -e MYSQL_DATABASE=dev -p 3306:3306 -it \
  docker.io/mysql:8.3
