from flask import Blueprint

bp = Blueprint("{{ cookiecutter.index_bp_name }}", __name__, template_folder="templates")
