# -*- coding: utf-8 -*-

"""Constants for Bio2BEL miRBase."""

import os

from bio2bel import get_data_dir

VERSION = '0.0.1'

DATA_URL = "ftp://mirbase.org/pub/mirbase/CURRENT/miRNA.dat.gz"

MODULE_NAME = "mirbase"

DATA_DIR = get_data_dir(MODULE_NAME)
DATA_PATH = os.path.join(DATA_DIR, "miRNA.dat.gz")
