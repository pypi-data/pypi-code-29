from threading import Thread


class DaemonThread(Thread):
    """
    Wrapper for auto-start daemon thread
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.daemon = True
        self.start()
