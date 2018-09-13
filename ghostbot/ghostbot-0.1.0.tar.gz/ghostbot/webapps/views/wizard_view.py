import random
from flask import render_template
from flask_classful import FlaskView, route
from ghostbot.utils.os import Hash


class WizardView(FlaskView):
    route_base = "/"
    auth_token = Hash.digest(str(random.uniform(-65535, 65535)))

    @route("/wizard/top")
    def top(self):
        return "wizard"

    @route("/wizard/project")
    def project(self):
        args = {
            "mode": "console",
            "breadcrumb": [{"href": None, "caption": "Wizard"}],
            "indicators": {
                "completed_actions": 1045,
                "finished_actions": 592,
                "failed_actions": 38,
                "aborted_actions": 16
            },
            "target": "project",
            "auth_token": self.auth_token
        }
        # return render_template("wizard.html", args=args)
        return render_template("logbook.html", args=args)

    @route("/wizard/agent/<project_id>")
    def agent(self, project_id):
        args = {
            "mode": "console",
            "breadcrumb": [{"href": "/wizard", "caption": "Wizard"}, {"href": None, "caption": "Agent"}],
            "target": "agent",
            "project_id": project_id,
            "auth_token": self.auth_token
        }
        return render_template("wizard.html", args=args)

    @route("/wizard/container/<project_id>")
    def container(self, project_id):
        args = {
            "mode": "console",
            "breadcrumb": [{"href": "/wizard", "caption": "Wizard"}, {"href": None, "caption": "Container"}],
            "target": "container",
            "project_id": project_id,
            "auth_token": self.auth_token
        }
        return render_template("wizard.html", args=args)

    @route("/wizard/reactor/<project_id>")
    def reactor(self, project_id):
        args = {
            "mode": "console",
            "breadcrumb": [{"href": "/wizard", "caption": "Wizard"}, {"href": None, "caption": "Reactor"}],
            "target": "reactor",
            "project_id": project_id,
            "auth_token": self.auth_token
        }
        return render_template("wizard.html", args=args)
