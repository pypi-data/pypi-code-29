from flask import render_template
from flask_classful import FlaskView, route


class SupportView(FlaskView):
    route_base = "/"

    @route("/support/help")
    def help(self):
        return "support/help"

    @route("/support/tutorial")
    def tutorial(self):
        return "support/tutorial"

    @route("/support/reference")
    def reference(self):
        return "support/reference"
