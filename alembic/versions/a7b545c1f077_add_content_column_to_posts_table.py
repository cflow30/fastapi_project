"""add content column to posts table

Revision ID: a7b545c1f077
Revises: 8e30ed98d6f5
Create Date: 2022-06-23 16:58:46.495423

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a7b545c1f077'
down_revision = '8e30ed98d6f5'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade() -> None:
    op.drop_column('posts', 'content')
    pass
