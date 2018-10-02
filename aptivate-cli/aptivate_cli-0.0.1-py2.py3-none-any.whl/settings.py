"""A configuration settings module."""

ANSIBLE_HOME_DIRECTORY = '.ansible'
ANSIBLE_REQUIREMENTS_FILE = 'requirements.yml'
ANSIBLE_PLAYBOOKS_DIRECTORY = 'playbooks'
ANSIBLE_INVENTORIES_DIRECTORY = 'inventories'
ANSIBLE_PLAYBOOK_FILE = 'deploy.yml'

ANSIBLE_INVENTORY_FILE = 'inventory'
ANSIBLE_ROLE_PATHS = [
    'external-roles',
]

PROJECT_PLAY_REPOSITORY_URL = 'git@git.coop:aptivate/ansible-plays/{}-play.git'
PROJECT_APP_REPOSITORY_URL = 'git@git.coop:aptivate/{}.git'

ROLE_TEMPLATE_URL = 'git@git.coop:aptivate/templates/role.git'
PLAY_TEMPLATE_URL = 'git@git.coop:aptivate/templates/play.git'
