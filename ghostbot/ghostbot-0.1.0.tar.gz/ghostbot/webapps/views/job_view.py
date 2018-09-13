from flask import render_template
from flask_classful import FlaskView, route
from ghostbot import Ghostbot


class JobView(FlaskView):
    route_base = "/"

    @route("/job")
    def top(self):
        # print("JobView#top called")
        # repository = Ghostbot.repository()
        # args = {
        #     "content_title": "Project",
        #     "active_project": "demo@525ace",
        #     "projects": enumerate(repository.fetch_project())
        # }
        # return render_template("project.html", args=args)
        return "job"
