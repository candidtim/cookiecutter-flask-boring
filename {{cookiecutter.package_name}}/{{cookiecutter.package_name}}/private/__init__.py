from flask import Blueprint
from flask import current_app as app

bp = Blueprint("private", __name__, template_folder="templates", url_prefix="/private")
