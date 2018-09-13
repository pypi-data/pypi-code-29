from flask import render_template
from flask_classful import FlaskView, route


class TaskView(FlaskView):
    route_base = "/"

    @route("/task")
    def top(self):
        args = {
            "content_title": "Task",
            "logbook": [
                {"active": True, "id": 123, "task": ["day", "amazon", "every day at 04:00"], "status": ["Running", "35 screenshots, 12 snapshots"], "progress": ["v1.2.0", "1043 API called", 45], "departure": ["2018-03-17", "16:32"], "arrival": ["", ""]},
                {"active": False, "id": 122, "task": ["week", "sample", "every week at sunday 02:30"], "status": ["Completed", "35 screenshots, 12 snapshots"], "progress": ["v1.2.0", "1043 API called", 100], "departure": ["2018-03-17", "16:32"], "arrival": ["2018-03-17", "20:30"]},
                {"active": False, "id": 121, "task": ["month", "amazon", "every month 1 at 04:00"], "status": ["Completed", "35 screenshots, 12 snapshots"], "progress": ["v1.2.0", "1043 API called", 100], "departure": ["2018-03-17", "16:32"], "arrival": ["2018-03-17", "20:30"]},
                {"active": False, "id": 120, "task": ["day", "amazon", "every day at 04:00"], "status": ["Completed", "35 screenshots, 12 snapshots"], "progress": ["v1.2.0", "1043 API called", 100], "departure": ["2018-03-17", "16:32"], "arrival": ["2018-03-17", "20:30"]},
                {"active": False, "id": 119, "task": ["once", "sandbox", "once at 2018-03-14 16:30"], "status": ["Aborted", "35 screenshots, 12 snapshots"], "progress": ["v1.2.0", "1043 API called", 12], "departure": ["2018-03-17", "16:32"], "arrival": ["2018-03-17", "20:30"]}
            ]
        }
        return render_template("task.html", args=args)
