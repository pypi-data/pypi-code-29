from flask import Flask

from .endpoints.authentication import bp as auth
from .endpoints.calendars import bp as cal

name = "diku_server"


def create_app():
    flask_app = Flask(__name__)

    flask_app.register_blueprint(auth)
    flask_app.register_blueprint(cal)

    @flask_app.route("/test", methods=["POST"])
    def test():
        return "success"

    return flask_app


app = create_app()
