"""add product_type table

Revision ID: 5340174d300
Revises: 18a06f2c7d7
Create Date: 2015-02-07 04:18:41.049618

"""

# revision identifiers, used by Alembic.
revision = '5340174d300'
down_revision = '18a06f2c7d7'
branch_labels = None
depends_on = None

from alembic import op
import sqlalchemy as sa
from sqlalchemy_utils.types.uuid import UUIDType


def upgrade():
    op.create_table('product_type',
    sa.Column('id', UUIDType(binary=False), server_default=sa.text('uuid_generate_v4()'), nullable=False),
    sa.Column('name', sa.Unicode(length=255), nullable=False),
    sa.Column('price', sa.Numeric(scale=2, precision=5), nullable=False),
    sa.Column('stock', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )


def downgrade():
    op.drop_table('product_type')
