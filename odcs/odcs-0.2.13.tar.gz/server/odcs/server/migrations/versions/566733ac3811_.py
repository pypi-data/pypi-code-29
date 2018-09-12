"""empty message

Revision ID: 566733ac3811
Revises: None
Create Date: 2017-06-08 15:50:27.348945

"""

# revision identifiers, used by Alembic.
revision = '566733ac3811'
down_revision = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('composes',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('owner', sa.String(), nullable=False),
    sa.Column('source_type', sa.Integer(), nullable=False),
    sa.Column('source', sa.String(), nullable=False),
    sa.Column('koji_event', sa.Integer(), nullable=True),
    sa.Column('state', sa.Integer(), nullable=False),
    sa.Column('results', sa.Integer(), nullable=False),
    sa.Column('packages', sa.String(), nullable=True),
    sa.Column('flags', sa.Integer(), nullable=True),
    sa.Column('reused_id', sa.Integer(), nullable=True),
    sa.Column('time_to_expire', sa.DateTime(), nullable=False),
    sa.Column('time_submitted', sa.DateTime(), nullable=False),
    sa.Column('time_done', sa.DateTime(), nullable=True),
    sa.Column('time_removed', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('composes')
    ### end Alembic commands ###
