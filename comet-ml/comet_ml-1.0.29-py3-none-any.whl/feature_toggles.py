# -*- coding: utf-8 -*-
# *******************************************************
#   ____                     _               _
#  / ___|___  _ __ ___   ___| |_   _ __ ___ | |
# | |   / _ \| '_ ` _ \ / _ \ __| | '_ ` _ \| |
# | |__| (_) | | | | | |  __/ |_ _| | | | | | |
#  \____\___/|_| |_| |_|\___|\__(_)_| |_| |_|_|
#
#  Sign up for free at http://www.comet.ml
#  Copyright (C) 2015-2019 Comet ML INC
#  This file can not be copied and/or distributed without the express
#  permission of Comet ML Inc.
# *******************************************************

"""
Author: Boris Feld

This module contains feature toggles related code

"""

import os

BOOLEAN_MAP = {
    "yes": True,
    "true": True,
    "t": True,
    "y": True,
    "1": True,
    "no": False,
    "false": False,
    "f": False,
    "n": False,
    "0": False,
}


def parse_boolean_env(boolean_ish_env_variable):
    return BOOLEAN_MAP.get(boolean_ish_env_variable, None)


class FeatureToggles(object):
    """ Feature Toggle helper class, avoid getting a feature toggle without
    fallbacking on the default value. Also read environment variables for
    overrides
    """

    def __init__(self, raw_toggles):
        self.raw_toggles = raw_toggles

    def __eq__(self, other):
        if isinstance(other, FeatureToggles):
            return self.raw_toggles == other.raw_toggles

        return False

    def __getitem__(self, name):
        env_name = "COMET_OVERRIDE_FEATURE_%s" % name.upper()
        env_value = parse_boolean_env(os.getenv(env_name))
        if env_value is not None:
            return env_value

        return self.raw_toggles.get(name, False)


# Constants defining feature toggles names to avoid typos disabling a feature

GPU_MONITOR = "sdk-gpu-monitor"
