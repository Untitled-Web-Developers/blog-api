"""Create 'articles' & 'article_comments' tables

Revision ID: 001
Revises: 
Create Date: 2024-03-03 16:40:57.747321

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '001'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('articles',
    sa.Column('id', sa.BIGINT(), autoincrement=True, nullable=False),
    sa.Column('title', sa.VARCHAR(length=255), nullable=False),
    sa.Column('body', sa.TEXT(), nullable=False),
    sa.Column('created_at', sa.DATETIME(), server_default=sa.text('now()'), nullable=False),
    sa.Column('updated_at', sa.DATETIME(), server_default=sa.text('CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP'), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('id')
    )
    op.create_table('article_comments',
    sa.Column('id', sa.BIGINT(), autoincrement=True, nullable=False),
    sa.Column('article_id', sa.BIGINT(), nullable=False),
    sa.Column('first_name', sa.VARCHAR(length=64), nullable=False),
    sa.Column('last_name', sa.VARCHAR(length=64), nullable=False),
    sa.Column('body', sa.TEXT(), nullable=False),
    sa.Column('created_at', sa.DATETIME(), server_default=sa.text('now()'), nullable=False),
    sa.ForeignKeyConstraint(['article_id'], ['articles.id'], ),
    sa.PrimaryKeyConstraint('id', 'article_id'),
    sa.UniqueConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('article_comments')
    op.drop_table('articles')
    # ### end Alembic commands ###
