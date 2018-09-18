import os
import time
import traceback
from threading import Thread, Timer


def run_task(target, args=()):
    t = Thread(target=target, args=args)
    t.daemon = True
    t.start()
    return t


def run_task_safe(target, args, err_handler):
    def _target(*args, **kwargs):
        try:
            target(*args, **kwargs)
        except Exception as e:
            err_handler(e, traceback.format_exc())
    return run_task(_target, args)


def run_timer(target, interval=1):
    def handler():
        while True:
            target()
            time.sleep(interval)
    t = Thread(target=handler)
    t.daemon = True
    t.start()
    return t


def run_timer_safe(target, err_handler, interval=1):
    def handler():
        while True:
            try:
                target()
            except Exception as e:
                err_handler(e, traceback.format_exc())
                return
            time.sleep(interval)
    t = Thread(target=handler)
    t.daemon = True
    t.start()
    return t

def force_shutdown(status_code=-1):
    os._exit(status_code)
