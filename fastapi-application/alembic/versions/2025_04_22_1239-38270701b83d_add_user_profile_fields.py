"""add user profile fields

Revision ID: 38270701b83d
Revises: 2c33dbd240ae
Create Date: 2025-04-22 12:39:17.441226

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "38270701b83d"
down_revision: Union[str, None] = "2c33dbd240ae"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "users",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("first_name", sa.String(), nullable=True),
        sa.Column("last_name", sa.String(), nullable=True),
        sa.Column("middle_name", sa.String(), nullable=True),
        sa.Column("phone_number", sa.String(), nullable=True),
        sa.Column("address", sa.String(), nullable=True),
        sa.Column("email", sa.String(length=320), nullable=False),
        sa.Column("hashed_password", sa.String(length=1024), nullable=False),
        sa.Column("is_active", sa.Boolean(), nullable=False),
        sa.Column("is_superuser", sa.Boolean(), nullable=False),
        sa.Column("is_verified", sa.Boolean(), nullable=False),
        sa.PrimaryKeyConstraint("id", name=op.f("pk_users")),
    )
    op.create_index(op.f("ix_users_email"), "users", ["email"], unique=True)
    op.create_foreign_key(
        op.f("fk_access_tokens_user_id_users"),
        "access_tokens",
        "users",
        ["user_id"],
        ["id"],
        ondelete="CASCADE",
    )



def downgrade() -> None:
    op.drop_constraint(
        op.f("fk_access_tokens_user_id_users"),
        "access_tokens",
        type_="foreignkey",
    )
    op.drop_index(op.f("ix_users_email"), table_name="users")
    op.drop_table("users")
