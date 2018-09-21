# -*- coding: utf-8 -*-

from apscheduler.schedulers.twisted import TwistedScheduler
from SpiderKeeper.scheduler.jobs import JobsAdder


def run_scheduler(flask_app):
    scheduler = TwistedScheduler()
    JobsAdder(scheduler, flask_app).add_jobs()
    scheduler.start()
