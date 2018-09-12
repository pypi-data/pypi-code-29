# data_models

from sqlalchemy import BigInteger, Boolean, Float, ForeignKey, Integer, String, Text
from sqlalchemy.orm import relationship, column_property
from sqlalchemy.sql import func
from sqlalchemy.ext.hybrid import hybrid_property

from cg_tornado import Base, DEFAULT_TABLE_ARGS, CGColumn

from app.cg_auth.models import User


class MailQueue(Base):
    __tablename__ = 'mail_queue'
    __primary_key__ = "mail_queue_id"
    __table_args__ = DEFAULT_TABLE_ARGS

    mail_queue_id = CGColumn(Integer, primary_key=True, nullable=False)
    date_added = CGColumn(BigInteger, nullable=True)
    mail_type = CGColumn(String(24), nullable=True)
    recipient_email = CGColumn(String(128), nullable=True)
    recipient_name = CGColumn(String(128), nullable=True)
    mail_data = CGColumn(Text, nullable=True)
    is_processed = CGColumn(Boolean, default=False, nullable=False)
    date_processed = CGColumn(BigInteger, nullable=True)


class Notification(Base):
    __tablename__ = "notifications"
    __primary_key__ = "notification_id"
    __table_args__ = DEFAULT_TABLE_ARGS

    notification_id = CGColumn(Integer, primary_key=True, autoincrement=True, nullable=False)

    title = CGColumn(String(128), nullable=False)
    message = CGColumn(String(256), nullable=True)
    data = CGColumn(Text, nullable=True)

    user_id = CGColumn(ForeignKey(User.user_id, onupdate='RESTRICT', ondelete='RESTRICT'), nullable=False)

    date_added = CGColumn(BigInteger, nullable=False, default=func.unix_timestamp())

    is_processed = CGColumn(Boolean, nullable=False, default=False)
    date_processed = CGColumn(BigInteger, nullable=False, default=func.unix_timestamp(), onupdate=func.unix_timestamp())


class UserFile(Base):
    __tablename__ = 'user_files'
    __primary_key__ = "file_id"
    __table_args__ = DEFAULT_TABLE_ARGS

    file_id = CGColumn(Integer, primary_key=True, autoincrement=True)
    user_id = CGColumn(ForeignKey('users.user_id', onupdate='RESTRICT', ondelete='RESTRICT'), nullable=False)

    file_name = CGColumn(String(260), nullable=False)
    file_size = CGColumn(Integer, nullable=False)
    file_type = CGColumn(String(8), nullable=False)
    file_url = CGColumn(String(260), nullable=True)
    file_ext = CGColumn(String(11), nullable=True)

    is_public = CGColumn(Boolean, nullable=False, default=False)
    is_attached = CGColumn(Boolean, nullable=False, default=False)

    date_added = CGColumn(BigInteger, nullable=False, default=func.unix_timestamp())
    date_updated = CGColumn(BigInteger, nullable=False, default=func.unix_timestamp(), onupdate=func.unix_timestamp())


class FileAttachment(Base):
    __tablename__ = 'file_attachments'
    __primary_key__ = "attachment_id"
    __table_args__ = DEFAULT_TABLE_ARGS

    attachment_id = CGColumn(Integer, primary_key=True, autoincrement=True)
    table_name = CGColumn(String(256), nullable=False)
    row_id = CGColumn(String(256), nullable=False)
    is_public = CGColumn(Boolean, default=False, nullable=False)

    file_id = CGColumn(ForeignKey(UserFile.file_id, onupdate='RESTRICT', ondelete='RESTRICT'), nullable=False)
    file = relationship(UserFile, remote_side=UserFile.file_id, foreign_keys=file_id, lazy='select')

    date_added = CGColumn(BigInteger, nullable=False, default=func.unix_timestamp())
    date_updated = CGColumn(BigInteger, nullable=False, default=func.unix_timestamp(), onupdate=func.unix_timestamp())


class ChangeLog(Base):
    __tablename__ = 'change_logs'
    __primary_key__ = "change_log_id"
    __table_args__ = DEFAULT_TABLE_ARGS

    change_log_id = CGColumn(Integer, primary_key=True, autoincrement=True)
    user_id = CGColumn(ForeignKey('users.user_id', onupdate='RESTRICT', ondelete='RESTRICT'), nullable=False)
    user_comments = CGColumn(String(512), nullable=True)  # record deletion comment if any

    event = CGColumn(String(50), nullable=False)
    table_name = CGColumn(String(100), nullable=False)
    table_row_id = CGColumn(String(100), nullable=False)
    changes = CGColumn(Text, nullable=False)

    date_added = CGColumn(BigInteger, nullable=False, default=func.unix_timestamp())
