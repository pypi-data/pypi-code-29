# Filename: baseapihandler.py

import traceback
import tornado.web

from sqlalchemy.exc import IntegrityError

from .open_handler import BaseHandler
from cg_tornado.errors import HttpErrors, CgBaseException


class BaseApiHandler(BaseHandler):

    def options(self, kwargs=None):
        self.set_header("Access-Control-Allow-Origin", "http://localhost:4200")
        self.set_header("Access-Control-Allow-Credentials", 'true')
        self.set_header("Access-Control-Allow-Headers", "Authorization, Content-Type, Cache-Control, observe, X-Requested-With, headers")
        self.set_header('Access-Control-Allow-Methods', 'POST, GET, OPTIONS')

    def prepare(self):
        super().prepare()

        self.set_header("Content-Type", "application/json")

        try:
            self.Data = {}
            if hasattr(self.request, 'files') and len(self.request.files) > 0:
                self.Files = self.request.files
            elif hasattr(self.request, 'body') and (len(self.request.body) > 0):
                self.Data = tornado.escape.json_decode(self.request.body)

        except Exception:
            traceback.print_exc()
            raise tornado.web.HTTPError(503)

        return

    def get(self, kwargs=None):
        raise tornado.web.HTTPError(404)

    @tornado.gen.coroutine
    def post(self, slug=None, kwargs=None):
        resp = {}
        try:
            retVal = self._dispatch()
            if isinstance(retVal, tornado.concurrent.Future):
                yield retVal

            return
        except IntegrityError as e:
            if self.application.Debug:
                traceback.print_exc()

            resp = {
                'Status': self.application.StatusError,
                'ErrorCode': -3,
                'ErrorMessage': "{}".format(e.orig.msg.split(' (')[0])
            }
        except KeyError as e:
            if self.application.Debug:
                traceback.print_exc()

            resp = {
                'Status': self.application.StatusError,
                'ErrorCode': -3,
                'ErrorMessage': "Field '{}' is required".format(e.args[0])
            }
        except CgBaseException as e:
            if self.application.Debug:
                traceback.print_exc()

            resp = {
                'Status': self.application.StatusError,
                'ErrorCode': e.ErrorCode,
                'ErrorMessage': e.ErrorMessage
            }

            if e.Args is not None:
                for i in range(0, int(len(e.Args) / 2)):
                    resp[e.Args[2 * i]] = e.Args[2 * i + 1]

        self.set_header("Server", self.application.ServerName)
        self.set_header("Content-Type", "application/json")
        self.set_status(200)
        self.write(resp)
        return

    def write_error(self, status_code, **kwargs):
        if 'exc_info' in kwargs:
            ex = kwargs['exc_info'][1]
            if isinstance(ex, CgBaseException):
                resp = {
                    'Status': self.application.StatusError,
                    'ErrorCode': ex.ErrorCode,
                    'ErrorMessage': ex.ErrorMessage
                }

                self.set_status(200)
                self.write(resp)
                return

        message = 'Unknown Error'
        code = '{}'.format(status_code)
        if code in HttpErrors:
            message = '{}-{}'.format(HttpErrors[code]['title'], HttpErrors[code]['message'])

        resp = {
            'Status': self.application.StatusError,
            'ErrorCode': status_code,
            'ErrorMessage': message
        }

        self.set_header("Server", self.application.ServerName)
        self.set_header("Content-Type", "application/json")
        self.write(resp)
        return

    def SendSuccessResponse(self, data=None):
        if self.gdb is not None:
            self.gdb.commit()

        resp = {}
        if data is not None:
            resp['data'] = data

        resp['Status'] = self.application.StatusSuccess

        self.write(resp)
        return

    def SendErrorResponse(self, *response):
        if self.gdb is not None:
            self.gdb.rollback()

        resp = {}
        if response is not None:
            if len(response) == 1:
                resp = response[0]
            else:
                for i in range(0, int(len(response) / 2)):
                    resp[response[2 * i]] = response[2 * i + 1]

        resp['Status'] = self.application.StatusError

        self.write(resp)
        self.finish()
        return
