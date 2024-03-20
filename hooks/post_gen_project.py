import os

REMOVE_PATHS = [
    '{% if cookiecutter.use_flake8 != "y" %} setup.cfg {% endif %}',
    '{% if cookiecutter.use_poetry == "y" %} setup.py {% endif %}',
    '{% if cookiecutter.use_poetry == "y" %} Makefile {% endif %}',

    '{% if cookiecutter.static_files == "webpack" %} assets/src/index.js {% endif %}',
    '{% if cookiecutter.static_files == "webpack" %} assets/src/styles.scss {% endif %}',
    '{% if cookiecutter.static_files == "webpack" %} assets/src/ {% endif %}',
    '{% if cookiecutter.static_files == "webpack" %} assets/package.json {% endif %}',
    '{% if cookiecutter.static_files == "webpack" %} assets/webpack.config.js {% endif %}',
    '{% if cookiecutter.static_files == "webpack" %} assets/ {% endif %}',
    '{% if cookiecutter.static_files == "webpack" %} static/styles.css {% endif %}',
    '{% if cookiecutter.db != "mysql" %} mysql.sh {% endif %}',
]

for path in REMOVE_PATHS:
    path = path.strip()
    if path and os.path.exists(path):
        if os.path.isdir(path):
            os.rmdir(path)
        else:
            os.unlink(path)
