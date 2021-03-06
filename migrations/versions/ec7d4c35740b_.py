"""empty message

Revision ID: ec7d4c35740b
Revises: 4e143b2ac72a
Create Date: 2016-07-24 00:32:18.755000

"""

# revision identifiers, used by Alembic.
revision = 'ec7d4c35740b'
down_revision = '4e143b2ac72a'

from alembic import op
import sqlalchemy as sa
import sqlalchemy_utils


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('session', sa.Column('timezone', sa.String()))
    op.add_column('session_version', sa.Column('timezone', sa.String(), autoincrement=False, nullable=True))
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('session_version', 'timezone')
    op.drop_column('session', 'timezone')
    ### end Alembic commands ###
