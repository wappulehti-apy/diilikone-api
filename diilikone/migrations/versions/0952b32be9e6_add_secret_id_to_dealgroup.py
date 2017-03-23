"""Add secret_id to DealGroup

Revision ID: 0952b32be9e6
Revises: ddb5e3c0e64c
Create Date: 2017-03-23 09:31:57.168735

"""

# revision identifiers, used by Alembic.
revision = '0952b32be9e6'
down_revision = 'ddb5e3c0e64c'
branch_labels = None
depends_on = None

from alembic import op
import sqlalchemy as sa
from sqlalchemy_utils.types.uuid import UUIDType

def upgrade():
    op.add_column('deal_group', sa.Column('secret_id', UUIDType(binary=False), server_default=sa.text('uuid_generate_v4()'), nullable=False))

def downgrade():
    op.drop_column('deal_group', 'secret_id')