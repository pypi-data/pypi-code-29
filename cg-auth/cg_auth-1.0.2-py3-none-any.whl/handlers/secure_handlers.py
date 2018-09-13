# Filename: secure_handlers.py

import tornado.web

from cg_tornado.handlers import BaseApiHandler, BaseWebHandler
from cg_auth.controllers import AuthSessions
from .security import CGSecurity


class SecureApiHandler(BaseApiHandler):
    def prepare(self):
        super().prepare()

        self.User = None

        if self.request.method == 'OPTIONS':
            raise tornado.web.HTTPError(200)

        # validate token
        auth_token = None
        if hasattr(self.application, 'AuthCookieName'):
            auth_token = self.get_secure_cookie(self.application.AuthCookieName)

        if auth_token is None:
            auth_token = self.request.headers.get('Authorization')

        session_id = None
        if auth_token is not None:
            try:
                session_id = CGSecurity.OpenToken(auth_token, self.application.PrivateKey,
                                                  self.application.PrivateKey_Secret)
            except Exception:
                self.clear_all_cookies()
                raise tornado.web.HTTPError(401)

        # decode session
        sess_ctrl = AuthSessions(gdb=self.gdb, data=self.Data, request=self.request,
                             user=self.User, app=self.application)
        self.User = sess_ctrl.DecodeSession(session_id)

        if self.User is None:
            self.clear_all_cookies()
            raise tornado.web.HTTPError(401)

        return


class SecureWebHandler(BaseWebHandler):
    def prepare(self):
        super().prepare()
        self.User = None
        return

    def _getSessionId(self):
        auth_token = None
        if hasattr(self.application, 'AuthCookieName'):
            auth_token = self.get_secure_cookie(self.application.AuthCookieName)

        session_id = None
        if auth_token is not None:
            try:
                session_id = CGSecurity.OpenToken(auth_token, self.application.PrivateKey,
                                                  self.application.PrivateKey_Secret)
            except Exception:
                self.clear_all_cookies()

        return session_id

    def Index(self):
        # validate session
        sess_ctrl = AuthSessions(gdb=self.gdb, data=self.Data, request=self.request,
                             user=self.User, app=self.application)
        self.User = sess_ctrl.DecodeSession(self._getSessionId())

        if self.User is None:
            self.clear_all_cookies()

        return

    def Logout(self):
        sess_ctrl = AuthSessions(gdb=self.gdb, data=self.Data, request=self.request )
        sess_ctrl.Logout(self._getSessionId())
        self.clear_all_cookies()
        return
