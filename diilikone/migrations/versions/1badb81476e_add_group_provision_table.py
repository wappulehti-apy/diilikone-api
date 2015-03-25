"""add group_provision table

Revision ID: 1badb81476e
Revises: 220610eeac6
Create Date: 2015-03-24 18:01:10.425116

"""

# revision identifiers, used by Alembic.
revision = '1badb81476e'
down_revision = '220610eeac6'
branch_labels = None
depends_on = None

import sqlalchemy as sa
from alembic import op
from sqlalchemy_utils.types.uuid import UUIDType


def upgrade():
    op.create_table(
        'group_provision',
        sa.Column(
            'id',
            UUIDType(binary=False),
            server_default=sa.text('uuid_generate_v4()'),
            nullable=False
        ),
        sa.Column('quantity', sa.Integer(), nullable=False),
        sa.Column(
            'price_per_magazine',
            sa.Numeric(precision=3, scale=2),
            nullable=False
        ),
        sa.PrimaryKeyConstraint('id'),
        sa.UniqueConstraint(
            'quantity',
            deferrable='True',
            initially='DEFERRED',
            name='uq_group_provision_quantity'
        )
    )


def downgrade():
    op.drop_table('group_provision')
