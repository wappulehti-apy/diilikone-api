"""add authentication columns to user

Revision ID: 11e423a9e61
Revises: 1badb81476e
Create Date: 2015-04-12 11:21:59.464934

"""

# revision identifiers, used by Alembic.
revision = '11e423a9e61'
down_revision = '1badb81476e'
branch_labels = None
depends_on = None

import sqlalchemy as sa
from alembic import op
from sqlalchemy_utils.types.password import PasswordType


def upgrade():
    op.add_column(
        'user',
        sa.Column('password', PasswordType, nullable=True)
    )


def downgrade():
    op.drop_column('user', 'password')
