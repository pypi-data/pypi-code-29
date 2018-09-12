from .open_handler import BaseHandler
from cg_tornado.errors import HttpErrors
import tornado.web


class BaseWebHandler(BaseHandler):
    def prepare(self):
        super().prepare()

        self.set_header("Content-Type", "text/html;charset=utf-8")
        return

    def run(self, slug, method):
        super().run(slug, method)

        if method not in self.PublicMethods:
            raise tornado.web.HTTPError(404)

        func = getattr(self, method, None)
        if not func:
            raise tornado.web.HTTPError(404)

        return func()

    def get(self, kwargs=None, kwargs2=None):
        return self._dispatch()

    def write_error(self, status_code, **kwargs):
        code = '{}'.format(status_code)
        title = "Unknown Error"
        message = "Unknown Error"

        if code in HttpErrors:
            title = HttpErrors[code]['title']
            message = HttpErrors[code]['message']

        self.render('error-page.html', Code=code, Title=title, Message=message)
        return
