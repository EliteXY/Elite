"""add_active_thread_tail_messsage_id_and_message_eval

Revision ID: 5ed411a331f4
Revises: 5b4211625a9f
Create Date: 2023-05-29 15:51:41.857262

"""
import sqlalchemy as sa
import sqlmodel
from alembic import op
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = "5ed411a331f4"
down_revision = "5b4211625a9f"
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "message_evaluation",
        sa.Column("inferior_message_ids", postgresql.JSONB(astext_type=sa.Text()), nullable=True),
        sa.Column("id", sqlmodel.sql.sqltypes.AutoString(), nullable=False),
        sa.Column("chat_id", sqlmodel.sql.sqltypes.AutoString(), nullable=False),
        sa.Column("user_id", sqlmodel.sql.sqltypes.AutoString(), nullable=False),
        sa.Column("selected_message_id", sqlmodel.sql.sqltypes.AutoString(), nullable=False),
        sa.ForeignKeyConstraint(
            ["chat_id"],
            ["chat.id"],
        ),
        sa.ForeignKeyConstraint(
            ["selected_message_id"],
            ["message.id"],
        ),
        sa.ForeignKeyConstraint(
            ["user_id"],
            ["user.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index(op.f("ix_message_evaluation_chat_id"), "message_evaluation", ["chat_id"], unique=False)
    op.create_index(op.f("ix_message_evaluation_user_id"), "message_evaluation", ["user_id"], unique=False)
    op.add_column("chat", sa.Column("active_thread_tail_message_id", sqlmodel.sql.sqltypes.AutoString(), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column("chat", "active_thread_tail_message_id")
    op.drop_index(op.f("ix_message_evaluation_user_id"), table_name="message_evaluation")
    op.drop_index(op.f("ix_message_evaluation_chat_id"), table_name="message_evaluation")
    op.drop_table("message_evaluation")
    # ### end Alembic commands ###
