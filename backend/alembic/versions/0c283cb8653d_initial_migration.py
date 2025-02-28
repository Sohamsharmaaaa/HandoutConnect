"""Initial Migration

Revision ID: 0c283cb8653d
Revises: 302f51db0d95
Create Date: 2025-02-27 20:32:55.714938

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '0c283cb8653d'
down_revision: Union[str, None] = '302f51db0d95'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
