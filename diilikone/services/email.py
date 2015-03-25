from flask import render_template
from flask_mail import Message

from diilikone.extensions import mail
from diilikone.models import Deal, IndividualProvision, GroupProvision


def send_confirmation_email(deal):
    msg = Message(
        subject='Tervetuloa Äpy-myyjäksi!',
        sender=("Äpy", "diilit@apy.fi"),
        recipients=[deal.salesperson.email],
        charset="utf8",
        bcc=["diilit@apy.fi"]
    )

    provision = IndividualProvision.query.filter_by(quantity=deal.size).one()


    group_provision = GroupProvision.query.filter_by(
        quantity=deal.deal_group.total_size
    ).first()

    msg.body = render_template(
        'confirmation_email.txt',
        deal=deal,
        provision=provision,
        group_provision=group_provision
    )

    mail.send(msg)
    return True
