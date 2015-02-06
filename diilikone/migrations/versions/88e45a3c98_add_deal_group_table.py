"""Add `deal_group` table.

Revision ID: 88e45a3c98
Revises: 1f75e6d37e
Create Date: 2015-02-07 01:14:20.398906

"""

# revision identifiers, used by Alembic.
revision = '88e45a3c98'
down_revision = '1f75e6d37e'
branch_labels = None
depends_on = None

from alembic import op
import sqlalchemy as sa
from sqlalchemy_utils.types.uuid import UUIDType


def upgrade():
    op.create_table(
        'deal_group',
        sa.Column(
            'id',
            UUIDType(binary=False),
            server_default=sa.text('uuid_generate_v4()'),
            nullable=False
        ),
        sa.Column('name', sa.Unicode(length=255), nullable=False),
        sa.Column('frozen_magazine_amount', sa.Integer(), nullable=True),
        sa.Column('owner_id', UUIDType(binary=False), nullable=False),
        sa.ForeignKeyConstraint(['owner_id'], ['user.id'], ondelete='CASCADE'),
        sa.PrimaryKeyConstraint('id')
    )
    op.create_index(
        op.f('ix_deal_group_owner_id'),
        'deal_group',
        ['owner_id'],
        unique=True
    )


def downgrade():
    op.drop_index(op.f('ix_deal_group_owner_id'), table_name='deal_group')
    op.drop_table('deal_group')
