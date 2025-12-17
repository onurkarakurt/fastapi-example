"""add content column to posts table

Revision ID: 00a275c41efa
Revises: a82450694cc4
Create Date: 2025-12-12 16:36:58.100783

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '00a275c41efa'
down_revision: Union[str, Sequence[str], None] = 'a82450694cc4'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade() -> None:
    op.drop_column('posts', 'content')
    pass
