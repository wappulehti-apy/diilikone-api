"""add deal_product_type table

Revision ID: 16906adf7a4
Revises: 5340174d300
Create Date: 2015-02-07 04:22:24.545262

"""

# revision identifiers, used by Alembic.
revision = '16906adf7a4'
down_revision = '5340174d300'
branch_labels = None
depends_on = None

from alembic import op
import sqlalchemy as sa
from sqlalchemy_utils.types.uuid import UUIDType


def upgrade():
    op.create_table('deal_product_type',
    sa.Column('deal_id', UUIDType(binary=False), nullable=True),
    sa.Column('product_type_id', UUIDType(binary=False), nullable=True),
    sa.ForeignKeyConstraint(['deal_id'], ['deal.id'], ondelete='cascade'),
    sa.ForeignKeyConstraint(['product_type_id'], ['product_type.id'], ondelete='cascade')
    )


def downgrade():
    op.drop_table('deal_product_type')
