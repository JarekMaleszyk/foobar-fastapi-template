"""constraint unique user_id role_id

Revision ID: d6ff0bc37722
Revises: 3406d6c9f2a1
Create Date: 2024-01-10 17:02:27.468761

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'd6ff0bc37722'
down_revision: Union[str, None] = '3406d6c9f2a1'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.execute("""ALTER TABLE user_roles ADD CONSTRAINT user_roles_userid_roleid_unique UNIQUE (user_id, role_id)""")
    pass


def downgrade() -> None:
    op.execute("""ALTER TABLE user_roles DROP CONSTRAINT user_roles_userid_roleid_unique""")
    pass
