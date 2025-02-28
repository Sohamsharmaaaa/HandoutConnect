"""Fix ForeignKey Ambiguity

Revision ID: 302f51db0d95
Revises: 55a4dddc1f03
Create Date: 2025-02-27 20:26:54.676282

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '302f51db0d95'
down_revision: Union[str, None] = '55a4dddc1f03'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
