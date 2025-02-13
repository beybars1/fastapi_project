"""test running migrations

Revision ID: cee79692e2e4
Revises: 382cc985ec1c
Create Date: 2025-02-12 17:23:29.420626

"""
import sqlalchemy as sa
from alembic import op
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = "cee79692e2e4"
down_revision = "4f7486dcadb1"
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column("users", sa.Column("hashed_password", sa.String(), nullable=False))
    op.add_column(
        "users", sa.Column("roles", postgresql.ARRAY(sa.String()), nullable=False)
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column("users", "roles")
    op.drop_column("users", "hashed_password")
    # ### end Alembic commands ###
