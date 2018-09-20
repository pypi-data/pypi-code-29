import importlib

# import os
import sys
import webbrowser

# TODO allow user set binary to open
# TODO display options and allow user use
# we want to open in a web browser, maybe as option
browsers = [
    "firefox",
    "mozilla",
    "google-chrome",
    "chrome",
    "chromium",
    "chromium-browser",
    # sorry IE
]

web_first = []
for w in webbrowser._tryorder:
    if any(browser in w for browser in browsers):
        web_first.insert(0, w)
    else:
        web_first.append(w)

webbrowser._tryorder = web_first
print(webbrowser._tryorder)


def cli():
    libname = sys.argv[1]
    lib = importlib.import_module(libname)

    try:
        path = lib.__path__[0]
    except AttributeError:
        path = lib.__file__

    # TODO make this an option
    # if os.path.isfile(path):
    #     path = os.path.dirname(path)
    print("Opening {} ".format(path))
    webbrowser.open_new_tab("file://{}".format(path))
