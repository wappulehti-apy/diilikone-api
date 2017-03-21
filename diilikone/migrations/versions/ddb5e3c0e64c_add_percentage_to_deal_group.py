"""Add percentage to deal_group

Revision ID: ddb5e3c0e64c
Revises: 8b58e9edd54e
Create Date: 2017-03-21 12:49:13.655692

"""

# revision identifiers, used by Alembic.
revision = 'ddb5e3c0e64c'
down_revision = '8b58e9edd54e'
branch_labels = None
depends_on = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    op.add_column(
        'deal_group',
        sa.Column(
            'percentage',
            sa.Integer(),
            server_default='0',
            nullable=False
        )
    )


def downgrade():
    op.drop_column('deal_group', 'percentage')
