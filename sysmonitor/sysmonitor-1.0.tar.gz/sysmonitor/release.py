#pylint: disable=all
"""Release information regarding sysmonitor.agent"""

RELEASE_LEVELS = [ALPHA, BETA, RELEASE_CANDIDATE, FINAL] = ['alpha', 'beta', 'candidate', 'final']
RELEASE_LEVELS_DISPLAY = {ALPHA: ALPHA,
                          BETA: BETA,
                          RELEASE_CANDIDATE: 'rc',
                          FINAL: ''}

version_info = (1, 0, 0, FINAL, 0)
version_db = version_info[:3]
version = '.'.join(str(s) for s in version_info[:2]) + RELEASE_LEVELS_DISPLAY[version_info[3]] + str(version_info[4] or '')
series = serie = major_version = '.'.join(str(s) for s in version_info[:2])

product_name = "sysmonitor"
description = "System Monitor Daemon"
long_desc = "Daemon used to gather agents information"
classifiers = """Development Status :: 3 - Alpha
Environment :: No Input/Output (Daemon)
Intended Audience :: System Administrators
License :: OSI Approved :: BSD License
Programming Language :: Python :: 3 :: Only
Operating System :: Unix
Topic :: System :: Monitoring
"""
url = "https://git.hugorodrigues.net/hugorodrigues/sysmonitor"
author = "Hugo Rodrigues"
author_email = "me@hugorodrigues.net"
license = "BSD-3-Clause"
