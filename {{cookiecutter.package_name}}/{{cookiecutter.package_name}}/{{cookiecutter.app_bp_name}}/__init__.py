from flask import Blueprint
from flask import current_app as app

bp = Blueprint("{{cookiecutter.app_bp_name}}", __name__, template_folder="templates", url_prefix="/{{ cookiecutter.app_bp_name }}")
