"""Adding webhook model

Revision ID: 2055953d31b9
Revises: f4005d62a61c
Create Date: 2019-02-18 13:08:04.292569+11:00

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2055953d31b9'
down_revision = 'f4005d62a61c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('webhook',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('url', sa.String(length=200), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('webhook')
    # ### end Alembic commands ###
