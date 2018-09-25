# -*- coding: utf-8 -*-
# Copyright (C) Alexander Pace (2018)
#
# This file is part of ligo-lvalert-monitor
#
# lvalert is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# It is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with lvalert.  If not, see <http://www.gnu.org/licenses/>.
# 

import os

from setuptools import setup, find_packages

version = "0.1"

setup(
  name = "ligo-lvalert-monitor",
  version = version,
  maintainer = "Tanner Prestegard, Alexander Pace, Leo Singer",
  maintainer_email = "tanner.prestegard@ligo.org, alexander.pace@ligo.org, leo.singer@ligo.org",
  description = "LIGO-Virgo Alert Network",
  long_description = "The LIGO-Virgo Alert Network (LVAlert) is a prototype notification service built XMPP to provide a basic notification tool which allows multiple producers and consumers of notifications.",

  url = "https://wiki.ligo.org/DASWG/LVAlert",
  license = 'GPLv2+',
  namespace_packages = ['ligo'],
  packages = find_packages(),

  install_requires = ['ligo-lvalert', 'numpy'],

  scripts = [
    os.path.join('bin','lvalert_monitor_listener'),
    os.path.join('bin','lvalert_monitor_broadcaster'),
  ],

#  include_package_data=True,

#  package_data={'ligo.lvalert': ['*.pem'] },
#  entry_points={
#        'console_scripts': [
#          'lvalert=ligo.lvalert.tool:main',
#      ],
#  }

)

