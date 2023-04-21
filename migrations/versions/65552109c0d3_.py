"""empty message

Revision ID: 65552109c0d3
Revises: 35e3e58b0796
Create Date: 2023-04-21 10:45:35.162063

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '65552109c0d3'
down_revision = '35e3e58b0796'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('contacts',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('email', sa.String(), nullable=False),
    sa.Column('phone', sa.String(), nullable=False),
    sa.Column('message', sa.Text(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('contacts')
    # ### end Alembic commands ###