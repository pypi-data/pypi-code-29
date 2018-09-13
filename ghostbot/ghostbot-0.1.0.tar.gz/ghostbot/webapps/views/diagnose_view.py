from flask_classful import FlaskView, route


class DiagnoseView(FlaskView):
    route_base = "/"

    @route("/diagnose/check")
    def check(self):
        return "diagnose/check"

    @route("/diagnose/update")
    def update(self):
        return "diagnose/update"
