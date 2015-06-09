"""create cases table

Revision ID: 467eda2cd7e0
Revises: 
Create Date: 2015-06-08 17:55:40.715667

"""

# revision identifiers, used by Alembic.
revision = '467eda2cd7e0'
down_revision = None
branch_labels = None
depends_on = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    op.create_table(
        'case',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('deed_id', sa.Integer, nullable=False),
        sa.Column('conveyancer_id', sa.Integer, nullable=False),
        sa.Column('status', sa.Unicode(50), nullable=False),
        sa.Column('last_updated', sa.DateTime, nullable=False),
        sa.Column('created_on', sa.DateTime, nullable=False),
    )


def downgrade():
    op.drop_table('case')
