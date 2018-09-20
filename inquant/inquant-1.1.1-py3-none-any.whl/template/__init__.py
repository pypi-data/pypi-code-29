# -*- coding: utf-8 -*-

import os
import sys

currPath = os.path.dirname(__file__)
libpath = os.path.abspath(os.path.join(currPath,'..',"libs"))
sys.path.insert(0,libpath)
