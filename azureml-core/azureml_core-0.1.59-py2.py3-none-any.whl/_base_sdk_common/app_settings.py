# ---------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# ---------------------------------------------------------

import os
import json


class AppSettings(object):
    def __init__(self):
        dir_path = os.path.dirname(os.path.realpath(__file__))
        file_path = os.path.join(dir_path, "appsettings.json")
        with open(file_path, "r") as settings_file:
            self._settings = json.load(settings_file)

    def get_flight(self):
        return self._settings["flight"]
