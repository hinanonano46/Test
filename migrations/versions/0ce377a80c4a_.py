"""empty message

Revision ID: 0ce377a80c4a
Revises: 
Create Date: 2021-03-01 17:10:02.419858

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0ce377a80c4a'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('data',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('metro_id', sa.String(length=125), nullable=False),
    sa.Column('car_id', sa.String(length=125), nullable=False),
    sa.Column('wheel_id', sa.String(length=125), nullable=False),
    sa.Column('QR', sa.Float(precision=2), nullable=True),
    sa.Column('Sh', sa.Float(precision=2), nullable=True),
    sa.Column('Sd', sa.Float(precision=2), nullable=True),
    sa.Column('ddM', sa.Float(precision=2), nullable=True),
    sa.Column('dAR', sa.Float(precision=2), nullable=True),
    sa.Column('WD', sa.Float(precision=2), nullable=True),
    sa.Column('AR', sa.Float(precision=2), nullable=True),
    sa.Column('date', sa.Date(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('data')
    # ### end Alembic commands ###
