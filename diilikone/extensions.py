import sqlalchemy as sa
from flask.ext.cors import CORS
from flask.ext.sqlalchemy import SQLAlchemy

db = SQLAlchemy()
cors = CORS()


@sa.event.listens_for(db.metadata, 'before_create')
def create_postgres_extensions(target, connection, **kw):
    connection.execute('CREATE EXTENSION IF NOT EXISTS "uuid-ossp"')


@sa.event.listens_for(db.metadata, 'after_drop')
def drop_postgres_extensions(target, connection, **kw):
    connection.execute('DROP EXTENSION "uuid-ossp"')
