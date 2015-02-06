"""Add uuid-ossp extension

Revision ID: 57a85bc4692
Revises:
Create Date: 2015-02-06 21:49:24.936366

"""

# revision identifiers, used by Alembic.
revision = '57a85bc4692'
down_revision = None
branch_labels = None
depends_on = None

from alembic import op


def upgrade():
    op.execute('CREATE EXTENSION "uuid-ossp"')


def downgrade():
    op.execute('DROP EXTENSION "uuid-ossp"')
