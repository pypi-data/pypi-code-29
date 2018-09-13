from flask import render_template
from flask_classful import FlaskView, route


class EvidenceView(FlaskView):
    route_base = "/"

    @route("/evidence/echo")
    def echo(self):
        print("EvidenceView#echo called")
        return "evidence"

    @route("/evidence")
    def top(self):
        print("ProjectView#top called")
        args = {
            "content_title": "Evidence",
            "active_project": "demo@525ace",
            "projects": enumerate([])
        }
        return render_template("evidence.html", args=args)

    @route("/evidence/<logbook_id>")
    def show(self, logbook_id):
        return "show logbook_id={}".format(logbook_id)
