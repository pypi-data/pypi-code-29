# -*- coding: utf-8 -*-
from distutils.core import setup

packages = \
['resin_release_tool']

package_data = \
{'': ['*']}

install_requires = \
['click>=6.7,<7.0', 'resin-sdk>=5.0,<6.0']

entry_points = \
{'console_scripts': ['resin-release-tool = resin_release_tool.cli:cli']}

setup_kwargs = {
    'name': 'resin-release-tool',
    'version': '0.1.0',
    'description': 'Release tool to have canary in resin.io',
    'long_description': '# resin-release-tool\nThis tool is to set release canary in resin.io\n\n## Installation\n```\npip install resin-release-tool\n```\n\n## Build / Run locally\nYou need poetry to build the project https://poetry.eustace.io/\n```\npoetry install\npoetry build\npoetry run resin-release-tool\netc..\n```\n\n\n## Usage\n```\nUsage: resin-release-tool [OPTIONS] COMMAND [ARGS]...\n\n  You can set app and token as an environment variable, using RESIN_APP and\n  RESIN_TOKEN\n\nOptions:\n  --token TOKEN  Resin.io auth token  [required]\n  --app APP_ID   Resin App name  [required]\n  --help         Show this message and exit.\n\nCommands:\n  disable_rolling      Disables rolling releases in the application\n  enable_rolling       Enables rolling releases in the application\n  info                 Information of the application\n  release              Sets release and canary commits\n  releases             Show success releases of the application\n  show_devices_status  Enables rolling releases in the application\n```\n',
    'author': 'roger',
    'author_email': 'roger.duran@mobilityhouse.com',
    'url': 'https://github.com/mobilityhouse/resin-release-tool',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.5,<4.0',
}


setup(**setup_kwargs)
