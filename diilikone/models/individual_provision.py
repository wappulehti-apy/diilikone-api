from sqlalchemy_utils import UUIDType

from diilikone.extensions import db


class IndividualProvision(db.Model):
    __tablename__ = 'individual_provision'

    id = db.Column(
        UUIDType(binary=False),
        server_default=db.func.uuid_generate_v4(),
        primary_key=True
    )

    quantity = db.Column(db.Integer, nullable=False)

    price_per_magazine = db.Column(
        db.Numeric(precision=3, scale=2),
        nullable=False
    )

    __table_args__ = (
        db.UniqueConstraint(
            'quantity',
            name='uq_provision_quantity',
            deferrable=True,
            initially='DEFERRED'
        ),
    )
