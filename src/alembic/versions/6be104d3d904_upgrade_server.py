"""upgrade server

Revision ID: 6be104d3d904
Revises: 0edd01580060
Create Date: 2023-09-14 20:11:39.959201

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6be104d3d904'
down_revision = '0edd01580060'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('server', sa.Column('address', sa.String(), nullable=True))
    op.add_column('server', sa.Column('port', sa.String(), nullable=True))
    op.create_unique_constraint(None, 'server', ['address'])
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'server', type_='unique')
    op.drop_column('server', 'port')
    op.drop_column('server', 'address')
    # ### end Alembic commands ###
