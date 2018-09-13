# Filename: auth_main

import tornado.web

from cg_tornado.handlers import BaseApiHandler
from cg_auth.controllers import AuthCtrl
from .security import CGSecurity


class GiniAuthHandler(BaseApiHandler):

    def prepare(self):
        super().prepare()
        return

    def run(self, slug, method):

        self.Controller = AuthCtrl
        self.ctrl = self.Controller(gdb=self.gdb, data=self.Data, request=self.request, app=self.application)
        self.ctrl.prepare()

        if method not in self.ctrl.PublicMethods:
            raise tornado.web.HTTPError(404)

        func = getattr(self.ctrl, method, None)
        if not func:
            raise tornado.web.HTTPError(404)

        data = {'data': {}}
        if slug == 'auth' and method == 'Login':
            session_id = self.ctrl.Login()
            token = CGSecurity.MakeToken(session_id, self.application.PublicKey)

            # if self.Data['device_type'] == 'web':
            self.set_secure_cookie(self.application.AuthCookieName, token)
            # else:
            data = {'Token': token}
        else:
            data = func()

        self.SendSuccessResponse(data)
        return
