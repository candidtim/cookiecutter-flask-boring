from flask import url_for, abort
from flask_admin import Admin, AdminIndexView
from flask_admin.contrib.sqla import ModelView
from flask_admin.menu import MenuLink
from flask_login import current_user

from .auth import User
from .db import db
from .private.models import Data
{%- if cookiecutter.with_stripe == 'y' %}
from .stripe.models import StripeCheckout
{%- endif %}


class SecureViewMixin:
    def is_accessible(self):
        return current_user.is_authenticated and current_user.is_admin

    def inaccessible_callback(self, name, **kwargs):
        return abort(404)


class SecureAdminIndexView(SecureViewMixin, AdminIndexView):
    pass


class SecureModelView(SecureViewMixin, ModelView):
    pass


admin = Admin(
    template_mode="bootstrap3",
    index_view=SecureAdminIndexView(),
)


def init_app(app):
    admin.init_app(app)
    admin.add_link(MenuLink(name="Home Page", url="/"))
    admin.add_view(SecureModelView(User, db.session))
    admin.add_view(SecureModelView(Data, db.session))
{%- if cookiecutter.with_stripe == 'y' %}
    admin.add_view(SecureModelView(StripeCheckout, db.session))
{%- endif %}
