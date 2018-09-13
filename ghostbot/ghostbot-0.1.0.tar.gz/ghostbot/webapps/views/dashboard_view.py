from flask import render_template
from flask_classful import FlaskView, route


class DashboardView(FlaskView):
    route_base = "/"

    @route("/")
    def root(self):
        args = {
            "mode": "dashboard",
            "project": "demo",
            # "breadcrumb": [{"href": None, "caption": "Dashboard"}],
            "breadcrumb": [],
            "indicators": {
                "completed_actions": 1045,
                "finished_actions": 592,
                "failed_actions": 38,
                "aborted_actions": 16
            },
            "activity": [{
                    "date": "2013-01-16",
                    "success": 71,
                    "completed": 5,
                    "total": 8
                }, {
                    "date": "2013-01-17",
                    "success": 74,
                    "completed": 4,
                    "total": 6
                }, {
                    "date": "2013-01-18",
                    "success": 78,
                    "completed": 5,
                    "total": 9
                }, {
                  "date": "2013-01-19",
                  "success": 85,
                  "completed": 8,
                  "total": 9
                }, {
                    "date": "2013-01-20",
                    "success": 82,
                    "completed": 9,
                    "total": 12
                }, {
                    "date": "2013-01-21",
                    "success": 83,
                    "completed": 3,
                    "total": 5
                }, {
                    "date": "2013-01-22",
                    "success": 88,
                    "completed": 5,
                    "total": 7
                }, {
                    "date": "2013-01-23",
                    "success": 85,
                    "completed": 7,
                    "total": 8
                }, {
                    "date": "2013-01-24",
                    "success": 85,
                    "completed": 9,
                    "total": 10
                }, {
                    "date": "2013-01-25",
                    "success": 80,
                    "completed": 5,
                    "total": 8
                }, {
                    "date": "2013-01-26",
                    "success": 87,
                    "completed": 4,
                    "total": 8
                }, {
                    "date": "2013-01-27",
                    "success": 84,
                    "completed": 3,
                    "total": 4
                }, {
                    "date": "2013-01-28",
                    "success": 83,
                    "completed": 5,
                    "total": 7
                }, {
                    "date": "2013-01-29",
                    "success": 84,
                    "completed": 5,
                    "total": 8
                }, {
                    "date": "2013-01-30",
                    "success": 81,
                    "completed": 4,
                    "total": 7
                }
            ],
            "logbook": [
                {"job_id": 223, "repeat": "day", "name": "amazon", "schedule": "Every day at 19:00", "status": "running", "time": "5 min 13 sec", "progress": 47, "api": 1192},
                {"job_id": 222, "repeat": "week", "name": "sample", "schedule": "Every friday at 23:45", "status": "completed", "time": "8 min 22 sec", "progress": 100, "api": 1467},
                {"job_id": 221, "repeat": "day", "name": "amazon", "schedule": "Every day at 19:00", "status": "failed", "time": "12 min 1 sec", "progress": 100, "api": 1732},
                {"job_id": 220, "repeat": "month", "name": "batch", "schedule": "Every end of month at 7:00", "status": "finished", "time": "3 min 2 sec", "progress": 100, "api": 1965},
                {"job_id": 219, "repeat": "once", "name": "sandbox", "schedule": "March 25th, 2018 at 21:00", "status": "aborted", "time": "46 sec", "progress": 16, "api": 84}
            ],
            "tasks": [
                {"task_id": 187, "name": "amazon", "status": "active"},
                {"task_id": 153, "name": "sample", "status": "active"},
                {"task_id": 11, "name": "sandbox", "status": "active"},
                {"task_id": 142, "name": "aws", "status": "inactive"},
                {"task_id": 119, "name": "vmware", "status": "inactive"}
            ],
            "evidence": {
                "job_id": [12, 11, 10, 9, 8],
                "screenshots": [
                    "/Users/orita/Developments/demo/exports/evidence/12/screenshots/20180320_134446.png",
                    "/Users/orita/Developments/demo/exports/evidence/12/screenshots/20180320_134450.png",
                    "/Users/orita/Developments/demo/exports/evidence/12/screenshots/20180320_134453.png"
                ],
                "snapshots": [
                    "/Users/orita/Developments/demo/exports/evidence/12/snapshots/20180320_134446.html",
                    "/Users/orita/Developments/demo/exports/evidence/12/snapshots/20180320_134502.html",
                    "/Users/orita/Developments/demo/exports/evidence/12/snapshots/20180320_134504.html",
                    "/Users/orita/Developments/demo/exports/evidence/12/snapshots/20180320_134505.html"
                ],
                "scraps": [

                ],
                "warnings": [

                ],
                "errors": [

                ]
            },
            "infos": {
                "disk_usage": {"amount": 3049, "increase": 8.5},
                "screenshots": {"amount": 6102, "increase": 1.9},
                "snapshots": {"amount": 977, "increase": 0.2},
                "images": {"amount": 4801, "increase": 13.5},
                "scraps": {"amount": 130725, "increase": 126.0},
                "warnings": {"amount": 762, "increase": 2.9},
                "errors": {"amount": 23, "increase": 3.2}
            }
        }
        return render_template("dashboard.html", args=args)

    @route("/trend")
    def trend(self):
        return "trend"
