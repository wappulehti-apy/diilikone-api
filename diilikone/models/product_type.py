from sqlalchemy_utils import UUIDType

from diilikone.extensions import db


class ProductType(db.Model):
    __tablename__ = 'product_type'

    id = db.Column(
        UUIDType(binary=False),
        server_default=db.func.uuid_generate_v4(),
        primary_key=True
    )

    name = db.Column(db.Unicode(255), nullable=False)

    price = db.Column(
        db.Numeric(scale=2),
        nullable=False
    )

    stock = db.Column(db.Integer, nullable=False)

    @property
    def left_in_stock(self):
        return self.stock - len(self.deals)

    def __repr__(self):
        return '<{cls} name={name!r}, price={price!r}>'.format(
            cls=self.__class__.__name__,
            price=self.price,
            name=self.name
        )
