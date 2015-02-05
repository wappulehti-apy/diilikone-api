"""asdasd

Revision ID: 270d5f8f801
Revises:
Create Date: 2015-02-05 09:44:46.256941

"""

# revision identifiers, used by Alembic.
revision = '270d5f8f801'
down_revision = None
branch_labels = None
depends_on = None

import sqlalchemy as sa
from alembic import op


def upgrade():
    op.create_table(
        'dummy',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('column', sa.Unicode(), nullable=True),
        sa.PrimaryKeyConstraint('id')
    )


def downgrade():
    op.drop_table('dummy')
