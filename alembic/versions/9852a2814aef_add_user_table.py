"""add user table

Revision ID: 9852a2814aef
Revises: a7b545c1f077
Create Date: 2022-06-23 17:14:26.147478

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9852a2814aef'
down_revision = 'a7b545c1f077'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table('users', 
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('email', sa.String(), nullable=False),
    sa.Column('password', sa.String(), nullable=False),
    sa.Column('created_at', sa.TIMESTAMP(timezone=True),
    server_default=sa.text('now()'), nullable=False),
    sa.PrimaryKeyConstraint('id'), sa.UniqueConstraint('email'))
    pass


def downgrade() -> None:
    op.drop_table('users')
    pass
