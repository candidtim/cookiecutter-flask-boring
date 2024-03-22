from flask import Flask

from {{cookiecutter.package_name}} import auth, db, errors
{%- if cookiecutter.static_files == 'webpack' %}
from {{cookiecutter.package_name}} import assets{% endif %}
{%- if cookiecutter.with_admin == 'y' %}
from {{cookiecutter.package_name}} import admin{% endif %}
{%- if cookiecutter.with_stripe == 'y' %}
from {{cookiecutter.package_name}} import stripe{% endif %}
from {{cookiecutter.package_name}}.logging import init_logging
from {{cookiecutter.package_name}}.{{ cookiecutter.app_bp_name }}.views import bp as {{ cookiecutter.app_bp_name }}_bp
from {{cookiecutter.package_name}}.{{ cookiecutter.index_bp_name }}.views import bp as {{ cookiecutter.index_bp_name }}_bp


def create_app(config_overrides=None):
    init_logging()  # should be configured before any access to app.logger

    Flask.jinja_options["line_statement_prefix"] = "#"
    app = Flask(__name__)

    app.config.from_object("{{cookiecutter.package_name}}.defaults")
    app.config.from_prefixed_env()

    if config_overrides is not None:
        app.config.from_mapping(config_overrides)

    db.init_app(app)
    auth.init_app(app)
    errors.init_app(app)
    {%- if cookiecutter.static_files == 'webpack' %}
    assets.init_app(app){% endif %}
    {%- if cookiecutter.with_admin == 'y' %}
    admin.init_app(app){% endif %}
    {%- if cookiecutter.with_stripe == 'y' %}
    stripe.init_app(app){% endif %}

    app.register_blueprint({{ cookiecutter.index_bp_name }}_bp)
    app.register_blueprint({{ cookiecutter.app_bp_name }}_bp)

    return app
