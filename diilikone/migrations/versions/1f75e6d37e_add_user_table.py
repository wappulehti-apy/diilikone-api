"""Add `user` table.

Revision ID: 1f75e6d37e
Revises: 3a550b296ce
Create Date: 2015-02-07 00:53:31.665860

"""

# revision identifiers, used by Alembic.
revision = '1f75e6d37e'
down_revision = '3a550b296ce'
branch_labels = None
depends_on = None

from alembic import op
import sqlalchemy as sa
from sqlalchemy_utils.types.email import EmailType
from sqlalchemy_utils.types.uuid import UUIDType


def upgrade():
    op.create_table(
        'user',
        sa.Column(
            'id',
            UUIDType(binary=False),
            server_default=sa.text('uuid_generate_v4()'),
            nullable=False
        ),
        sa.Column('email', EmailType(length=255), nullable=False),
        sa.Column('first_name', sa.Unicode(length=255), nullable=False),
        sa.Column('last_name', sa.Unicode(length=255), nullable=False),
        sa.Column('guild', sa.Unicode(length=100), nullable=True),
        sa.Column('class_year', sa.Unicode(length=1), nullable=True),
        sa.Column('phone_number', sa.Unicode(length=20), nullable=True),
        sa.Column('signed_at', sa.DateTime(), nullable=True),
        sa.PrimaryKeyConstraint('id'),
        sa.UniqueConstraint('email')
    )


def downgrade():
    op.drop_table('user')
