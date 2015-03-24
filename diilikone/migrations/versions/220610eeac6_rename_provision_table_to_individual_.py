"""rename provision table to individual_provision

Revision ID: 220610eeac6
Revises: 196fcaf351a
Create Date: 2015-03-24 17:13:30.485825

"""

# revision identifiers, used by Alembic.
revision = '220610eeac6'
down_revision = '196fcaf351a'
branch_labels = None
depends_on = None

from alembic import op


def upgrade():
    op.rename_table('provision', 'individual_provision')


def downgrade():
    op.rename_table('individual_provision', 'provision')
