"""Add notes to Deal

Revision ID: 8b58e9edd54e
Revises: eac3dc550200
Create Date: 2017-03-19 12:50:45.654743

"""

# revision identifiers, used by Alembic.
revision = '8b58e9edd54e'
down_revision = 'eac3dc550200'
branch_labels = None
depends_on = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    op.add_column('deal', sa.Column('notes', sa.Unicode(length=255), nullable=True))


def downgrade():
    op.drop_column('deal', 'notes')