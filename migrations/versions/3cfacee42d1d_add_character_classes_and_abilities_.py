"""Add character classes and abilities tables

Revision ID: 3cfacee42d1d
Revises: ae89e78477b2
Create Date: 2024-11-10 10:35:27.394416

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '3cfacee42d1d'
down_revision: Union[str, None] = 'ae89e78477b2'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('character_classes',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('health', sa.Integer(), nullable=False),
    sa.Column('strength', sa.Integer(), nullable=False),
    sa.Column('agility', sa.Integer(), nullable=False),
    sa.Column('description', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('abilities',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('description', sa.String(), nullable=False),
    sa.Column('effect', sa.String(), nullable=False),
    sa.Column('power', sa.Integer(), nullable=True),
    sa.Column('character_class_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['character_class_id'], ['character_classes.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.add_column('Player', sa.Column('agility', sa.Integer(), nullable=True))
    op.add_column('Player', sa.Column('level', sa.Integer(), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('Player', 'level')
    op.drop_column('Player', 'agility')
    op.drop_table('abilities')
    op.drop_table('character_classes')
    # ### end Alembic commands ###