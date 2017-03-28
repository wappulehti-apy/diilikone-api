# -*- coding: utf-8 -*-
from flask import render_template
from flask_mail import Message

from diilikone.extensions import mail
from diilikone.models import GroupProvision, IndividualProvision


def _calculateIndividualProvision(deal):
    provision = IndividualProvision.query.filter_by(quantity=deal.size).one()
    base = provision.price_per_magazine
    for product in deal.product_types:
        base -= product.price / deal.size
    return round(base, 2)


def _get_group_provision(group):
    if group:
        group_provision = GroupProvision.query.filter_by(
            quantity=group.total_size
        ).first()
        return group_provision.price_per_magazine
    else:
        return 0


def send_confirmation_email(deal):
    msg = Message(
        subject='Tervetuloa Äpy-myyjäksi!',
        sender=("Äpy", "diilit@apy.fi"),
        recipients=[deal.salesperson.email],
        charset="utf8",
        bcc=["diilit@apy.fi"]
    )

    msg.body = render_template('confirmation_email.txt', deal=deal)

    mail.send(msg)
    return True
