"""Add `deal` table.

Revision ID: 18a06f2c7d7
Revises: 88e45a3c98
Create Date: 2015-02-07 01:36:24.589027

"""

# revision identifiers, used by Alembic.
revision = '18a06f2c7d7'
down_revision = '88e45a3c98'
branch_labels = None
depends_on = None

from alembic import op
import sqlalchemy as sa
from sqlalchemy_utils.types.uuid import UUIDType


def upgrade():
    op.create_table(
        'deal',
        sa.Column(
            'id',
            UUIDType(binary=False),
            server_default=sa.text('uuid_generate_v4()'),
            nullable=False
        ),
        sa.Column('size', sa.Integer(), nullable=False),
        sa.Column('deal_group_id', UUIDType(binary=False), nullable=False),
        sa.Column('salesperson_id', UUIDType(binary=False), nullable=False),
        sa.ForeignKeyConstraint(
            ['deal_group_id'], ['deal_group.id'], ondelete='RESTRICT'
        ),
        sa.ForeignKeyConstraint(
            ['salesperson_id'], ['user.id'], ondelete='RESTRICT'
        ),
        sa.PrimaryKeyConstraint('id')
    )
    op.create_index(
        op.f('ix_deal_deal_group_id'), 'deal', ['deal_group_id'], unique=False
    )
    op.create_index(
        op.f('ix_deal_salesperson_id'), 'deal', ['salesperson_id'], unique=True
    )


def downgrade():
    op.drop_index(op.f('ix_deal_salesperson_id'), table_name='deal')
    op.drop_index(op.f('ix_deal_deal_group_id'), table_name='deal')
    op.drop_table('deal')
