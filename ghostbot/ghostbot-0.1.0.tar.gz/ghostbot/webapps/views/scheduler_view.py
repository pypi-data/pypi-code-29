from flask import render_template
from flask_classful import FlaskView, route


class SchedulerView(FlaskView):
    route_base = "/"

    @route("/")
    def top(self):
        return "scheduler"
