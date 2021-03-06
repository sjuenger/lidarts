"""empty message

Revision ID: dec6e094b69c
Revises: c5015c06a737
Create Date: 2020-03-24 12:48:14.426672

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'dec6e094b69c'
down_revision = 'c5015c06a737'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('is_online', sa.Boolean(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'is_online')
    # ### end Alembic commands ###
