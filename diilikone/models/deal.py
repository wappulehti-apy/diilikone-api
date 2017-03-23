from datetime import datetime

from sqlalchemy_utils import UUIDType

from diilikone.extensions import db

deal_product_type = db.Table(
    'deal_product_type',
    db.Column(
        'deal_id',
        UUIDType(binary=False),
        db.ForeignKey('deal.id', ondelete='cascade')
    ),
    db.Column(
        'product_type_id',
        UUIDType(binary=False),
        db.ForeignKey('product_type.id', ondelete='cascade')
    )
)


class Deal(db.Model):
    __tablename__ = 'deal'

    id = db.Column(
        UUIDType(binary=False),
        server_default=db.func.uuid_generate_v4(),
        primary_key=True
    )

    size = db.Column(db.Integer, nullable=False)

    deal_group_id = db.Column(
        UUIDType,
        db.ForeignKey('deal_group.id', ondelete='RESTRICT'),
        index=True,
        nullable=True
    )

    deal_group = db.relationship('DealGroup', backref=db.backref('deals'))

    salesperson_id = db.Column(
        UUIDType,
        db.ForeignKey('user.id', ondelete='RESTRICT'),
        index=True,
        nullable=False,
        unique=True
    )

    salesperson = db.relationship(
        'User',
        backref=db.backref(
            'deal',
            cascade='all, delete-orphan',
            uselist=False,
            passive_deletes=True
        )
    )

    product_types = db.relationship(
        'ProductType',
        secondary=deal_product_type,
        backref=db.backref('deals')
    )

    created_at = db.Column(
        db.DateTime,
        server_default=db.func.now(),
        default=datetime.now()
    )

    notes = db.Column(
        db.Unicode(255),
        nullable=True
    )

    shirt_received = db.Column(
        db.Boolean,
        default=False,
        server_default='f',
        nullable=False
    )

    backpack_received = db.Column(
        db.Boolean,
        default=False,
        server_default='f',
        nullable=False
    )

    magazines_received = db.Column(
        db.Integer,
        nullable=False,
        default=0,
        server_default='0'
    )

    def __repr__(self):
        return '<{cls} size={size!r}, salesperson={name!r}>'.format(
            cls=self.__class__.__name__,
            size=self.size,
            name=self.salesperson.name
        )
