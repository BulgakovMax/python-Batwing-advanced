"""001_create_table_authors

Revision ID: 001_create_table_authors
Revises: 
Create Date: 2022-07-09 18:19:30.841874

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '001_create_table_authors'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
       "authors",
       sa.Column("id", sa.Integer, primary_key=True, autoincrement=True),
       sa.Column("name", sa.String(100), nullable=False),
       sa.Column("second_name", sa.String(100), nullable=False),       
       sa.Column("country", sa.String(100), nullable=False)
    )
    

def downgrade() -> None:
    op.drop_table("authors")
