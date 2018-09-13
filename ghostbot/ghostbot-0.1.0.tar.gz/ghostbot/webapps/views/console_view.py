import random
from flask import request, render_template
from flask_classful import FlaskView, route
from ghostbot.utils.os import Hash


class ConsoleView(FlaskView):
    route_base = "/"
    auth_token = Hash.digest(str(random.uniform(-65535, 65535)))

    @route("/")
    def root(self):
        args = {
            "mode": "console",
            "projects": [
                # TODO project status is active/inactive/invalid
                {"id": 10, "name": "blank", "path": "/Users/orita/Developments/blank", "dashboard": "invalid", "port": 30010, "last_update": "March 1st, 2018", "agents": 12, "containers": 2, "reactors": 10},
                {"id": 11, "name": "test", "path": "/Users/orita/Developments/test", "dashboard": "inactive", "port": 30011, "last_update": "March 2nd, 2018", "agents": 0, "containers": 0, "reactors": 0},
                {"id": 12, "name": "demo", "path": "/Users/orita/Developments/demo", "dashboard": "inactive", "port": 30012, "last_update": "March 3rd, 2018", "agents": 4, "containers": 1, "reactors": 1},
                {"id": 13, "name": "sandbox", "path": "/Users/orita/Developments/sandbox", "dashboard": "active", "port": 30013, "last_update": "March 30th, 2018", "agents": 38, "containers": 22, "reactors": 30}
            ],
            "auth_token": self.auth_token
        }
        return render_template("console.html", args=args)

    @route("/project/refresh/<project_name>")
    def refresh(self, project_name):
        # TODO
        if not project_name:
            pass
        return "refresh {}".format(project_name)

    @route("/project/remove/<project_id>", methods=["GET", "POST"])
    def remove(self, project_id):
        if "secret" in request.form:
            secret = request.form["secret"]
            if secret == self.auth_token:
                result = "remove project_id={}".format(project_id), 200
            else:
                result = "token unmatched", 500
        else:
            result = "secret required", 400
        return result

    @route("/dashboard/startup/<project_id>", methods=["GET", "POST"])
    def startup(self, project_id):
        # TODO
        return "startup {}".format(project_id)

    @route("/dashboard/shutdown/<project_id>", methods=["GET", "POST"])
    def shutdown(self, project_id):
        # TODO
        return "shutdown {}".format(project_id)

    @route("/wizard")
    def wizard(self):
        args = {
            "mode": "console",
            "projects": [
                # TODO project status is active/inactive/invalid
                {"id": 10, "name": "blank", "path": "/Users/orita/Developments/blank", "dashboard": "invalid", "port": 30010, "last_update": "March 1st, 2018", "agents": 12, "containers": 2, "reactors": 10},
                {"id": 11, "name": "test", "path": "/Users/orita/Developments/test", "dashboard": "inactive", "port": 30011, "last_update": "March 2nd, 2018", "agents": 0, "containers": 0, "reactors": 0},
                {"id": 12, "name": "demo", "path": "/Users/orita/Developments/demo", "dashboard": "inactive", "port": 30012, "last_update": "March 3rd, 2018", "agents": 4, "containers": 1, "reactors": 1},
                {"id": 13, "name": "sandbox", "path": "/Users/orita/Developments/sandbox", "dashboard": "active", "port": 30013, "last_update": "March 30th, 2018", "agents": 38, "containers": 22, "reactors": 30}
            ],
            "auth_token": self.auth_token
        }
        return render_template("wizard.html", args=args)
