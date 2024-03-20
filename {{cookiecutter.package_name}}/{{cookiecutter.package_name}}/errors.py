from flask import render_template
from werkzeug.exceptions import HTTPException


def init_app(app):
    app.register_error_handler(HTTPException, handle_error)


def handle_error(error):
    return render_template("error.html", error=error), error.code
