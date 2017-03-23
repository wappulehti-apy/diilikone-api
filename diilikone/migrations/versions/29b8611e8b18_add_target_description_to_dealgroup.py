"""Add target_description to dealGroup

Revision ID: 29b8611e8b18
Revises: 0952b32be9e6
Create Date: 2017-03-23 10:10:39.035630

"""

# revision identifiers, used by Alembic.
revision = '29b8611e8b18'
down_revision = '0952b32be9e6'
branch_labels = None
depends_on = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    op.add_column('deal_group', sa.Column('target_description', sa.Unicode(length=255), nullable=True))

def downgrade():
    op.drop_column('deal_group', 'target_description')