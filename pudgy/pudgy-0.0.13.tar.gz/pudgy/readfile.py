import sys
import time
import os
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler


class FileChangedException(Exception):
    pass

class FileReader(FileSystemEventHandler):
    def __init__(self, *args, **kwargs):
        super(FileSystemEventHandler, self).__init__(*args, **kwargs)

        self.__files__ = {}

    def readfile(self, fname):
        fname = os.path.abspath(fname)
        if not fname in self.__files__:
            with open(fname) as f:
                self.__files__[fname] = f.read()

        return self.__files__[fname]

    def cleanfile(self, fname):
        fname = os.path.abspath(fname)
        if fname in self.__files__:
            os._exit(1)

    def on_any_event(self, event):
        pname = os.path.abspath(event.src_path)
        self.cleanfile(pname)

FILE_READER=FileReader()

def readfile(fname):
    return FILE_READER.readfile(fname)


def watchappdir(app):
    d = app.root_path
    watchdir(d)

def watchdir(path):
    print "WATCHING DIR", path
    observer = Observer()
    observer.schedule(FILE_READER, path, recursive=True)
    observer.start()

    return observer


if __name__ == "__main__":
    path = sys.argv[1] if len(sys.argv) > 1 else '.'
    observer = watchdir(path)
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()

