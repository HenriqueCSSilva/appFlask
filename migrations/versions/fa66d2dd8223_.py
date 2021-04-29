"""empty message

Revision ID: fa66d2dd8223
Revises: cf6779a0fdd1
Create Date: 2021-04-28 23:04:01.584976

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'fa66d2dd8223'
down_revision = 'cf6779a0fdd1'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('portfolio',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nome', sa.String(), nullable=True),
    sa.Column('descricao', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('nome')
    )
    op.create_table('portfolio_picture',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('id_portfolio', sa.String(), nullable=True),
    sa.Column('imagem', sa.String(), nullable=True),
    sa.ForeignKeyConstraint(['id_portfolio'], ['portfolio.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('imagem')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('portfolio_picture')
    op.drop_table('portfolio')
    # ### end Alembic commands ###