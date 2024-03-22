from flask import render_template, abort

from . import bp


@bp.route("/")
def index():
    return render_template("{{ cookiecutter.index_bp_name }}/index.html")


@bp.route("/error")
def error():
    abort(500)
