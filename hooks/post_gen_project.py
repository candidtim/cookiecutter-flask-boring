import shutil
import os

REMOVE_PATHS = [
    '{% if cookiecutter.use_flake8 != "y" %} setup.cfg {% endif %}',
    '{% if cookiecutter.use_poetry == "y" %} setup.py {% endif %}',
    '{% if cookiecutter.use_poetry == "y" %} Makefile {% endif %}',
    '{% if cookiecutter.static_files != "webpack" %} assets/ {% endif %}',
    '{% if cookiecutter.static_files != "webpack" %} {{ cookiecutter.package_name }}/assets.py {% endif %}',
    '{% if cookiecutter.static_files == "webpack" %} {{ cookiecutter.package_name }}/static/styles.css {% endif %}',
    '{% if cookiecutter.static_files == "webpack" %} {{ cookiecutter.package_name }}/static/main.js {% endif %}',
    '{% if cookiecutter.db == "sqlite" %} db.sh {% endif %}',
    '{% if cookiecutter.with_admin != "y" %} {{ cookiecutter.package_name }}/admin.py {% endif %}',
    '{% if cookiecutter.with_stripe != "y" %} {{ cookiecutter.package_name }}/stripe {% endif %}',
    '{% if cookiecutter.use_htmx != "y" %} {{ cookiecutter.package_name }}/{{ cookiecutter.app_bp_name }}/templates/{{ cookiecutter.app_bp_name }}/added-data.html {% endif %}',
]

for path in REMOVE_PATHS:
    path = path.strip()
    if path and os.path.exists(path):
        if os.path.isdir(path):
            shutil.rmtree(path)
        else:
            os.unlink(path)

shutil.copyfile(".env.example", ".env")

{% if cookiecutter.use_poetry == "y" %}
os.system(
    "poetry install && "
    "poetry run flask db init && "
    "poetry run flask db migrate -m 'Initial version'"
)
{% elif cookiecutter.use_pipenv == "y" %}
{% else %}
os.system(
    "make venv && "
    "./venv/bin/flask db init && "
    "./venv/bin/flask db migrate -m 'Initial version'"
)
{% endif %}

{% if cookiecutter.static_files == "webpack" %}
os.system("cd assets && npm install && npm run dev")
{% endif %}
