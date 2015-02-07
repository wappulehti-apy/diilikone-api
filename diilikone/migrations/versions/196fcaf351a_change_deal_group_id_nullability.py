"""change deal_group_id nullability

Revision ID: 196fcaf351a
Revises: 16906adf7a4
Create Date: 2015-02-07 09:42:00.544577

"""

# revision identifiers, used by Alembic.
revision = '196fcaf351a'
down_revision = '16906adf7a4'
branch_labels = None
depends_on = None

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

def upgrade():
    op.alter_column('deal', 'deal_group_id',
               existing_type=postgresql.UUID(),
               nullable=True)


def downgrade():
    op.alter_column('deal', 'deal_group_id',
               existing_type=postgresql.UUID(),
               nullable=False)
