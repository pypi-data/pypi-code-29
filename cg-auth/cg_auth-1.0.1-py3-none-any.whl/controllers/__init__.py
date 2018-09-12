# Filename: __init__.py

from .auth import AuthCtrl

from .groups import Groups, Group
from .users import Users, User
from .sessions import Sessions, AuthSession
from .devices import Devices, UserDevice
from .logs import Logs, AuthLog

Registry = {
    'groups':  {'ctrl': Groups, 'model': Group},
    'users': {'ctrl': Users, 'model': User},
    'user_sessions': {'ctrl': Sessions, 'model': AuthSession},
    'user_devices': {'ctrl': Devices, 'model': UserDevice}
}
