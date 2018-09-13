# Filename: open_handlers.py

import traceback
import tornado.web


class BaseHandler(tornado.web.RequestHandler):

    def set_default_headers(self):
        self.set_header("Access-Control-Allow-Origin", "http://localhost:4200")
        self.set_header("Access-Control-Allow-Credentials", 'true')
        self.set_header("Access-Control-Allow-Headers", "Authorization, Content-Type, Cache-Control, observe, X-Requested-With, headers")
        self.set_header('Access-Control-Allow-Methods', 'POST, GET, OPTIONS')

    def prepare(self):
        super().prepare()
        self.PublicMethods = []

        self.gdb = None
        self.Data = {}
        self.Files = []

        self.Controller = None
        self.ctrl = None

        # URL Format
        # https://demo.codegini.com/<slug>/api/<table>/(.*) -> API Handler
        # https://demo.codegini.com/<slug>/(.*) -> Web Handler

        # parts = self.request.uri.split('/')
        # if len(parts) < 3:
        #     raise tornado.web.HTTPError(400)
        #
        # slug = parts[1]
        # if not slug.startswith('~'):
        #     raise tornado.web.HTTPError(501)
        # slug = slug[1:]
        # if slug not in self.application.LoadedProjects:
        #     raise tornado.web.HTTPError(501)
        #
        # self.ProjectSlug = slug
        # self.UrlParts = parts
        # self.Project = self.application.LoadedProjects[slug]

        try:
            self.gdb = self.application.SessionMaker()
        except Exception:
            traceback.print_exc()
            raise tornado.web.HTTPError(503)

        self.set_header("Server", self.application.ServerName)
        return

    def run(self, slug, method):
        return

    def on_finish(self):
        if self.gdb is not None:
            self.gdb.close()

        super().on_finish()
        return

    def _dispatch(self):

        if self.request.uri.endswith('/'):
            func = getattr(self, 'Index', None)
            if not func:
                raise tornado.web.HTTPError(404)

            func()

        else:
            path = self.request.uri.split('?')[0]
            slug = path.split('/')[-2]
            method = path.split('/')[-1]

            self.run(slug=slug, method=method)

        return
