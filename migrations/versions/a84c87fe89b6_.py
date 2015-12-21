"""Add problem tag model.

Revision ID: a84c87fe89b6
Revises: 8d1f976c8cbe
Create Date: 2015-12-21 14:47:05.487722

"""

# revision identifiers, used by Alembic.
revision = 'a84c87fe89b6'
down_revision = '8d1f976c8cbe'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('problem_tag',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('text', sa.String(length=32), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('problem_tag_rel',
    sa.Column('tag_id', sa.Integer(), nullable=True),
    sa.Column('problem_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['problem_id'], ['problem.id'], ),
    sa.ForeignKeyConstraint(['tag_id'], ['problem_tag.id'], )
    )
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('problem_tag_rel')
    op.drop_table('problem_tag')
    ### end Alembic commands ###