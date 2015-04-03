import sqlalchemy as sa
from flask.ext.cors import CORS
from flask.ext.sqlalchemy import SQLAlchemy
from sqlalchemy_utils import force_auto_coercion
from flask_mail import Mail

cors = CORS()
db = SQLAlchemy()
mail = Mail()



# Assign automatic data type coercion. For example str representations of UUIDs
# are automatically coerced into UUID objects.
force_auto_coercion()


@sa.event.listens_for(db.metadata, 'before_create')
def create_postgres_extensions(target, connection, **kw):
    connection.execute('CREATE EXTENSION IF NOT EXISTS "uuid-ossp"')


@sa.event.listens_for(db.metadata, 'after_drop')
def drop_postgres_extensions(target, connection, **kw):
    connection.execute('DROP EXTENSION "uuid-ossp"')
