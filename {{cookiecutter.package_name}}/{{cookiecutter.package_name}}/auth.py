import urllib.parse

from flask import Blueprint, abort
from flask import current_app as app
from flask import g, redirect, url_for
{%- if cookiecutter.auth == "auth0" %}
from flask_dance.consumer import OAuth2ConsumerBlueprint, oauth_authorized
from flask_dance.consumer.storage.sqla import OAuthConsumerMixin, SQLAlchemyStorage
{%- endif %}
from flask_login import (
    LoginManager,
    UserMixin,
    current_user,
    login_required,
    login_user,
    logout_user,
)
from sqlalchemy.orm.exc import NoResultFound

from .db import db
{%- if cookiecutter.auth == "auth0" %}

bp = OAuth2ConsumerBlueprint(
    "auth",
    __name__,
    scope="openid profile email",
    redirect_to="{{ cookiecutter.app_bp_name }}.index",
)
{%- else %}

bp = Blueprint("auth", __name__)
{%- endif %}

login_manager = LoginManager()


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(255), unique=True, nullable=False)
    username = db.Column(db.String(255), unique=True)
    {%- if cookiecutter.auth == "auth0" %}
    name = db.Column(db.String(255))
    first_name = db.Column(db.String(255))
    last_name = db.Column(db.String(255))
    picture = db.Column(db.String(255))
    locale = db.Column(db.String(255))
    {%- endif %}
    {%- if cookiecutter.with_admin == 'y' %}

    @property
    def is_admin(self):
        return self.email == app.config["ADMIN_EMAIL"]
    {%- endif %}

    def get_id(self):
        return str(self.id)
{%- if cookiecutter.auth == "auth0" %}


class OAuth(OAuthConsumerMixin, db.Model):
    user_id = db.Column(db.Integer, db.ForeignKey(User.id))
    user = db.relationship(User)
{%- endif %}


def init_app(app):
    # setup login manager
    login_manager.init_app(app)
    login_manager.login_view = "auth.login"
{%- if cookiecutter.auth == "auth0" %}

    # setup Auth0
    bp.from_config = {
        "client_id": "AUTH0_OAUTH_CLIENT_ID",
        "client_secret": "AUTH0_OAUTH_CLIENT_SECRET",
        "base_url": "AUTH0_BASE_URL",
        "token_url": "AUTH0_TOKEN_URL",
        "authorization_url": "AUTH0_AUTHORIZE_URL",
    }
    bp.storage = SQLAlchemyStorage(
        OAuth,
        db.session,
        user=lambda: current_user,
        user_required=True,
    )
{%- endif %}
    app.register_blueprint(bp, url_prefix="/auth")
{%- if cookiecutter.auth == "auth0" %}


@oauth_authorized.connect_via(bp)
def on_logged_in(blueprint, token):
    res = blueprint.session.get("userinfo")
    if res.ok:
        userinfo = res.json()
        email = userinfo["email"]
        query = db.select(User).filter_by(email=email)
        user = db.session.scalars(query).one_or_none()
        if not user:
            user = User(
                username=userinfo["nickname"],
                email=email,
                name=userinfo.get("name"),
                first_name=userinfo.get("given_name"),
                last_name=userinfo.get("family_name"),
                picture=userinfo.get("picture"),
                locale=userinfo.get("locale"),
            )
            db.session.add(user)
            db.session.commit()
        login_user(user=user)
    else:
        abort(res.status_code)
{%- endif %}


@login_manager.user_loader
def load_user(user_id: int) -> User:
    return db.session.get(User, user_id)
{%- if cookiecutter.auth == "flask-login" %}


@bp.route("/login")
def login():
    # TODO: login routine here
    user = None
    login_user(user)
{%- endif %}


@bp.route("/logout")
@login_required
def logout():
    # clear session:
    logout_user()
{%- if cookiecutter.auth == "auth0" %}

    # sign out from auth0:
    params = {
        "returnTo": url_for("{{ cookiecutter.index_bp_name }}.index", _external=True),
        "client_id": app.config["AUTH0_OAUTH_CLIENT_ID"],
    }
    logout_url = (
        app.config["AUTH0_BASE_URL"] + "/v2/logout?" + urllib.parse.urlencode(params)
    )
    return redirect(logout_url)
{%- endif %}
