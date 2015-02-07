from sqlalchemy_utils import UUIDType

from diilikone.extensions import db


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
        nullable=False
    )

    deal_group = db.relationship(
        'DealGroup',
        backref=db.backref(
            'deals',
            cascade='all, delete-orphan',
            passive_deletes=True
        )
    )

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

    def __repr__(self):
        return '<{cls} size={size!r}, salesperson={name!r}>'.format(
            cls=self.__class__.__name__,
            size=self.size,
            name=self.salesperson.name
        )
