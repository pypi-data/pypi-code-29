# users
import json
from sqlalchemy import func

from cg_tornado import CgDbLogic
from app.cg_auth.models.data_models import AuthLog, UserDevice, AuthSession


class Logs(CgDbLogic):

    def prepare(self):
        self.Model = AuthLog
        self.PublicMethods = ['AddAuthLog', 'RecordLoginSuccess', 'RecordFailedLogin', 'RecordBlockedLogin']

        super().prepare()

    def AddAuthLog(self, message, user=None, isSuccess=False):
        log = AuthLog()

        if user is not None:
            log.user_id = user.user_id

        if 'email' in self.Data:
            log.username = self.Data['email']

        log.ip_address = self.request.remote_ip

        log.is_success = isSuccess

        log.message = message
        log.end_point = self.request.path
        log.auth_data = json.dumps(self.Data)

        self.gdb.add(log)
        self.gdb.flush()
        return

    def RecordLoginSuccess(self, user, device):
        log = AuthLog()
        newDeviceAdded = False
        if device is None:
            device = UserDevice()
            device.device_id = self.Data['device_id']
            device.user_id = user.user_id
            device.device_name = self.Data['device_name']
            device.device_model = self.Data['device_model']
            device.device_type = self.Data['device_type']
            device.is_authorized = True

            self.gdb.add(device)
            self.gdb.flush()

            newDeviceAdded = True

        elif device.user_id != user.user_id:
            device.user_id = user.user_id

        device.os_name = self.Data['os_name']
        device.os_version = self.Data['os_version']
        device.pn_type = self.Data['pn_type']
        device.pn_token = self.Data['pn_token']
        device.app_version = self.Data['app_version']
        device.last_used = func.unix_timestamp()

        if newDeviceAdded:
            deviceData = {
                'pn_type': device.pn_type,
                'device_name': device.device_name,
                'os_version': device.os_version,
                'device_model': device.device_model
            }
            # self.AddToMailQueue('NewDeviceSignIn', user.email, user.username, deviceData)

        if not user.allow_multi_login:
            query = self.gdb.query(AuthSession).filter(AuthSession.user_id == user.user_id)
            query.delete()

        query = self.gdb.query(AuthSession).filter(AuthSession.user_id == user.user_id)
        query = query.filter(AuthSession.device_id == device.device_id)
        session = query.one_or_none()
        if session is None:
            session = AuthSession()
            session.session_id = self.GetUniqueId()
            session.user_id = user.user_id
            session.device_id = device.device_id
            session.date_created = func.unix_timestamp()
            self.gdb.add(session)
        else:
            session.session_id = self.GetUniqueId()
            session.date_created = func.unix_timestamp()

        session.last_used = func.unix_timestamp()
        session.last_ip = self.request.remote_ip
        session.last_ip_change = None
        session.previous_ip = None
        session.ip_change_delta = 0

        # add session data
        session_data = self.application.MakeSessionDdata(self.gdb, user.user_id)
        session.session_data = json.dumps(session_data)

        user.last_success_login = func.unix_timestamp()
        user.failed_login_attempts = 0

        log.user_id = user.user_id
        log.username = user.email
        log.date_added = func.unix_timestamp()
        log.ip_address = self.request.remote_ip

        log.is_success = True

        log.message = "Successfull login"
        log.end_point = self.request.path
        log.auth_data = json.dumps(self.Data)

        self.gdb.add(log)
        self.gdb.flush()

        return session

    def RecordFailedLogin(self, user):
        log = AuthLog()

        user.failed_login_attempts += 1
        user.last_failed_login = func.unix_timestamp()

        if user.failed_login_attempts > 4:
            user.is_blocked = True
            user.block_reason = "Exsessive incorrect password attempts"

        log.user_id = user.user_id
        log.username = user.email
        log.date_added = func.unix_timestamp()
        log.ip_address = self.request.remote_ip

        log.is_success = False

        log.message = 'Incorrect password'
        log.end_point = self.request.path
        log.auth_data = json.dumps(self.Data)

        self.gdb.add(log)
        self.gdb.flush()

        return

    def RecordBlockedLogin(self, user):
        log = AuthLog()

        log.user_id = user.user_id
        log.username = user.email
        log.date_added = func.unix_timestamp()
        log.ip_address = self.request.remote_ip

        log.is_success = False

        log.message = "User is blocked, reason: {}".format(user.block_reason)
        log.end_point = self.request.path
        log.auth_data = json.dumps(self.Data)

        self.gdb.add(log)
        self.gdb.flush()

        return
