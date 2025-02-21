"""empty message

Revision ID: 561bdf73025e
Revises: 46a278193a94
Create Date: 2023-09-12 13:32:03.684063

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "561bdf73025e"
down_revision = "0012477fe0a8"
branch_labels = None
depends_on = None


def upgrade(op):
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column("ecs_challenge", sa.Column("guide", sa.Text(), nullable=True))
    op.add_column("ecs_config", sa.Column("guide_enabled", sa.Boolean(), nullable=True))
    # ### end Alembic commands ###


def downgrade(op):
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column("ecs_config", "guide_enabled")
    op.drop_column("ecs_challenge", "guide")
    # ### end Alembic commands ###
