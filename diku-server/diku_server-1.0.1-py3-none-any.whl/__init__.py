from flask import Flask

from diku_server.diku_server.endpoints.authentication import bp as auth
from diku_server.diku_server.endpoints.calendars import bp as cal

name = "diku_server"


def create_app():
    app = Flask(__name__)

    app.register_blueprint(auth)
    app.register_blueprint(cal)

    @app.route("/test", methods=["POST"])
    def test():
        return "success"

    return app
