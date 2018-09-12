# -*- coding: utf-8 -*-
from distutils.core import setup

packages = \
['adroit']

package_data = \
{'': ['*'], 'adroit': ['docker/*']}

entry_points = \
{'console_scripts': ['adroit = adroit.cli:main']}

setup_kwargs = {
    'name': 'adroit',
    'version': '0.3',
    'description': 'Ansible Docker Role Testing',
    'long_description': "# `adroit` - Ansible Docker Role Testing\n\nHeavily opinionated tool for testing Ansible roles using Docker containers.\n\n### Assumptions and limitations\n\nThese are the current assumptions about your Ansible codebase which might prevent you from using Adroit. They are subject to change or improve.\n\n- You only deploy (or only want to test) on modern systems with systemd as their init system.\n- You have a `base` role which other roles can build upon. (If you don't need this, you can just have an empty `roles/base` directory).\n- With the exception of depending on the base role, your Ansible roles are atomic, indepentent, and can be applied individually. `include_role` and dependencies defined in `meta` should still work, though.\n\nFeel free to open a Github issue about any limitations that prevent you from using Adroit.\n\n### How it works\n\n1. Adroit builds a *core image* based on your distro of choice.\n2. A container based on the core image is created. The `base` role will be applied to the container, and it is saved as the *base image*.\n3. For each role you want to test, a container based on the base image is started, and the role under test will be applied.\n\nAdroit will check if the role playbook fails, and will also run the playbook a second time to test for idempotency - if there are any changes on the second run, we consider it a failure.\n\n### Precautions\n\nTo properly test Ansible using Docker containers, systemd needs to be running inside the containers. This requires the containers to run in privileged mode. There is a security risk involved here, check your base images and playbooks accordingly.\n\n## Usage\n\nIn a virtualenv or whatever you prefer: `pip install adroit`\n\nIn the root directory of your Ansible tree structure, which should at least contain a `roles` directory, run this command:\n\n```bash\nadroit -d debian:stretch myrole\n```\n\nWhere `debian:stretch` is the image you want to base your tests on. Currently supported are Debian, Ubuntu and CentOS.\n\n### Customizing your roles for testing\n\nCertain tasks simply cannot be ran inside a Docker container - for example, mounting `/proc` with `hidepid=2`. You should add a `when` clause to these tasks. Example:\n\n```yaml\n- when: ansible_virtualization_type != 'docker'\n  import_tasks: configure_network.yml\n```\n\nIf you need certain variables to be set which aren't in `defaults` or `vars` but should be set during testing, you can create a file like `roles/myrole/testing/test_vars.yml` and it will be applied when testing that particular role.\n\n## License\n\nThe contents of this repository is released under the [MIT license](http://opensource.org/licenses/MIT). See the LICENSE file included for details.\n",
    'author': 'Andreas Lutro',
    'author_email': 'anlutro@gmail.com',
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'entry_points': entry_points,
    'python_requires': '>=3.5,<4.0',
}


setup(**setup_kwargs)
