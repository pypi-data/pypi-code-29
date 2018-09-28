import threading
from gi.repository import GLib


def threaded(func):
    def call(*args, **kwargs):
        thread = threading.Thread(target=func, args=args, kwargs=kwargs)
        thread.daemon = True
        thread.start()
        return thread
    return call


def glib_call(func):
    def call(*args, **kwargs):
        GLib.idle_add(func, *args)
    return call
