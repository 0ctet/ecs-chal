"""Change subnet column in ECSChallenge to subnets so we can store numerous subnets

Revision ID: fd89efbba1d3
Revises: d636e6a85f63
Create Date: 2023-03-08 09:26:07.262308

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = "fd89efbba1d3"
down_revision = "d636e6a85f63"
branch_labels = None
depends_on = None


def upgrade(op=None):
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column("ecs_challenge", sa.Column("subnets", sa.Text(), nullable=True))
    op.drop_index("ix_ecs_challenge_subnet", table_name="ecs_challenge")
    op.drop_column("ecs_challenge", "subnet")
    # ### end Alembic commands ###


def downgrade(op=None):
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column(
        "ecs_challenge",
        sa.Column(
            "subnet",
            mysql.VARCHAR(collation="utf8mb4_unicode_ci", length=128),
            nullable=True,
        ),
    )
    op.create_index(
        "ix_ecs_challenge_subnet", "ecs_challenge", ["subnet"], unique=False
    )
    op.drop_column("ecs_challenge", "subnets")
    # ### end Alembic commands ###
