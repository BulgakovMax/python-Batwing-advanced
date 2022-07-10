"""002_create_table_books

Revision ID: 002_create_table_books
Revises: 001_create_table_authors
Create Date: 2022-07-09 19:14:01.122289

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '002_create_table_books'
down_revision = '001_create_table_authors'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
       "books",
       sa.Column("id", sa.Integer, primary_key=True, autoincrement=True),
       sa.Column("title", sa.String(100), nullable=False),
       sa.Column("genre", sa.String(100), nullable=False)
    )


def downgrade() -> None:
    op.drop_table("books")
