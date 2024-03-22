all: run

clean:
	rm -rf venv build dist .pytest_cache .mypy_cache *.egg-info

venv:
	python3 -m venv venv && \
		venv/bin/pip install --upgrade pip setuptools && \
		venv/bin/pip install --editable ".[dev]"

run: venv
	venv/bin/flask --app {{cookiecutter.package_name}} --debug run

{%- if cookiecutter.use_black == 'y' %}

format: venv
	venv/bin/black .{%- if cookiecutter.use_isort == 'y' %} && venv/bin/isort .{% endif %}

format-check: venv
	venv/bin/black --check .{%- if cookiecutter.use_isort == 'y' %} && venv/bin/isort --check .{% endif %}
{%- endif %}
{%- if cookiecutter.use_flake8 == 'y' %}

lint: venv
	venv/bin/flake8 .
{%- endif %}
{%- if cookiecutter.use_mypy == 'y' %}

mypy: venv
	venv/bin/mypy
{%- endif %}

test: venv
	venv/bin/pytest

dist: venv {% if cookiecutter.use_black == 'y' %}format-check {% endif %}{% if cookiecutter.use_flake8 == 'y' %}lint {% endif %}{% if cookiecutter.use_mypy == 'y' %}mypy {% endif %}test
	venv/bin/pip wheel --wheel-dir dist --no-deps .
{%- if cookiecutter.db == 'mysql' %}


db:
	mkdir -p ./instance/mysqldata && \
	docker run --name {{cookiecutter.package_name}}-mysql -d \
	  -v ./instance/mysqldata:/var/lib/mysql \
	  -e MYSQL_ROOT_PASSWORD=dev -e MYSQL_DATABASE=dev \
	  -p 3306:3306 -it \
	  docker.io/mysql:latest
{%- endif %}
{%- if cookiecutter.db == 'postgres' %}

db:
	mkdir -p ./instance/pgdata && \
	docker run --name {{cookiecutter.package_name}}-postgres -d \
	  -v ./instance/pgdata:/var/lib/postgresql/data \
	  -e POSTGRES_USER=dev -e POSTGRES_PASSWORD=dev \
	  -p 5432:5432 \
	  docker.io/postgres:latest
{%- endif %}
