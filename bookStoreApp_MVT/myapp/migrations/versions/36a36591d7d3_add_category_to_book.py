"""add category to book

Revision ID: 36a36591d7d3
Revises: 51358bb20a09
Create Date: 2024-02-23 03:51:51.861700

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '36a36591d7d3'
down_revision = '51358bb20a09'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('books', schema=None) as batch_op:
        batch_op.drop_column('category')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('books', schema=None) as batch_op:
        batch_op.add_column(sa.Column('category', sa.VARCHAR(), autoincrement=False, nullable=True))

    # ### end Alembic commands ###
