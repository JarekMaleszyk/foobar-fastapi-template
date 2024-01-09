"""is_active user_role added

Revision ID: 3406d6c9f2a1
Revises: f07a55426cb5
Create Date: 2024-01-09 20:22:31.194874

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.sql.expression import text


# revision identifiers, used by Alembic.
revision: str = '3406d6c9f2a1'
down_revision: Union[str, None] = 'f07a55426cb5'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.drop_column('user_roles', column_name='updated_at')
    op.drop_column('user_roles', column_name='created_at')
    op.add_column('user_roles', sa.Column('is_active', sa.Boolean, nullable=False, server_default='TRUE'))
    op.add_column('user_roles', sa.Column('created_at', sa.TIMESTAMP(timezone=True), nullable=False, server_default=text('now()')))
    op.add_column('user_roles', sa.Column('updated_at', sa.TIMESTAMP(timezone=True), nullable=True))
    pass

def downgrade() -> None:
    op.drop_column('user_roles', column_name='is_active')
    pass
