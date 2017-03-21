from decimal import Decimal

import sqlalchemy as sa
from flask.json import JSONEncoder
from flask_cors import CORS
from flask_login import LoginManager
from flask_mail import Mail
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_utils import force_auto_coercion

login_manager = LoginManager()
cors = CORS()
db = SQLAlchemy()
mail = Mail()


class CustomJSONEncoder(JSONEncoder):
    def default(self, obj):
        try:
            if isinstance(obj, Decimal):
                return float(obj)
            iterable = iter(obj)
        except TypeError:
            pass
        else:
            return list(iterable)
        return JSONEncoder.default(self, obj)


@login_manager.user_loader
def load_user(user_id):
    from .models.user import User
    return User.query.get(user_id)


# Assign automatic data type coercion.
# For example str representations of UUIDs
# are automatically coerced into UUID objects.
force_auto_coercion()


@sa.event.listens_for(db.metadata, 'before_create')
def create_postgres_extensions(target, connection, **kw):
    connection.execute('CREATE EXTENSION IF NOT EXISTS "uuid-ossp"')


@sa.event.listens_for(db.metadata, 'after_drop')
def drop_postgres_extensions(target, connection, **kw):
    connection.execute('DROP EXTENSION "uuid-ossp"')
