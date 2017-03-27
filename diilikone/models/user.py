from flask_login import UserMixin
from sqlalchemy_utils import EmailType, PasswordType, UUIDType

from diilikone.extensions import db


class User(db.Model, UserMixin):
    __tablename__ = 'user'

    id = db.Column(
        UUIDType(binary=False),
        server_default=db.func.uuid_generate_v4(),
        primary_key=True
    )

    email = db.Column(EmailType(255), nullable=False, unique=True)

    first_name = db.Column(db.Unicode(255), nullable=False)

    last_name = db.Column(db.Unicode(255), nullable=False)

    guild = db.Column(db.Unicode(100), nullable=True)

    class_year = db.Column(db.Unicode(1), nullable=True)

    phone_number = db.Column(db.Unicode(20), nullable=True)

    signed_at = db.Column(db.DateTime, nullable=True)

    password = db.Column(PasswordType(128, schemes=['sha512_crypt']))

    @property
    def name(self):
        return '{0} {1}'.format(self.first_name, self.last_name)

    def __repr__(self):
        return '<{cls} name={name!r}>'.format(
            cls=self.__class__.__name__,
            name=self.name
        )

    def __str__(self):
        return '{name}'.format(
            name=self.name
        )
