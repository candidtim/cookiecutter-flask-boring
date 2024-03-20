import random
import string

from flask import redirect, render_template, url_for
from flask_login import current_user, login_required

from . import bp
from .models import Data, db


@bp.route("/")
@login_required
def index():
    query = db.select(Data).filter_by(user_id=current_user.id)
    data = db.session.scalars(query).all()
    return render_template("private/index.html", data=data)


@bp.route("/add-data", methods=["POST"])
@login_required
def add_data():
    text = "".join(random.choice(string.ascii_lowercase) for i in range(12))
    data = Data(user_id=current_user.id, text=text)
    db.session.add(data)
    db.session.commit()
    return redirect(url_for("private.index"))


@bp.route("/add-data-htmx", methods=["POST"])
@login_required
def add_data_htmx():
    text = "".join(random.choice(string.ascii_lowercase) for i in range(12))
    data = Data(user_id=current_user.id, text=text)
    db.session.add(data)
    db.session.commit()
    return render_template("private/added-data.html", data=data)
