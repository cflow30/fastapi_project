"""add last few columns to posts table

Revision ID: 17d037af5b5a
Revises: e6de0d2ac69a
Create Date: 2022-06-23 17:58:25.024437

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '17d037af5b5a'
down_revision = 'e6de0d2ac69a'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column ('posts', sa.Column('published', sa.Boolean(), nullable=False, server_default="TRUE"),)
    op.add_column('posts', sa.Column('created_at', sa.TIMESTAMP(timezone=True), nullable=False, server_default=sa.text('NOW()')), )

    pass


def downgrade() -> None:
    op.drop_column('posts', 'published')
    op.drop_column('posts', 'created_at')
    pass
