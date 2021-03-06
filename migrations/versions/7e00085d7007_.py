"""empty message

Revision ID: 7e00085d7007
Revises: 4cdc7d622e75
Create Date: 2020-03-29 20:03:20.932671

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7e00085d7007'
down_revision = '4cdc7d622e75'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user_settings', sa.Column('last_country_change', sa.DateTime(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user_settings', 'last_country_change')
    # ### end Alembic commands ###
