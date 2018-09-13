# Filename: data_models

from sqlalchemy import BigInteger, Boolean, Float, ForeignKey, Integer, String, Text
from sqlalchemy.orm import relationship, column_property
from sqlalchemy.sql import func
from sqlalchemy.ext.hybrid import hybrid_property

from cg_tornado import Base, DEFAULT_TABLE_ARGS, CGColumn


class Group(Base):
    __tablename__ = 'groups'
    __primary_key__ = "group_id"
    __table_args__ = DEFAULT_TABLE_ARGS

    group_id = CGColumn(Integer, primary_key=True, nullable=False, autoincrement=True)
    group_name = CGColumn(String(64), nullable=False, unique=True)

    enable_admin_login = CGColumn(Boolean, nullable=False, default=False)
    enable_web_login = CGColumn(Boolean, nullable=False, default=False)
    enable_app_login = CGColumn(Boolean, nullable=False, default=False)

    menu_permissions = CGColumn(Text, nullable=False, default='[]')
    compiled_permissions = CGColumn(Text, nullable=True)

    parent_id = CGColumn(ForeignKey('groups.group_id', onupdate='RESTRICT', ondelete='RESTRICT'), nullable=True)
    parent = relationship('Group', remote_side='Group.group_id', foreign_keys=parent_id, lazy='select')

    date_added = CGColumn(BigInteger, nullable=False, default=func.unix_timestamp())
    date_updated = CGColumn(BigInteger, nullable=False, default=func.unix_timestamp(), onupdate=func.unix_timestamp())


class User(Base):
    __tablename__ = 'users'
    __primary_key__ = "user_id"
    __table_args__ = DEFAULT_TABLE_ARGS

    user_id = CGColumn(Integer, primary_key=True, nullable=False, autoincrement=True)

    group_id = CGColumn(ForeignKey(Group.group_id, onupdate='RESTRICT', ondelete='RESTRICT'), nullable=False)
    group = relationship(Group, remote_side=Group.group_id, foreign_keys=group_id, lazy='select')

    email = CGColumn(String(64), nullable=False, unique=True)
    mobile = CGColumn(String(64), nullable=False, unique=True)
    username = CGColumn(String(64), nullable=False, unique=True)
    password = CGColumn(String(32), nullable=False, secure=True)

    last_success_login = CGColumn(BigInteger, nullable=True)
    last_failed_login = CGColumn(BigInteger, nullable=True)
    failed_login_attempts = CGColumn(Integer, default=False, nullable=False)
    is_activated = CGColumn(Boolean, default=False, nullable=False)
    email_verified = CGColumn(Boolean, default=False, nullable=False)
    phone_verified = CGColumn(Boolean, default=False, nullable=False)
    use_two_factor = CGColumn(Boolean, default=False, nullable=False)
    allow_multi_login = CGColumn(Boolean, default=True, nullable=False)
    is_blocked = CGColumn(Boolean, default=False, nullable=False)
    block_reason = CGColumn(String(64), nullable=True)

    date_added = CGColumn(BigInteger, nullable=False, default=func.unix_timestamp())
    date_updated = CGColumn(BigInteger, nullable=False, default=func.unix_timestamp(), onupdate=func.unix_timestamp())


class UserGroup(Base):
    __tablename__ = 'user_groups'
    __primary_key__ = "membership_id"
    __table_args__ = DEFAULT_TABLE_ARGS

    membership_id = CGColumn(Integer, primary_key=True, nullable=False, autoincrement=True)

    user_id = CGColumn(ForeignKey('users.user_id', onupdate='RESTRICT', ondelete='RESTRICT'), nullable=False)
    user = relationship(User, remote_side=User.user_id, foreign_keys=user_id, lazy='select')

    group_id = CGColumn(ForeignKey(Group.group_id, onupdate='RESTRICT', ondelete='RESTRICT'), nullable=False)
    group = relationship(Group, remote_side=Group.group_id, foreign_keys=group_id, lazy='select')


class UserCode(Base):
    __tablename__ = 'user_codes'
    __primary_key__ = "code_id"
    __table_args__ = DEFAULT_TABLE_ARGS

    code_id = CGColumn(Integer, primary_key=True, nullable=False, autoincrement=True)

    user_id = CGColumn(ForeignKey('users.user_id', onupdate='RESTRICT', ondelete='RESTRICT'), nullable=False)

    code_type = CGColumn(String(8), nullable=True)
    user_code = CGColumn(String(8), nullable=True)
    code_expiry = CGColumn(BigInteger, default=False, nullable=False)


class UserDevice(Base):
    __tablename__ = 'user_devices'
    __primary_key__ = "device_id"
    __table_args__ = DEFAULT_TABLE_ARGS

    device_id = CGColumn(String(32), primary_key=True, nullable=False)
    user_id = CGColumn(ForeignKey('users.user_id', onupdate='RESTRICT', ondelete='RESTRICT'), nullable=False)

    device_name = CGColumn(String(64), nullable=True)
    device_model = CGColumn(String(64), nullable=True)
    device_type = CGColumn(String(64), nullable=True)

    os_name = CGColumn(String(64), nullable=True)
    os_version = CGColumn(String(64), nullable=True)

    pn_type = CGColumn(String(64), nullable=True)
    pn_token = CGColumn(String(512), nullable=True)

    app_version = CGColumn(String(64), nullable=True)
    is_authorized = CGColumn(String(64), nullable=True)
    last_used = CGColumn(String(64), nullable=True)

    date_added = CGColumn(BigInteger, nullable=False, default=func.unix_timestamp())


class AuthSession(Base):
    __tablename__ = 'auth_sessions'
    __primary_key__ = "session_id"
    __table_args__ = DEFAULT_TABLE_ARGS

    session_id = CGColumn(String(32), primary_key=True, nullable=False)

    user_id = CGColumn(ForeignKey('users.user_id', onupdate='RESTRICT', ondelete='RESTRICT'), nullable=True)
    user = relationship(User, remote_side=User.user_id, foreign_keys=user_id, lazy='select')

    session_data = CGColumn(Text, nullable=False, default='{}')

    device_id = CGColumn(ForeignKey('user_devices.device_id', onupdate='RESTRICT', ondelete='RESTRICT'), nullable=True)
    device = relationship(UserDevice, remote_side=UserDevice.device_id, foreign_keys=device_id, lazy='select')

    date_created = CGColumn(BigInteger, nullable=True)
    last_used = CGColumn(BigInteger, nullable=True)
    last_ip = CGColumn(String(24), nullable=True)
    last_ip_change = CGColumn(BigInteger, nullable=True)
    previous_ip = CGColumn(String(24), nullable=True)
    ip_change_delta = CGColumn(Integer, default=False, nullable=False)

    date_added = CGColumn(BigInteger, nullable=False, default=func.unix_timestamp())


class AuthLog(Base):
    __tablename__ = 'auth_logs'
    __table_args__ = DEFAULT_TABLE_ARGS

    auth_log_id = CGColumn(Integer, primary_key=True, nullable=False, autoincrement=True)

    user_id = CGColumn(ForeignKey('users.user_id', onupdate='RESTRICT', ondelete='RESTRICT'), nullable=True)
    user = relationship(User, remote_side=User.user_id, foreign_keys=user_id, lazy='select')

    ip_address = CGColumn(String(24), nullable=True)
    username = CGColumn(String(24), nullable=True)
    is_success = CGColumn(Boolean, default=False, nullable=False)
    message = CGColumn(String(64), nullable=True)
    end_point = CGColumn(String(128), nullable=True)
    auth_data = CGColumn(Text, nullable=True)

    date_added = CGColumn(BigInteger, nullable=False, default=func.unix_timestamp())
