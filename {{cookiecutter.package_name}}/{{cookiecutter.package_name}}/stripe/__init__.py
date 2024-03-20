import stripe
from flask import Blueprint
from flask import current_app as app

bp = Blueprint("stripe", __name__, template_folder="templates", url_prefix="/checkout")


def init_app(app):
    from . import views

    stripe.api_key = app.config["STRIPE_SECRET_KEY"]
    app.register_blueprint(bp)
