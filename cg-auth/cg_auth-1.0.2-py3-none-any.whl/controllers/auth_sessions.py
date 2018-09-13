# Filename: auth_sessions

import json

from cg_tornado import CGDbLogic, LoggedInUser
from cg_auth.models.data_models import AuthSession, UserGroup


class AuthSessions(CGDbLogic):

    def prepare(self):
        self.Model = AuthSession
        super().prepare()

        self.PublicMethods = ['DecodeSession', 'Logout', 'List']

    def List(self):
        self.addTopWhere(column='user_id', value=self.User.user_id)
        return super().List()

    def Logout(self, session_id=None):
        if session_id is None:
            return None

        self.gdb.query(AuthSession).filter(AuthSession.session_id == session_id).delete()
        self.gdb.commit()

        return

    def DecodeSession(self, session_id=None):

        if session_id is None:
            return None

        query = self.gdb.query(AuthSession).filter(AuthSession.session_id == session_id)
        session = query.one_or_none()

        if session is None:
            return None

        data = {
            'session_id': session_id,
            'user_id': session.user_id,
            'email': session.user.email,
            'mobile': session.user.mobile,
            'username': session.user.username,
            'group_id': session.user.group.group_id,
            'session_data': json.loads(session.session_data),
            'menu_permissions': session.user.group.menu_permissions,
            'compiled_permissions': session.user.group.compiled_permissions
        }

        # query = self.gdb.query(UserGroup).filter(UserGroup.user_id == session.user_id)
        # groups = query.all()
        # user['groups'] = [session.user.group_id] + [g.group_id for g in groups]

        user = LoggedInUser(data)
        return user
