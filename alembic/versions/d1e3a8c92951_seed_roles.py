"""seed roles

Revision ID: d1e3a8c92951
Revises: 9a3a04a33b78
Create Date: 2024-01-06 16:18:06.293761

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'd1e3a8c92951'
down_revision: Union[str, None] = '9a3a04a33b78'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.execute(r"""INSERT INTO public.roles (id, "name", code) VALUES(nextval('roles_id_seq'::regclass), 'Superuser', 'SUP');""")
    op.execute(r"""INSERT INTO public.roles (id, "name", code) VALUES(nextval('roles_id_seq'::regclass), 'Project Manager', 'PMG');""")
    op.execute(r"""INSERT INTO public.roles (id, "name", code) VALUES(nextval('roles_id_seq'::regclass), 'Regular User', 'RGU');""")


def downgrade() -> None:
    op.execute(r"""DELETE FROM roles WHERE code in('SUP', 'PMG', 'RGU')""")
