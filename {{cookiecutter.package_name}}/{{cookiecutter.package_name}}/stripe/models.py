from ..auth import User
from ..db import db


class StripeCheckout(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    user_id = db.Column(db.Integer, db.ForeignKey(User.id))
    user = db.relationship(User)

    checkout_session_id = db.Column(db.String(255), unique=True)
    payment_intent_id = db.Column(db.String(255), unique=True)
    paymet_status = db.Column(db.String(255))

    @property
    def is_paid(self):
        return self.paymet_status == "paid"
