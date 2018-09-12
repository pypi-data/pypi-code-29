# users
import hashlib

from sqlalchemy import or_

from cg_tornado import CgDbLogic
from cg_tornado.errors import UserPasswordMismatch, UserBlocked, UserNotActivated, DeviceNotAuthorized
from app.cg_auth.models.data_models import User, User, UserDevice, AuthSession
from .logs import Logs


class AuthCtrl(CgDbLogic):

    def prepare(self):
        self.Model = User
        self.PublicMethods = ['Login']

        super().prepare()

    def _getUserLogin(self):
        query = self.gdb.query(User)
        query = query.filter(or_(User.email == self.Data['username'],
                                 User.mobile == self.Data['username'],
                                 User.username == self.Data['username']))
        return query.one_or_none()

    def Login(self):

        self.AssertData('username', 'password', 'device_id', 'device_name', 'device_model',
                        'os_name', 'os_version', 'pn_type', 'pn_token', 'app_version')

        if 'device_type' not in self.Data:
            self.Data['device_type'] = 'web'

        user = self._getUserLogin()

        log_ctrl = Logs(gdb=self.gdb, data=self.Data, request=self.request,
                        user=self.User, app=self.application)

        if user is None:
            log_ctrl.AddAuthLog('User not exist')
            raise UserPasswordMismatch()

        if user.is_blocked:
            log_ctrl.RecordBlockedLogin(user)
            raise UserBlocked(user.block_reason)

        m = hashlib.md5()
        m.update(self.Data['password'].encode('utf-8'))
        passwd = m.hexdigest()

        if passwd != user.password:
            log_ctrl.RecordFailedLogin(user)
            raise UserPasswordMismatch()

        if not user.is_activated:
            raise UserNotActivated()

        query = self.gdb.query(UserDevice).filter(UserDevice.device_id == self.Data['device_id'])
        # query = query.filter(UserDevice.user_id == user.user_id)
        device = query.one_or_none()

        if device is None:
            if user.use_two_factor:
                pass
        elif not device.is_authorized and device.user_id == user.user_id:
            raise DeviceNotAuthorized()

        session = log_ctrl.RecordLoginSuccess(user, device)

        return session.session_id
