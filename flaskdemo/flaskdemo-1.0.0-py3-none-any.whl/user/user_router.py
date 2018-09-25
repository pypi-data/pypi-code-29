# -*- coding:utf-8 -*-
from flask import render_template, current_app


def user_router(username):
    current_app.logger.info("user_router username:%s", username)
    return render_template("user/welcome.html", name=username)

