import logging

import stripe
from flask import abort
from flask import current_app as app
from flask import redirect, render_template, request, url_for
from flask_login import current_user, login_required

from . import bp
from .models import StripeCheckout, db


@bp.route("/")
@login_required
def checkout():
    return render_template("stripe/checkout.html")


@bp.route("/create", methods=["POST"])
@login_required
def new_checkout_session():
    try:
        line_item = {"price": app.config["STRIPE_PRICE_ID"], "quantity": 1}
        session = stripe.checkout.Session.create(
            line_items=[line_item],
            customer_email=current_user.email,
            mode="payment",
            success_url=url_for(".checkout_success", _external=True),
            cancel_url=url_for(".checkout_cancel", _external=True),
        )
    except Exception as e:
        logging.exception(f"Error creating checkout session: {e}")
        abort(500)

    checkout = StripeCheckout(user_id=current_user.id, checkout_session_id=session.id)
    db.session.add(checkout)
    db.session.commit()

    return redirect(session.url, code=303)


@bp.route("/success")
@login_required
def checkout_success():
    return render_template("stripe/success.html")


@bp.route("/cancel")
@login_required
def checkout_cancel():
    return redirect(url_for(".checkout"), code=303)


@bp.route("/webhook", methods=["POST"])
def stripe_webhook():
    event = get_stripe_event()

    if event["type"] == "checkout.session.completed":
        checkout_session = event["data"]["object"]

        query = db.select(StripeCheckout).filter_by(
            checkout_session_id=checkout_session["id"]
        )
        checkout = db.session.scalars(query).one()
        checkout.payment_intent_id = checkout_session["payment_intent"]
        checkout.paymet_status = checkout_session["payment_status"]
        db.session.commit()

    return "OK"


def get_stripe_event():
    """Get a Stripe event from a request."""
    payload = request.get_data(as_text=True)
    signature = request.headers.get("Stripe-Signature")
    try:
        return stripe.Webhook.construct_event(
            payload, signature, app.config["STRIPE_WEBHOOK_SECRET"]
        )
    except ValueError as e:
        logging.exception(f"Error constructing webhook event: {e}")
        abort(400)
    except stripe.error.SignatureVerificationError as e:
        logging.exception(f"Error verifying webhook signature: {e}")
        abort(400)
