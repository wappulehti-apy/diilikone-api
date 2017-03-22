from sqlalchemy_utils import UUIDType

from diilikone.extensions import db


class DealGroup(db.Model):
    __tablename__ = 'deal_group'

    id = db.Column(
        UUIDType(binary=False),
        server_default=db.func.uuid_generate_v4(),
        primary_key=True
    )

    name = db.Column(db.Unicode(255), nullable=False)

    frozen_magazine_amount = db.Column(db.Integer, nullable=True)

    owner_id = db.Column(
        UUIDType,
        db.ForeignKey('user.id', ondelete='RESTRICT'),
        index=True,
        nullable=False,
        unique=True
    )

    percentage = db.Column(
        db.Integer,
        nullable=False,
        default=0,
        server_default='0'
    )

    owner = db.relationship('User')

    @property
    def total_size(self):
        sizes = [deal.size for deal in self.deals]
        return sum(sizes)

    def __repr__(self):
        return '<{cls} name={name!r}>'.format(
            cls=self.__class__.__name__,
            name=self.name
        )
