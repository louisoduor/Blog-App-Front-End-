"""empty message

Revision ID: c27850d31478
Revises: b56c01991337
Create Date: 2024-04-18 13:50:43.742693

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c27850d31478'
down_revision = 'b56c01991337'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('author_model')
    op.drop_table('register_model')
    op.drop_table('blog_model')
    op.drop_table('help_messages')
    op.drop_table('author_list')
    op.drop_table('blog_data')
    op.drop_table('tags_list')
    op.drop_table('tokens')
    op.drop_table('author_profile')
    op.drop_table('user_model')
    op.drop_table('profile_model')
    op.drop_table('general')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('general',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('message', sa.VARCHAR(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('profile_model',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('email', sa.VARCHAR(), nullable=True),
    sa.Column('isverified', sa.BOOLEAN(), nullable=True),
    sa.Column('createdon', sa.DATE(), nullable=True),
    sa.Column('firstname', sa.VARCHAR(), nullable=True),
    sa.Column('lastname', sa.VARCHAR(), nullable=True),
    sa.Column('dob', sa.DATE(), nullable=True),
    sa.Column('profileurl', sa.VARCHAR(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('user_model',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('firstname', sa.VARCHAR(), nullable=True),
    sa.Column('lastname', sa.VARCHAR(), nullable=True),
    sa.Column('dob', sa.DATE(), nullable=True),
    sa.Column('profileurl', sa.VARCHAR(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('author_profile',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('profile_model_id', sa.INTEGER(), nullable=True),
    sa.Column('blog_data_id', sa.INTEGER(), nullable=True),
    sa.ForeignKeyConstraint(['blog_data_id'], ['blog_data.id'], ),
    sa.ForeignKeyConstraint(['profile_model_id'], ['profile_model.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('tokens',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('message', sa.VARCHAR(), nullable=True),
    sa.Column('access_token', sa.VARCHAR(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('tags_list',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('total_tags', sa.INTEGER(), nullable=True),
    sa.Column('tags', sa.VARCHAR(length=255), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('blog_data',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('Total_Blogs', sa.INTEGER(), nullable=True),
    sa.Column('blog_model_id', sa.INTEGER(), nullable=True),
    sa.ForeignKeyConstraint(['blog_model_id'], ['blog_model.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('author_list',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('total', sa.INTEGER(), nullable=True),
    sa.Column('author_model_id', sa.INTEGER(), nullable=True),
    sa.ForeignKeyConstraint(['author_model_id'], ['author_model.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('help_messages',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('message', sa.VARCHAR(), nullable=True),
    sa.Column('help', sa.VARCHAR(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('blog_model',
    sa.Column('id', sa.VARCHAR(), nullable=False),
    sa.Column('title', sa.VARCHAR(), nullable=True),
    sa.Column('thumbnail', sa.VARCHAR(), nullable=True),
    sa.Column('content', sa.VARCHAR(), nullable=True),
    sa.Column('createdon', sa.DATETIME(), nullable=True),
    sa.Column('tag', sa.VARCHAR(), nullable=True),
    sa.Column('name', sa.VARCHAR(), nullable=True),
    sa.Column('authorid', sa.VARCHAR(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('register_model',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('email', sa.VARCHAR(), nullable=True),
    sa.Column('password', sa.VARCHAR(), nullable=True),
    sa.Column('isverified', sa.BOOLEAN(), nullable=True),
    sa.Column('createdon', sa.DATE(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('author_model',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('email', sa.VARCHAR(), nullable=True),
    sa.Column('isverified', sa.BOOLEAN(), nullable=True),
    sa.Column('createdon', sa.DATE(), nullable=True),
    sa.Column('firstname', sa.VARCHAR(), nullable=True),
    sa.Column('lastname', sa.VARCHAR(), nullable=True),
    sa.Column('dob', sa.DATE(), nullable=True),
    sa.Column('profileurl', sa.VARCHAR(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###
