"""Add provision table.

Revision ID: 3a550b296ce
Revises: 57a85bc4692
Create Date: 2015-02-06 21:57:35.790120

"""

# revision identifiers, used by Alembic.
revision = '3a550b296ce'
down_revision = '57a85bc4692'
branch_labels = None
depends_on = None

from alembic import op
import sqlalchemy as sa
from sqlalchemy_utils.types.uuid import UUIDType


def upgrade():
    op.create_table(
        'provision',
        sa.Column(
            'id',
            UUIDType(binary=False),
            server_default=sa.text('uuid_generate_v4()'),
            nullable=False
        ),
        sa.Column('quantity', sa.Integer, nullable=False),
        sa.Column(
            'price_per_magazine',
            sa.Numeric(precision=3, scale=2),
            nullable=False
        ),
        sa.PrimaryKeyConstraint('id')
    )
    op.create_unique_constraint(
        'uq_provision_quantity',
        'provision',
        ['quantity'],
        deferrable='True',
        initially='DEFERRED'
    )


def downgrade():
    op.drop_constraint('uq_provision_quantity', 'provision', type_='unique')
    op.drop_table('provision')
