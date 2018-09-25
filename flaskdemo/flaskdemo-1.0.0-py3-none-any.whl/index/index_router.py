# -*- coding:utf-8 -*-
from flask import render_template, current_app


def index_router():
    current_app.logger.info("index_router")
    return render_template("index/index.html")

