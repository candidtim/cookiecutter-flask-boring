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
    '{% if cookiecutter.db != "mysql" %} mysql.sh {% endif %}',
    '{% if cookiecutter.with_admin != "y" %} {{ cookiecutter.package_name }}/admin.py {% endif %}',
    '{% if cookiecutter.with_stripe != "y" %} {{ cookiecutter.package_name }}/stripe {% endif %}',
    '{% if cookiecutter.use_htmx != "y" %} {{ cookiecutter.package_name }}/private/templates/private/added-data.html {% endif %}',
]

for path in REMOVE_PATHS:
    path = path.strip()
    if path and os.path.exists(path):
        if os.path.isdir(path):
            shutil.rmtree(path)
        else:
            os.unlink(path)
