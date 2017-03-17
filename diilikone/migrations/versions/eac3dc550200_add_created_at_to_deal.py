"""Add created at to Deal

Revision ID: eac3dc550200
Revises: 11e423a9e61
Create Date: 2017-03-17 14:04:06.428351

"""

# revision identifiers, used by Alembic.
revision = 'eac3dc550200'
down_revision = '11e423a9e61'
branch_labels = None
depends_on = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    op.add_column('deal', sa.Column('created_at', sa.DateTime(), server_default=sa.text('now()'), nullable=True))


def downgrade():
    op.drop_column('deal', 'created_at')
   