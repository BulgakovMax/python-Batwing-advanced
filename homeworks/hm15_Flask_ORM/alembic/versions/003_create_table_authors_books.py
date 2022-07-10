"""003_create_table_authors_books

Revision ID: 003_create_table_authors_books
Revises: 002_create_table_books
Create Date: 2022-07-09 19:20:22.252246

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '003_create_table_authors_books'
down_revision = '002_create_table_books'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
       "authors_books",
       sa.Column("id", sa.Integer, primary_key=True, autoincrement=True),
       sa.Column("name", sa.String(100), nullable=False),
       sa.Column("second_name", sa.String(100), nullable=False),
       sa.Column("title", sa.String(100), nullable=False)
    )


def downgrade() -> None:
    op.drop_table("authors_books")
