# Filename: __init__.py

from .auth import AuthCtrl

from .groups import Groups, Group
from .users import Users, User
from .auth_sessions import AuthSessions, AuthSession
from .user_devices import UserDevices, UserDevice
from .auth_logs import AuthLogs, AuthLog

Registry = {
    'groups':  {'ctrl': Groups, 'model': Group},
    'users': {'ctrl': Users, 'model': User},
    'auth_sessions': {'ctrl': AuthSessions, 'model': AuthSession},
    'user_devices': {'ctrl': UserDevices, 'model': UserDevice},
    'auth_logs': {'ctrl': AuthLogs, 'model': AuthLog}
}
