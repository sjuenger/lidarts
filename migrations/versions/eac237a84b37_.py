"""empty message

Revision ID: eac237a84b37
Revises: 037f62122689
Create Date: 2019-01-15 21:58:36.681547

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'eac237a84b37'
down_revision = '037f62122689'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('stats',
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('darts_thrown', sa.Integer(), nullable=True),
    sa.Column('double_thrown', sa.Integer(), nullable=True),
    sa.Column('legs_won', sa.Integer(), nullable=True),
    sa.Column('doubles', sa.Float(), nullable=True),
    sa.Column('first9_average', sa.Float(), nullable=True),
    sa.Column('average', sa.Float(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('user_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('stats')
    # ### end Alembic commands ###