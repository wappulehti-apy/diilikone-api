"""Add received product columns to Deal

Revision ID: c29b1060ae3c
Revises: 29b8611e8b18
Create Date: 2017-03-23 13:27:10.390280

"""

# revision identifiers, used by Alembic.
revision = 'c29b1060ae3c'
down_revision = '29b8611e8b18'
branch_labels = None
depends_on = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    op.add_column('deal', sa.Column('backpack_received', sa.Boolean(), server_default='f', nullable=False))
    op.add_column('deal', sa.Column('magazines_received', sa.Integer(), server_default='0', nullable=False))
    op.add_column('deal', sa.Column('shirt_received', sa.Boolean(), server_default='f', nullable=False))

def downgrade():
    op.drop_column('deal', 'shirt_received')
    op.drop_column('deal', 'magazines_received')
    op.drop_column('deal', 'backpack_received')