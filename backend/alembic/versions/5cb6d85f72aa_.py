"""

Revision ID: 5cb6d85f72aa
Revises: 89ccfb58eabc
Create Date: 2024-05-25 08:55:45.668904

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '5cb6d85f72aa'
down_revision: Union[str, None] = '89ccfb58eabc'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('books',
    sa.Column('users_id', sa.UUID(), nullable=False),
    sa.Column('books_id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('books_title', sa.String(length=100), nullable=False),
    sa.Column('books_author', sa.String(length=100), nullable=False),
    sa.Column('books_publisher', sa.String(length=100), nullable=True),
    sa.Column('books_qtd_page', sa.Integer(), nullable=True),
    sa.Column('books_dat_published', sa.DateTime(timezone=True), nullable=True),
    sa.Column('books_dat_created', sa.DateTime(timezone=True), nullable=False),
    sa.ForeignKeyConstraint(['users_id'], ['users.users_id'], ),
    sa.PrimaryKeyConstraint('users_id', 'books_id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('books')
    # ### end Alembic commands ###
