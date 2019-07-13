"""empty message

Revision ID: 0f5dd8872720
Revises: 
Create Date: 2019-07-13 01:48:36.532315

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '0f5dd8872720'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('sandbox_tokens',
    sa.Column('token', sa.String(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('app_uuid', postgresql.UUID(as_uuid=True), nullable=True),
    sa.PrimaryKeyConstraint('token')
    )
    op.create_index('sandbox_token_uid_appuuid_index', 'sandbox_tokens', ['user_id', 'app_uuid'], unique=True)
    op.create_table('timeline_pins',
    sa.Column('guid', postgresql.UUID(as_uuid=True), nullable=False),
    sa.Column('app_uuid', postgresql.UUID(as_uuid=True), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('id', sa.String(length=32), nullable=False),
    sa.Column('time', sa.DateTime(), nullable=False),
    sa.Column('duration', sa.Integer(), nullable=True),
    sa.Column('create_notification', postgresql.JSONB(astext_type=sa.Text()), nullable=True),
    sa.Column('update_notification', postgresql.JSONB(astext_type=sa.Text()), nullable=True),
    sa.Column('layout', postgresql.JSONB(astext_type=sa.Text()), nullable=False),
    sa.Column('reminders', postgresql.JSONB(astext_type=sa.Text()), nullable=True),
    sa.Column('actions', postgresql.JSONB(astext_type=sa.Text()), nullable=True),
    sa.Column('data_source', sa.String(length=64), nullable=False),
    sa.Column('source', sa.String(length=8), nullable=False),
    sa.Column('create_time', sa.DateTime(), nullable=False),
    sa.Column('update_time', sa.DateTime(), nullable=False),
    sa.PrimaryKeyConstraint('guid')
    )
    op.create_index('timeline_pin_appuuid_uid_pinid_index', 'timeline_pins', ['app_uuid', 'user_id', 'id'], unique=True)
    op.create_table('user_timeline',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('type', sa.String(length=32), nullable=True),
    sa.Column('pin_id', postgresql.UUID(as_uuid=True), nullable=True),
    sa.ForeignKeyConstraint(['pin_id'], ['timeline_pins.guid'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_user_timeline_user_id'), 'user_timeline', ['user_id'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_user_timeline_user_id'), table_name='user_timeline')
    op.drop_table('user_timeline')
    op.drop_index('timeline_pin_appuuid_uid_pinid_index', table_name='timeline_pins')
    op.drop_table('timeline_pins')
    op.drop_index('sandbox_token_uid_appuuid_index', table_name='sandbox_tokens')
    op.drop_table('sandbox_tokens')
    # ### end Alembic commands ###
