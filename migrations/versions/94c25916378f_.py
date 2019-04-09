"""Add cascading on delete for objects and tasks

Revision ID: 94c25916378f
Revises: be488404c125
Create Date: 2019-04-02 00:54:37.918529

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '94c25916378f'
down_revision = 'be488404c125'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('objects_project_id_fkey',
                       'objects', type_='foreignkey')
    op.create_foreign_key('objects_project_id_fkey', 'objects', 'projects', ['project_id'], [
                          'project_id'], ondelete='CASCADE')
    op.drop_constraint('task_project_id_fkey', 'task', type_='foreignkey')
    op.create_foreign_key('task_project_id_fkey', 'task', 'projects', ['project_id'], [
                          'project_id'], ondelete='CASCADE')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('task_project_id_fkey', 'task', type_='foreignkey')
    op.create_foreign_key('task_project_id_fkey', 'task',
                          'projects', ['project_id'], ['project_id'])
    op.drop_constraint('objects_project_id_fkey',
                       'objects', type_='foreignkey')
    op.create_foreign_key('objects_project_id_fkey', 'objects', 'projects', [
                          'project_id'], ['project_id'])
    # ### end Alembic commands ###
