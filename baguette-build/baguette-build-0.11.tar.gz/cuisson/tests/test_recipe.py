#-*-coding:utf-8 -*-
"""
Test Recipe parse.
"""
#pylint:disable=wildcard-import,unused-wildcard-import,redefined-outer-name
from .fixtures import *

def test_get_valid_recette1(build, valid_recette1):#pylint:disable=unused-argument
    """
    Generate a dockerfile using a valid recette.
    """
    recipe = build.get_recipe()
    assert recipe.generate_dockerfile()
    dockerfile = open(os.path.join(recipe.path, 'Dockerfile'))
    config = [l.strip() for l in dockerfile.readlines()]
    #1. `FROM` statement at the first line of the Dockerfile
    print config
    assert config[0] == 'FROM python:3.6'
    #2. `COPY` statement at the second line
    assert config[1] == 'COPY * /root/'
    #3. `ENV` statement
    assert 'ENV PLATFORM=development' in config
    #4. `Run` statement
    assert 'RUN apt-get install -y python wget' in config
    assert 'RUN ls' in config
    #5. `CMD` statement at the end of the Dockerfile
    assert config[-1] == 'CMD echo "none"'
    #6. Check the whole file
    dockerfile.seek(0)
    assert dockerfile.read() == '''FROM python:3.6
COPY * /root/
ENV PLATFORM=development
RUN apt-get install -y python wget
RUN ls
CMD echo "none"'''

def test_generate_definition1(build, valid_recette1):
    """
    Test that the recipe generates the definition.
    """
    recipe = build.get_recipe()
    recipe.generate_definition()
    assert recipe.definition
    assert recipe.definition['instances'] == 1
    assert recipe.definition['branch'] == 'mybranch'
    assert recipe.definition['tag'].endswith('{0}/{1}/{2}:{3}'.format(recipe.definition['owner'], recipe.definition['repo'], recipe.definition['branch'], recipe.definition['uid']).lower())
    assert recipe.definition['namespace'] == '{}-default'.format(recipe.definition['owner'])
    assert recipe.definition['ports'] == [{'name': 'http-80', 'protocol':'TCP', 'number':80}]
    assert recipe.definition['healthchecks'] == []
    assert recipe.definition['private'] == True
    assert recipe.definition['domain_name'] == None
    assert recipe.definition['ports'] == [{'protocol':'TCP', 'number':80, 'name':'http-80'}]

def test_generate_definition2(build, valid_recette2, api_namespace):
    """
    Test that the recipe generates the definition.
    """
    recipe = build.get_recipe()
    recipe.generate_definition()
    assert recipe.definition
    assert recipe.definition['instances'] == 1
    assert recipe.definition['branch'] == 'mybranch'
    assert recipe.definition['tag'].endswith('{0}/{1}/{2}:{3}'.format(recipe.definition['owner'], recipe.definition['repo'], recipe.definition['branch'], recipe.definition['uid']).lower())
    assert recipe.definition['private'] == False
    assert recipe.definition['domain_name'] == 'mybranch.myrepo.owner.projects.baguette.io'
    assert recipe.definition['ports'] == [{'protocol':'UDP', 'number':1, 'name':'udp-1'}, {'protocol':'TCP', 'number':8000, 'name':'tcp-8000'}]
    assert recipe.definition['namespace'] == '{}-experimental'.format(recipe.definition['owner'])
    assert sorted(recipe.definition['ports']) == sorted([
        {'name': 'tcp-8000', 'protocol':'TCP', 'number':8000},
        {'name': 'udp-1', 'protocol':'UDP', 'number':1}])
    assert sorted(recipe.definition['healthchecks']) == sorted([
        {'initial_delay_seconds': 3,
         'interval_seconds': 10,
         'failure_threshold': 5,
         'success_threshold': 5,
         'path': '/',
         'port': 8000,
         'protocol': 'HTTP',
         'type': 'liveness',
         'timeout_seconds': 10},
        {'initial_delay_seconds': 3,
         'interval_seconds': 10,
         'failure_threshold': 5,
         'success_threshold': 5,
         'protocol': 'COMMAND',
         'timeout_seconds': 10,
         'type': 'readiness',
         'value': ['/usr/bin/ls']}
    ])

def test_cleanup(build, valid_recette1, docker_registry_cleanup):
    """
    Test that the recipe can cleanup.
    """
    recipe = build.get_recipe()
    with pytest.raises(KeyError):
        recipe.cleanup()
    #
    recipe.generate_definition()
    assert recipe.cleanup()

def test_no_cleanup(build, valid_recette1, docker_registry_cleanupko):
    """
    Test When a cleanup failed no exception is raised.
    """
    recipe = build.get_recipe()
    recipe.generate_definition()
    assert recipe.cleanup() is False

def test_build_dockerfile(build, valid_recette1, docker_registry_build):
    """
    Test on build_dockerfile()
    """
    recipe = build.get_recipe()
    recipe.generate_definition()
    assert recipe.build_dockerfile()

def test_build_dockerfile_ko(build, valid_recette1, docker_registry_buildko):
    """
    Test on build_dockerfile() : when it failes just return False.
    """
    recipe = build.get_recipe()
    recipe.generate_definition()
    assert recipe.build_dockerfile() is False

def test_push_dockerfile(build, valid_recette1, docker_registry_push):
    """
    Test on push_dockerfile()
    """
    recipe = build.get_recipe()
    recipe.generate_definition()
    assert recipe.push_dockerfile()

def test_push_dockerfile_ko(build, valid_recette1, docker_registry_pushko):
    """
    Test on push_dockerfile() : when it failes just return False.
    """
    recipe = build.get_recipe()
    recipe.generate_definition()
    assert recipe.push_dockerfile() is False

def test_full(build, valid_recette1, docker_registry_build, docker_registry_push, docker_registry_cleanup):#pylint:disable=unused-argument
    """
    Test that Recette1 image build and is pushed to the registry.
    """
    recipe = build.get_recipe()
    assert recipe.generate_definition()
    assert recipe.generate_dockerfile()
    assert recipe.build_dockerfile()
    assert recipe.push_dockerfile()
    assert build.cleanup()
