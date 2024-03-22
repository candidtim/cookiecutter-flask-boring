from ..auth import User
from ..db import db


class Data(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    user_id = db.Column(db.Integer, db.ForeignKey(User.id))
    user = db.relationship(User)

    text = db.Column(db.String(255))
