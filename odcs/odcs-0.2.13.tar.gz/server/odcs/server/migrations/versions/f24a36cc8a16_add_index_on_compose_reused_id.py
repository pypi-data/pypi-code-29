"""Add index on Compose.reused_id

Revision ID: f24a36cc8a16
Revises: 3b92820da295
Create Date: 2017-09-21 11:42:00.622541

"""

# revision identifiers, used by Alembic.
revision = 'f24a36cc8a16'
down_revision = '3b92820da295'

from alembic import op
import sqlalchemy as sa


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_index(op.f('ix_composes_reused_id'), 'composes', ['reused_id'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_composes_reused_id'), table_name='composes')
    # ### end Alembic commands ###
